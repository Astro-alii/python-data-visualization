import matplotlib.pyplot as plt 
import pandas as pd
#Multi-Line Temperature Cross Over Plot
#Sacramento Daily High and Low using matplotlib and pandas
#5 graphs over 5 years windows

SAC_df = pd.read_csv("raw_data_files/sacramento_data_2000_2025.csv")


SAC_df["DATE"] = pd.to_datetime(SAC_df["DATE"])
                               
df1 = SAC_df[(SAC_df["DATE"] >= "2000-01-01") & (SAC_df["DATE"] <= "2004-12-31")]
df2 = SAC_df[(SAC_df["DATE"] >= "2005-01-01") & (SAC_df["DATE"] <= "2009-12-31")]
df3 = SAC_df[(SAC_df["DATE"] >= "2010-01-01") & (SAC_df["DATE"] <= "2014-12-31")]
df4 = SAC_df[(SAC_df["DATE"] >= "2015-01-01") & (SAC_df["DATE"] <= "2019-12-31")]
df5 = SAC_df[(SAC_df["DATE"] >= "2020-01-01") & (SAC_df["DATE"] <= "2025-12-31")]

plt.style.use('seaborn-v0_8-whitegrid')
fig , ax = plt.subplots(3,2,figsize = (15, 8))

fig.suptitle("Daily High & Low Temperatures — Sacramento (2000–2025)", fontsize=16, fontweight='bold')
# 2000-2005 Graph
ax[0,0].plot(df1["DATE"], df1["TMAX"], color = "#F4A261" , linewidth =0.5 , alpha = 0.7)
ax[0,0].plot(df1["DATE"], df1["TMIN"], color = "#2A9D8F" , linewidth =0.5 , alpha = 0.7)
ax[0,0].set_ylabel("Temperature (°F)" , fontsize = 12)
ax[0,0].set_xlabel("Date", fontsize = 12)
ax[0,0].tick_params(axis='both', labelsize=9)

# 2005 - 2010
ax[0,1].plot(df2["DATE"], df2["TMAX"], color = "#F4A261" , linewidth =0.5 , alpha = 0.7)
ax[0,1].plot(df2["DATE"], df2["TMIN"], color = "#2A9D8F" , linewidth =0.5 , alpha = 0.7)
ax[0,1].set_ylabel("Temperature (°F)" , fontsize = 12)
ax[0,1].set_xlabel("Date", fontsize = 12)
ax[0,1].tick_params(axis='both', labelsize=9)

# 2005 - 2010
ax[1,0].plot(df3["DATE"], df3["TMAX"], color = "#F4A261" , linewidth =0.5 , alpha = 0.7)
ax[1,0].plot(df3["DATE"], df3["TMIN"], color = "#2A9D8F", linewidth =0.5 , alpha = 0.7)
ax[1,0].set_ylabel("Temperature (°F)" , fontsize = 12)
ax[1,0].set_xlabel("Date", fontsize = 12)
ax[1,0].tick_params(axis='both', labelsize=9)

# 2010 - 2015
ax[1,1].plot(df4["DATE"], df4["TMAX"], color = "#F4A261" , linewidth =0.5 , alpha = 0.7)
ax[1,1].plot(df4["DATE"], df4["TMIN"], color = "#2A9D8F" , linewidth =0.5 , alpha = 0.7)
ax[1,1].set_ylabel("Temperature (°F)" , fontsize = 12)
ax[1,1].set_xlabel("Date", fontsize = 12)
ax[1,1].tick_params(axis='both', labelsize=9)

# 2015 - 2025
ax[2,0].plot(df5["DATE"], df5["TMAX"], color = "#F4A261" , linewidth =0.5 , alpha = 0.7)
ax[2,0].plot(df5["DATE"], df5["TMIN"], color = "#2A9D8F" , linewidth =0.5 , alpha = 0.7)
ax[2,0].set_ylabel("Temperature (°F)" , fontsize = 12)
ax[2,0].set_xlabel("Date", fontsize = 12)
ax[2,0].tick_params(axis='both', labelsize=9)

ax[2, 1].set_visible(False)

plt.tight_layout()
plt.savefig("graph1_daily_highlow_sac_matplotlib.png",dpi = 150 , bbox_inches='tight' ) 
