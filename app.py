import streamlit as st
import pandas as pd, numpy as np
from statsmodels.tsa.arima.model import ARIMA
import plotly.express as px

st.set_page_config(page_title="Netflix Forecast (ARIMA)", layout="wide")

st.title("📈 Netflix Subscriptions – ARIMA Forecast")
st.caption("CSV mit Spalten **Time Period** (Datum) & **Subscribers** (Zahl) hochladen.")

file = st.file_uploader("CSV hochladen", type=["csv"])
p = st.number_input("p", 0, 5, 1); d = st.number_input("d", 0, 2, 1); q = st.number_input("q", 0, 5, 1)
n_steps = st.slider("Vorhersagequartale", 1, 12, 5)

if file:
    df = pd.read_csv(file)
    # robustes Datum-Parsing
    df["Time Period"] = pd.to_datetime(df["Time Period"], dayfirst=True, errors="coerce")
    df = df.dropna(subset=["Time Period", "Subscribers"]).sort_values("Time Period")
    ts = df.set_index("Time Period")["Subscribers"].asfreq("QS").interpolate()

    # QoQ & YoY (quartalsbasiert)
    tmp = df.copy().set_index("Time Period").asfreq("QS")
    tmp["QoQ_%"] = tmp["Subscribers"].pct_change()*100
    tmp["YoY_%"] = tmp["Subscribers"].pct_change(4)*100

    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Quartalsverlauf")
        st.plotly_chart(px.line(tmp, x=tmp.index, y="Subscribers", labels={"x":"Datum","Subscribers":"Abonnenten"}), use_container_width=True)
        st.subheader("Quartalswachstum (QoQ, %)")
        st.bar_chart(tmp["QoQ_%"])
    with c2:
        st.subheader("Jahreswachstum (YoY, %)")
        st.bar_chart(tmp["YoY_%"])

    # ARIMA fit + Forecast
    try:
        model = ARIMA(ts, order=(int(p), int(d), int(q))).fit()
        pred = model.predict(len(ts), len(ts)+n_steps-1).clip(lower=0)
        pred = pred.round().astype(int)

        st.subheader("Vorhersage")
        fdf = pd.DataFrame({"Time Period": pred.index, "Predictions": pred.values})
        st.dataframe(fdf, use_container_width=True)

        st.download_button("⬇️ Forecast als CSV", fdf.to_csv(index=False), "forecast.csv", "text/csv")

        st.subheader("Plot")
        plot_df = pd.concat([ts.rename("Original"), pred.rename("Forecast")], axis=1)
        st.plotly_chart(px.line(plot_df, labels={"value":"Abonnenten","index":"Datum"}), use_container_width=True)

        st.caption("Hinweis: YoY ist quartalsbasiert (`pct_change(4)`) → mehr Detailtiefe als Jahresaggregation.")
    except Exception as e:
        st.error(f"Modellfehler: {e}")
else:
    st.info("Bitte CSV hochladen.")

    st.markdown(
    """
    ---
    **Made with ❤️ by Emr7y | Modell: ARIMA | Datenquelle: Kaggle / Aman Kharwal**
    """
)

