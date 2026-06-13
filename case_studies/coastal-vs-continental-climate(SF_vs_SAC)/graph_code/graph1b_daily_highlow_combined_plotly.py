import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

SF_df = pd.read_csv("raw_data_files/san_francisco_data_2000_2025.csv")
SAC_df = pd.read_csv("raw_data_files/sacramento_data_2000_2025.csv")


SF_df['sf_high_roll'] = SF_df['TMAX'].rolling(30).mean()
SF_df['sf_low_roll'] = SF_df['TMIN'].rolling(30).mean()
SAC_df['sac_high_roll'] = SAC_df['TMAX'].rolling(30).mean()
SAC_df['sac_low_roll'] = SAC_df['TMIN'].rolling(30).mean()

fig = go.Figure()

fig.add_trace(go.Scatter(x=SF_df["DATE"], y=SF_df["sf_high_roll"], name="SF High", line=dict(color='#E63946', width=1.5)))
fig.add_trace(go.Scatter(x=SF_df["DATE"], y=SF_df["sf_low_roll"], name="SF Low", line=dict(color='#457B9D', width=1.5)))
fig.add_trace(go.Scatter(x=SAC_df["DATE"], y=SAC_df["sac_high_roll"], name="SAC High", line=dict(color='#F4A261', width=1.5)))
fig.add_trace(go.Scatter(x=SAC_df["DATE"], y=SAC_df["sac_low_roll"], name="SAC Low", line=dict(color='#2A9D8F', width=1.5)))

fig.update_layout(
    xaxis_title ="Date" ,
    yaxis_title ="Temperature (°F)" , 
    height=600,
    xaxis=dict(rangeslider=dict(visible=True)),
    title="Daily Rolling Temperatures — San Francisco vs Sacramento (2000–2025)"
)
fig.write_html("graph1b_daily_highlow_combined_rolling_plotly.html")