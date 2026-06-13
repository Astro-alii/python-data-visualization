import plotly.graph_objects as go 
import pandas as pd
import numpy as np

SF_df = pd.read_csv("raw_data_files/san_francisco_data_2000_2025.csv")
SAC_df = pd.read_csv("raw_data_files/sacramento_data_2000_2025.csv")

SF_df["DATE"] = pd.to_datetime(SF_df["DATE"])
SAC_df["DATE"] = pd.to_datetime(SAC_df["DATE"])

SF_df["MONTH"] = SF_df["DATE"].dt.month
SAC_df["MONTH"]= SAC_df["DATE"].dt.month

sf_avg_high = SF_df.groupby('MONTH')['TMAX'].mean()
sf_avg_low = SF_df.groupby('MONTH')['TMIN'].mean()
sac_avg_high = SAC_df.groupby('MONTH')['TMAX'].mean()
sac_avg_low = SAC_df.groupby('MONTH')['TMIN'].mean()


months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
fig = go.Figure()

fig.add_trace(go.Scatter(  
    x=months,
    y= sf_avg_high,
    name = "SF High",
    line = dict(color = "#E63946" , width = 2)))

fig.add_trace(go.Scatter(  
    x=months,
    y= sf_avg_low,
    name = "SF Low",
    line = dict(color = "#457B9D" , width = 2)))

fig.add_trace(go.Scatter(  
    x=months,
    y= sac_avg_high,
    name = "SAC High",
    line = dict(color = "#F4A261" , width = 2)))

fig.add_trace(go.Scatter(  
    x=months,
    y= sac_avg_low,
    name = "SAC Low",
    line = dict(color = "#2A9D8F" , width = 2)))

fig.update_layout(
    title="Monthly Average Temperatures — SF vs Sacramento",
    xaxis_title="Month",
    yaxis_title="Average Temperature (°F)",
    height=600
)
fig.write_html('graph2_monthly_avg_line.html')
