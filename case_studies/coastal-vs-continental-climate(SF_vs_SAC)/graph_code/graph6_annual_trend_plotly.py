import plotly.graph_objects as go 
import pandas as pd
import numpy as np

SF_df = pd.read_csv("raw_data_files/san_francisco_data_2000_2025.csv")
SAC_df = pd.read_csv("raw_data_files/sacramento_data_2000_2025.csv")

SF_df["DATE"] = pd.to_datetime(SF_df["DATE"])
SAC_df["DATE"] = pd.to_datetime(SAC_df["DATE"])

SF_df["YEAR"] = SF_df["DATE"].dt.year
SAC_df["YEAR"] = SAC_df["DATE"].dt.year 

SF_df["TMEAN"] = (SF_df["TMAX"] + SF_df["TMIN"])  / 2
SAC_df["TMEAN"] = (SAC_df["TMAX"] + SAC_df["TMIN"])  / 2


sf_yearly_avg= SF_df.groupby("YEAR")["TMEAN"].mean()
sac_yearly_avg = SAC_df.groupby("YEAR")["TMEAN"].mean()

sf_trend = np.polyfit(sf_yearly_avg.index.values , sf_yearly_avg, 1)
sf_trendline = np.poly1d(sf_trend)

sac_trend = np.polyfit(sac_yearly_avg.index.values , sac_yearly_avg, 1)
sac_trendline = np.poly1d(sac_trend)

fig = go.Figure()

fig.add_trace(go.Scatter(
    x= sf_yearly_avg.index.values  ,        # x axis data
    y=sf_yearly_avg, # y axis data
    name='SF Mean',    # legend label
    line=dict(
        color='#E63946',  # line color
        width=2           # line thickness
    )))
fig.add_trace(go.Scatter(
    x= sac_yearly_avg.index.values  ,        # x axis data
    y=sac_yearly_avg, # y axis data
    name='SAC Mean',    # legend label
    line=dict(
        color='#F4A261',  # line color
        width=2           # line thickness
    )))

fig.add_trace(go.Scatter(x=sf_yearly_avg.index.values,
                          y=sf_trendline(sf_yearly_avg.index.values), 
                          name='SF Trend', 
                          line=dict(color='#E63946', width=1.5, dash='dash')))
fig.add_trace(go.Scatter(x=sac_yearly_avg.index.values,
                        y=sac_trendline(sac_yearly_avg.index.values), 
                        name='SAC Trend', 
                        line=dict(color='#F4A261', width=1.5, dash='dash')))

fig.update_layout(
    title="Annual Average High Temperature Trend — SF vs Sacramento (2000–2025)",
    xaxis_title="Year",
    yaxis_title="Average Temperature (°F)",
    height=600
)
fig.write_html("graph6_annual_trend_plotly.html")