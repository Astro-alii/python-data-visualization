import plotly.express as px
import pandas as pd

df = pd.read_csv("raw_data_files/exoplanets_raw.csv" , comment = "#")
df_clean = df.dropna(subset = ["pl_masse" , "pl_rade"])

print (len (df_clean["pl_masse"]))
print (len (df_clean["pl_rade"]))

fig = px.scatter(df_clean, df_clean["pl_masse"], df_clean["pl_rade"], log_x= True , log_y= True,
                 color = "discoverymethod",
                 hover_name="pl_name", 
                 hover_data=["hostname", "disc_year"], 
                 labels = {"pl_masse": "Planet Mass (Earth Masses)",
                           "pl_rade":"Planet Radius (Earth Radii)", 
                           "discoverymethod": "Detection Method"},
                 title = "Exoplanet Mass-Radius Relationships")
                    
#Pnadas df from scratch
reference_planets = pd.DataFrame({
    'name': ['Earth', 'Neptune', 'Jupiter'],
    'mass': [1, 17.15, 317.8],
    'radius': [1, 3.88, 11.2]
})

fig.add_scatter(
    x=reference_planets['mass'],      # 3 x-positions: 1, 17.15, 317.8
    y=reference_planets['radius'],    # 3 y-positions: 1, 3.88, 11.2
    mode='markers+text',              # draw both a dot AND a text label
    text=reference_planets['name'],   # the actual words to display: 'Earth', 'Neptune', 'Jupiter'
    textposition='top center',        # position the text just above each dot
    marker=dict(size=14, color='black', symbol='star'),  # make these dots stand out — bigger, black, star-shaped
    name='Solar System Reference'     # what this layer is called in the legend
)


fig.write_html("graph3_mass_radius.html")
fig.show ()