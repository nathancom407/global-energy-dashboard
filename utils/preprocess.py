import pandas as pd

def load_and_clean_data(file_path):
    df = pd.read_csv(file_path)
    df = df[df['iso_code'].str.len() == 3]
    df['year'] = pd.to_numeric(df['year'], errors='coerce')
    df['primary_energy_consumption'] = df['primary_energy_consumption'].fillna(0)
    df['renewables_share_energy'] = df['renewables_share_energy'].fillna(0)
    df['gdp'] = df['gdp'].fillna(0)
    df['greenhouse_gas_emissions'] = df['greenhouse_gas_emissions'].fillna(0)
    return df

