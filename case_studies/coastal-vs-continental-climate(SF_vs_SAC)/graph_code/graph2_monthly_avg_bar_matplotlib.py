import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np


SF_df = pd.read_csv("raw_data_files/san_francisco_data_2000_2025.csv")
SAC_df = pd.read_csv("raw_data_files/sacramento_data_2000_2025.csv")

SF_df["DATE"] = pd.to_datetime(SF_df["DATE"])
SAC_df["DATE"] = pd.to_datetime(SAC_df["DATE"])

SF_df['MONTH'] = SF_df['DATE'].dt.month
SAC_df['MONTH'] = SAC_df['DATE'].dt.month


sf_avg_high = SF_df.groupby('MONTH')['TMAX'].mean()
sf_avg_low = SF_df.groupby('MONTH')['TMIN'].mean()
sac_avg_high = SAC_df.groupby('MONTH')['TMAX'].mean()
sac_avg_low = SAC_df.groupby('MONTH')['TMIN'].mean()

months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
plt.figure(figsize=(14,6))
x = np.arange(12)
width = 0.2

plt.bar(x - 1.5*width, sf_avg_high.values, width, label='SF High', color='#E63946')
plt.bar(x - 0.5*width, sf_avg_low.values, width, label='SF Low', color='#457B9D')
plt.bar(x + 0.5*width, sac_avg_high.values, width, label='SAC High', color='#F4A261')
plt.bar(x + 1.5*width, sac_avg_low.values, width, label='SAC Low', color='#2A9D8F')
plt.xlabel("Month", fontsize=12)
plt.ylabel("Average Temperature (°F)",fontsize=12)
plt.xticks(x, months, fontsize=10)
plt.title("Monthly Average High & Low Temperatures — SF vs Sacramento (2000–2025)")
plt.legend(fontsize=10)
plt.savefig("graph2_monthly_avg_bar.png", dpi=150, bbox_inches="tight")