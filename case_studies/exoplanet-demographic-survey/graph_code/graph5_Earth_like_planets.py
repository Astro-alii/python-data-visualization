import plotly.express as px 
import pandas as pd 

df = pd.read_csv("raw_data_files/exoplanets_raw.csv" , comment = "#")
df_clean = df.dropna(subset = ["pl_eqt", "pl_rade"])


fig = px.scatter(
    df_clean,
    x='pl_eqt',
    y='pl_rade',
    
    color='discoverymethod',
    hover_name='pl_name',
    hover_data=['hostname', 'pl_orbper', 'st_teff'],
    labels={
        'pl_eqt': 'Equilibrium Temperature (K)',
        'pl_rade': 'Planet Radius (Earth Radii)',
        'discoverymethod': 'Detection Method'
    },
    title='Exoplanet Habitable Zone Candidates'
)
fig.add_shape(
    type="rect",
    x0=200, x1=320,
    y0=0.8, y1=1.6,
    line=dict(color="green", dash="dash"),
    fillcolor="green",
    opacity=0.15

)

fig.add_annotation(
    x=260, y=1.9,
    text="Roughly Earth-like zone",
    showarrow=False,
    font=dict(color="green", size=12)
)




fig.write_html("graph5_Earth_like_planets.html")
fig.show()