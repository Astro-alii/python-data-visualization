import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
SF_df = pd.read_csv("raw_data_files/san_francisco_data_2000_2025.csv")
SAC_df = pd.read_csv("raw_data_files/sacramento_data_2000_2025.csv")


SF_df["DATE"] = pd.to_datetime(SF_df["DATE"])
SAC_df["DATE"] = pd.to_datetime(SAC_df["DATE"])

SF_df["MONTH"] = SF_df["DATE"].dt.month
SAC_df["MONTH"] = SAC_df["DATE"].dt.month

sf_avg_high = SF_df.groupby("MONTH")["TMAX"].mean()
sf_avg_low = SF_df.groupby("MONTH")["TMIN"].mean()
sac_avg_high = SAC_df.groupby("MONTH")["TMAX"].mean()
sac_avg_low = SAC_df.groupby("MONTH")["TMIN"].mean()


sf_avg_diurnal = sf_avg_high - sf_avg_low
sac_avg_diurnal = sac_avg_high - sac_avg_low


months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

x = np.arange(12)
plt.style.use('seaborn-v0_8-whitegrid')
plt.figure(figsize = (14,6))

plt.bar(x - 0.2 , sf_avg_diurnal, width = 0.2 , label = "SF RANGE" , color = '#E63946')
plt.bar(x + 0.2 , sac_avg_diurnal, width =0.2 , label = "SAC Range" , color = '#F4A261')


plt.xticks(x, months)
plt.title ("Temperature Range (°F)", fontsize=12)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Temperature Range (°F)", fontsize=12)


plt.savefig("graph3_diurnal_temp_range.png", dpi=150, bbox_inches='tight')
