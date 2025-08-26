# 📈 Netflix Subscriptions Forecasting (Python, ARIMA)

🚀 Mit **ARIMA (AutoRegressive Integrated Moving Average)** prognostieren wir die  
zukünftigen **Netflix-Abonnentenzahlen** auf Basis historischer Quartalsdaten.  

👉 Ergebnis: Ein kompakter Forecast der nächsten **5 Quartale**, visualisiert in Python.  

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSjiUrMYUOdgvXeA-D5pevIWdOhm_R5xInvr8PxTMJfUVi_2nAHsdsBpsuYXlNjvcuUAI8&usqp=CAU" width="400" style="display:block; margin-left:auto; margin-right:auto;">

---

## 🎬 Motivation
Netflix ist einer der größten Streaming-Giganten der Welt. Doch wie entwickeln sich die **Abonnentenzahlen in Zukunft**?  
Mit **Zeitreihenanalyse** (ARIMA) wagen wir den Blick nach vorne:  
Quartalswerte der Vergangenheit dienen uns als Grundlage, um die nächsten **5 Quartale** zu prognostizieren.  

---

## 🔍 Vorgehen
Der Workflow dieses Projekts umfasst:

1. **Datenaufbereitung** – Bereinigen & Strukturieren der historischen Quartalszahlen  
2. **Explorative Analyse** – Trends, Saisonalitäten & Wachstumsraten erkennen  
3. **Modellauswahl (ARIMA)** – geeignet für stationäre Zeitreihen mit klarer Trendkomponente  
4. **Training & Validierung** – Modell fitten, Forecast evaluieren  
5. **Forecast & Visualisierung** – zukünftige Abonnentenzahlen anschaulich darstellen  

---

## 🧠 Kurzer Exkurs: Was ist ARIMA?
ARIMA steht für **AutoRegressive Integrated Moving Average** und ist ein bewährtes Modell  
zur **Zeitreihenprognose**. Es kombiniert drei Bausteine:

- **AR (AutoRegressive):** nutzt vergangene Werte (Lags)  
- **I (Integrated):** macht die Serie stationär durch Differenzierung  
- **MA (Moving Average):** glättet Schwankungen über Residuen  

👉 Die Modellordnung **(p, d, q)** bestimmt:  
- **p:** Anzahl der Lags (AR-Anteil)  
- **d:** Differenzierungen (I-Anteil)  
- **q:** Fehler-/Rauschanteile (MA-Anteil)  

---

## 📊 Ergebnisse & Schlussfolgerung
- Mit **ARIMA(1,1,1)** konnten die Netflix-Abonnentenzahlen **robust modelliert** werden.  
- Die Prognose zeigt einen **weiter steigenden Trend**, wenn auch mit leicht abflachendem Wachstum.  
- Das Projekt verdeutlicht, wie **klassische Zeitreihenmodelle** praxisnah im Business-Kontext  
  (z. B. Entertainment-Branche, Marketingplanung) eingesetzt werden können.  

---

## 🛠️ Technologien
- **Python 3.x**  
- `pandas`, `numpy` – Datenaufbereitung  
- `statsmodels` – ARIMA-Modellierung  
- `plotly`, `matplotlib` – Visualisierungen  
- *(optional)* `streamlit` – interaktive Forecast-App  

---

## ▶️ Nutzung
1. Repository klonen  
   ```bash
   git clone https://github.com/DEINUSERNAME/netflix-forecast-arima.git
   cd netflix-forecast-arima
