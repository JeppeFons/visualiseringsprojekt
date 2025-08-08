import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# --- TIP: For at få hele Streamlit UI i mørkt tema, opret filen ~/.streamlit/config.toml med:
# [theme]
# base="dark"
# primaryColor="#1abc9c"
# backgroundColor="#0e1117"
# secondaryBackgroundColor="#262730"
# textColor="#fafafa"
# font="sans serif"

# Sæt matplotlib til dark background stil
plt.style.use('dark_background')

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv(r'C:\Job_og_eksamensbevis\Github\projekter\visualisering_projekt\data\GDI_2000_2020.csv')
    return df

df = load_data()

st.title("Interaktivt Dashboard - Økonomiske og Miljømæssige Data (Mørkt Tema)")

# Sidebar for valg
st.sidebar.header("Filtrer data")
years = st.sidebar.slider("Vælg år", int(df['year'].min()), int(df['year'].max()), (2000, 2020))
regions = st.sidebar.multiselect("Vælg region(er)", options=df['region'].unique(), default=df['region'].unique())

# Filtrer data baseret på valg
filtered_df = df[(df['year'] >= years[0]) & (df['year'] <= years[1]) & (df['region'].isin(regions))]

# Missing data heatmap
if st.sidebar.checkbox("Vis Missing Data Heatmap"):
    st.subheader("Missing Values Heatmap")
    fig, ax = plt.subplots(figsize=(14,6))
    fig.patch.set_facecolor('#0e1117')
    ax.set_facecolor('#0e1117')
    sns.heatmap(filtered_df.isnull(), cbar=False, cmap='viridis', ax=ax)
    ax.title.set_color('white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.tick_params(colors='white')
    st.pyplot(fig)

# Correlation matrix
if st.sidebar.checkbox("Vis Korrelationsmatrix"):
    corr_cols = [
        'gdp_usd', 'population', 'gdp_per_capita', 'inflation_rate', 'unemployment_rate',
        'co2_emissions_kt', 'renewable_energy_pct', 'life_expectancy', 'internet_usage_pct',
        'mobile_subscriptions_per_100', 'human_development_index'
    ]
    st.subheader("Korrelationsmatrix")
    fig, ax = plt.subplots(figsize=(12, 10))
    fig.patch.set_facecolor('#0e1117')
    ax.set_facecolor('#0e1117')
    corr = filtered_df[corr_cols].corr()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm', square=True, linewidths=.5, ax=ax)
    ax.title.set_color('white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.tick_params(colors='white')
    st.pyplot(fig)

# Scatter plot GDP vs CO2 emissions
if st.sidebar.checkbox("Vis GDP vs CO2 Emissioner"):
    st.subheader("GDP per Capita vs CO2 Emissions per Capita")
    fig = px.scatter(
        filtered_df, x='gdp_per_capita', y='co2_emissions_per_capita_tons',
        size='population', color='income_group', hover_name='country_name',
        title='GDP per Capita vs CO2 Emissions per Capita',
        size_max=60, log_x=True, log_y=True,
        template='plotly_dark'
    )
    st.plotly_chart(fig)

# Lineplot for CO2 emissions over tid
if st.sidebar.checkbox("Vis CO2 Emissioner Over Tid"):
    st.subheader("Gennemsnitlige CO2 Emissioner Over Tid efter Region")
    fig, ax = plt.subplots(figsize=(12, 6))
    fig.patch.set_facecolor('#0e1117')
    ax.set_facecolor('#0e1117')
    sns.lineplot(data=filtered_df, x='year', y='co2_emissions_kt', hue='region', estimator='mean', ax=ax)
    ax.set_title('Average CO2 Emissions (kt) Over Time by Region', color='white')
    ax.set_ylabel('CO2 Emissions (kt)', color='white')
    ax.set_xlabel('Year', color='white')
    ax.legend(title='Region')
    for text in ax.legend().get_texts():
        text.set_color("white")
    ax.tick_params(colors='white')
    st.pyplot(fig)

# Dual-axis plot CO2 emissions vs Renewable energy
if st.sidebar.checkbox("Vis CO2 Emissioner vs Vedvarende Energi"):
    st.subheader("CO2 Emissioner vs Vedvarende Energi Over Tid")
    fig, ax1 = plt.subplots(figsize=(12, 6))
    fig.patch.set_facecolor('#0e1117')
    ax1.set_facecolor('#0e1117')

    ax1.set_xlabel('Year', color='white')
    ax1.set_ylabel('CO2 Emissions (kt)', color='tab:red')
    sns.lineplot(data=filtered_df, x='year', y='co2_emissions_kt', ax=ax1, label='CO2 Emissions', color='tab:red')
    ax1.tick_params(axis='x', colors='white')
    ax1.tick_params(axis='y', colors='tab:red')

    ax2 = ax1.twinx()
    ax2.set_ylabel('Renewable Energy (%)', color='tab:green')
    sns.lineplot(data=filtered_df, x='year', y='renewable_energy_pct', ax=ax2, label='Renewable Energy', color='tab:green')
    ax2.tick_params(axis='y', colors='tab:green')

    plt.title('CO2 Emissions vs Renewable Energy Over Time', color='white')
    fig.tight_layout()
    st.pyplot(fig)

# --- CO2 Intensity per Region ---
if st.sidebar.checkbox("Vis CO2 Intensity per Million GDP by Region"):
    st.subheader("CO2 Intensity per Million GDP by Region")
    fig, ax = plt.subplots(figsize=(12, 6))
    fig.patch.set_facecolor('#0e1117')
    ax.set_facecolor('#0e1117')
    sns.boxplot(data=filtered_df, x='region', y='co2_intensity_per_million_gdp', ax=ax)
    ax.set_title('CO2 Intensity per Million GDP by Region', color='white')
    ax.set_xlabel('Region', color='white')
    ax.set_ylabel('CO2 Intensity per Million GDP', color='white')
    ax.tick_params(colors='white')
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", color='white')
    st.pyplot(fig)