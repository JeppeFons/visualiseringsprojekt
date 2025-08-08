import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html, Input, Output


import pandas as pd
import plotly.express as px

# Load dit data
df = pd.read_csv(r'C:\Job_og_eksamensbevis\Github\projekter\visualisering_projekt\data\GDI_2000_2020.csv')

# Antag df har kolonner: 'Country_Code' (ISO Alpha-3), 'Year', og 'GDP_per_Capita' eller anden måling

# Filtrer evt. for et bestemt år
df_2020 = df[df['year'] == 2020]

fig = px.choropleth(
    df_2020,
    locations='country_code',        # ISO Alpha-3 koder, fx 'DNK' for Danmark
    color='gdp_per_capita',          # Værdien, der skal farvelægges efter
    hover_name='country_name',            # Navn ved hover
    color_continuous_scale='Viridis',
    title='GDP per Capita 2020',
)

fig.show()

