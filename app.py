import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
from utils.preprocess import load_and_clean_data

df = load_and_clean_data("owid-energy-data.csv")
available_countries = df['country'].dropna().unique().tolist()

year_min = int(df['year'].min())
year_max = int(df['year'].max())

energy_sources = ['coal_share_energy', 'oil_share_energy', 'gas_share_energy',
                  'nuclear_share_energy', 'renewables_share_energy']
df_melted = df[['country', 'year'] + energy_sources].fillna(0).melt(
    id_vars=['country', 'year'],
    value_vars=energy_sources,
    var_name='energy_type', value_name='share')

df_map = df[['iso_code', 'country', 'year', 'renewables_share_energy']].fillna(0)
df_biofuel = df[['iso_code', 'country', 'year', 'biofuel_share_energy']].fillna(0)

df_scatter = df[['country', 'year', 'gdp', 'energy_per_capita', 'population']].dropna()

df_electricity = df[['country', 'year', 'electricity_generation', 'electricity_demand']].dropna()

df_solar_wind = df[['country', 'year', 'solar_share_energy', 'wind_share_energy']].fillna(0).melt(
    id_vars=['country', 'year'],
    value_vars=['solar_share_energy', 'wind_share_energy'],
    var_name='source', value_name='share')

app = dash.Dash(__name__)
app.title = "Global Energy Dashboard"

app.layout = html.Div([
    html.H1("Global Energy Dashboard"),

    dcc.Tabs([
        # Tab 1
        dcc.Tab(label='Primary Energy Consumption', children=[
            dcc.Dropdown(id="country-dropdown", options=[{"label": c, "value": c} for c in available_countries],
                         value="United States", clearable=False),
            dcc.RangeSlider(id="year-slider", min=year_min, max=year_max, value=[2000, 2020],
                            marks={str(y): str(y) for y in range(1990, 2025, 5)}, step=1),
            dcc.Graph(id="energy-consumption-graph")
        ]),

        # Tab 2
        dcc.Tab(label='Energy Mix Over Time', children=[
            dcc.Dropdown(id="country-energy-mix", options=[{"label": c, "value": c} for c in available_countries],
                         value="United States", clearable=False),
            dcc.RangeSlider(id="energy-mix-year-slider", min=year_min, max=year_max, value=[2000, 2020],
                            marks={str(y): str(y) for y in range(1990, 2025, 5)}, step=1),
            dcc.Graph(id="energy-mix-area")
        ]),

        # Tab 3
        dcc.Tab(label='Global Renewables Map', children=[
            dcc.Slider(id='map-year-slider', min=year_min, max=year_max, value=2020,
                       marks={str(y): str(y) for y in range(1990, 2025, 5)}, step=1),
            dcc.Graph(id="renewables-map")
        ]),

        # Tab 4
        dcc.Tab(label='Energy per Capita vs GDP', children=[
            dcc.Slider(id="scatter-year-slider", min=year_min, max=year_max, value=2020,
                       marks={str(y): str(y) for y in range(1990, 2025, 5)}, step=1),
            dcc.Graph(id="energy-gdp-scatter")
        ]),

        # Tab 5
        dcc.Tab(label='Electricity Supply vs Demand', children=[
            dcc.Dropdown(id="country-electricity", options=[{"label": c, "value": c} for c in available_countries],
                         value="United States", clearable=False),
            dcc.Graph(id="electricity-line")
        ]),

        # Tab 6
        dcc.Tab(label='Solar vs Wind Trends', children=[
            dcc.Dropdown(id="country-solar-wind", options=[{"label": c, "value": c} for c in available_countries],
                         value="United States", clearable=False),
            dcc.Graph(id="solar-wind-line")
        ]),

        # Tab 7
        dcc.Tab(label='Biofuel Share Map', children=[
            dcc.Slider(id='biofuel-year-slider', min=year_min, max=year_max, value=2020,
                       marks={str(y): str(y) for y in range(1990, 2025, 5)}, step=1),
            dcc.Graph(id="biofuel-map")
        ])
    ])
])

@app.callback(Output("energy-consumption-graph", "figure"),
              Input("country-dropdown", "value"), Input("year-slider", "value"))
def update_energy_chart(country, year_range):
    filtered = df[(df["country"] == country) &
                  (df["year"] >= year_range[0]) &
                  (df["year"] <= year_range[1])]
    return px.line(filtered, x="year", y="primary_energy_consumption",
                   title=f"{country}: Primary Energy Consumption ({year_range[0]}–{year_range[1]})")

@app.callback(Output("energy-mix-area", "figure"),
              Input("country-energy-mix", "value"), Input("energy-mix-year-slider", "value"))
def update_area_chart(country, year_range):
    filtered = df_melted[(df_melted['country'] == country) &
                         (df_melted['year'] >= year_range[0]) &
                         (df_melted['year'] <= year_range[1])]
    return px.area(filtered, x="year", y="share", color="energy_type",
                   title=f"{country}: Energy Mix ({year_range[0]}–{year_range[1]})")

@app.callback(Output("renewables-map", "figure"),
              Input("map-year-slider", "value"))
def update_map(year):
    filtered = df_map[df_map["year"] == year]
    return px.choropleth(filtered, locations="iso_code", color="renewables_share_energy",
                          hover_name="country", color_continuous_scale="Viridis",
                          title=f"Renewable Energy Share by Country ({year})")

@app.callback(Output("energy-gdp-scatter", "figure"),
              Input("scatter-year-slider", "value"))
def update_scatter(year):
    filtered = df_scatter[df_scatter["year"] == year]
    return px.scatter(filtered, x="gdp", y="energy_per_capita", size="population", hover_name="country",
                      title=f"Energy per Capita vs GDP ({year})", log_x=True, size_max=60)

@app.callback(Output("electricity-line", "figure"),
              Input("country-electricity", "value"))
def update_electricity_chart(country):
    filtered = df_electricity[df_electricity['country'] == country]
    fig = px.line(filtered, x="year", y="electricity_generation", labels={"electricity_generation": "TWh"},
                  title=f"{country}: Electricity Generation vs Demand")
    fig.add_scatter(x=filtered['year'], y=filtered['electricity_demand'], mode='lines', name='Electricity Demand')
    return fig

@app.callback(Output("solar-wind-line", "figure"),
              Input("country-solar-wind", "value"))
def update_solar_wind_chart(country):
    filtered = df_solar_wind[df_solar_wind['country'] == country]
    return px.line(filtered, x="year", y="share", color="source",
                   title=f"{country}: Solar vs Wind Share Over Time")

@app.callback(Output("biofuel-map", "figure"),
              Input("biofuel-year-slider", "value"))
def update_biofuel_map(year):
    filtered = df_biofuel[df_biofuel["year"] == year]
    return px.choropleth(filtered, locations="iso_code", color="biofuel_share_energy",
                          hover_name="country", color_continuous_scale="YlOrBr",
                          title=f"Biofuel Share by Country ({year})")

if __name__ == "__main__":
    app.run(debug=True)
