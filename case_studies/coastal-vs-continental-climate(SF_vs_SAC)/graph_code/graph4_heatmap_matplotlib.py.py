import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 


SF_df = pd.read_csv("raw_data_files/san_francisco_data_2000_2025.csv")
SAC_df = pd.read_csv("raw_data_files/sacramento_data_2000_2025.csv")

SF_df["DATE"] = pd.to_datetime(SF_df["DATE"])
SAC_df["DATE"] = pd.to_datetime(SAC_df["DATE"])

SF_df["YEAR"] = SF_df["DATE"].dt.year
SF_df["MONTH"] = SF_df["DATE"].dt.month

SAC_df["YEAR"] = SAC_df["DATE"].dt.year
SAC_df["MONTH"] = SAC_df["DATE"].dt.month

sf_group = SF_df.groupby(["MONTH","YEAR"])
sf_heat = sf_group["TMAX"].mean().unstack()


sac_group = SAC_df.groupby(["MONTH","YEAR"])
sac_heat = sac_group["TMAX"].mean().unstack()


fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 7))

sns.heatmap(sf_heat, cmap='RdYlBu_r', ax=ax1)
sns.heatmap(sac_heat, cmap='RdYlBu_r', ax=ax2)

ax1.set_title("SF Daily High Temperature Heatmap (2000–2025)", fontsize=14)
ax2.set_title("Sacramento Daily High Temperature Heatmap (2000–2025)", fontsize=14)

fig.suptitle("Monthly Average High Temperatures — SF vs Sacramento", fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig("graph4_heatmap.png",dpi = 150 , bbox_inches= "tight")
