# 🌍 Global Energy Dashboard

An interactive, multi-page dashboard application built with **Plotly Dash**, this project showcases skills in **data wrangling**, **Python-based EDA**, **interactive visualization**, and **dashboard design**. Using public data from [Our World in Data](https://github.com/owid/energy-data), the app enables real-time exploration of global energy consumption, production, and sustainability patterns.

---

## ✨ Project Objectives

- ✅ Showcase dashboard engineering and visualization design in **Plotly Dash**
- ✅ Demonstrate interactive **multi-tab app development**
- ✅ Apply **data preprocessing and feature selection** with Pandas
- ✅ Communicate insights through effective visual analytics
- ✅ Provide global and country-level views on energy trends

---

## 📊 Visualizations Overview

The dashboard contains **7 interactive pages**, each with custom interactivity, dropdowns, sliders, and dynamic Plotly charts.

### 1. Primary Energy Consumption
- **Type:** Line Chart  
- **Filters:** Country, Year Range  
- **Goal:** Show long-term energy usage trends

### 2. Energy Mix Over Time
- **Type:** Stacked Area Chart  
- **Filters:** Country, Year Range  
- **Goal:** Display changes in energy source reliance (coal, oil, gas, nuclear, renewables)

### 3. Global Renewables Map
- **Type:** Choropleth Map  
- **Filters:** Year  
- **Goal:** Compare countries by renewable share of energy

### 4. Energy per Capita vs GDP
- **Type:** Bubble Scatter Plot  
- **Filters:** Year  
- **Goal:** Correlate economic growth with energy intensity (bubble size = population)

### 5. Electricity Supply vs Demand
- **Type:** Dual Line Chart  
- **Filters:** Country  
- **Goal:** Compare generation capacity to national demand

### 6. Solar vs Wind Trends
- **Type:** Line Chart  
- **Filters:** Country  
- **Goal:** Compare the rise of solar vs wind over time

### 7. Biofuel Share Map
- **Type:** Choropleth Map  
- **Filters:** Year  
- **Goal:** Highlight biofuel dependency globally

---

## 🧠 Skills Demonstrated

- **📌 Plotly Dash:** Multi-tab layout, callbacks, dynamic interactivity  
- **📌 Python EDA:** Cleaning, filtering, reshaping (`melt`, `fillna`, `dropna`)  
- **📌 Data Wrangling:** Country-level and time-series segmentation  
- **📌 Data Visualization:** Line charts, area plots, scatter plots, choropleths  
- **📌 UI/UX:** Responsive layout, color scaling, annotations, dropdowns  
- **📌 Modular Code Structure:** Use of `utils/preprocess.py` for reusable data pipelines

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/global-energy-dashboard.git
cd global-energy-dashboard

## 2. Install Dependencies

Create a virtual environment and install requirements:

```bash
pip install -r requirements.txt
```

---

## 3. Add Dataset

Download `owid-energy-data.csv` from [OWID Energy GitHub](https://github.com/owid/energy-data) and place it in the project root (or update the path in `app.py`).

---

## 4. Run the App

```bash
python app.py
```

Then open your browser and visit:

[http://127.0.0.1:8050](http://127.0.0.1:8050)

---

## 📂 File Structure

```bash
├── app.py                    # Main Dash application
├── utils/
│   └── preprocess.py         # Data loading and cleaning
├── owid-energy-data.csv      # Public energy dataset
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

---

## 📦 requirements.txt

```ini
dash==2.15.0
plotly==5.19.0
pandas==2.2.2
```

---

## 📄 Data Source

Data provided by [Our World in Data](https://ourworldindata.org/energy), covering over a century of energy production, consumption, and emissions by country.

---

## 📜 License

This project is open source and built entirely on public data. All credit for raw data goes to OWID. You are free to use, modify, and share this dashboard under the terms of the [Creative Commons BY 4.0 License](https://creativecommons.org/licenses/by/4.0/).

---

## 🤝 Connect

If you find this dashboard useful or want to collaborate on data visualization or analytics projects, feel free
