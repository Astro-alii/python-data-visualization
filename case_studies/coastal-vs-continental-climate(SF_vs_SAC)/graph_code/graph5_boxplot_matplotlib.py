import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

SF_df = pd.read_csv("raw_data_files/san_francisco_data_2000_2025.csv")
SAC_df = pd.read_csv("raw_data_files/sacramento_data_2000_2025.csv")

SF_df["DATE"] = pd.to_datetime(SF_df["DATE"])
SAC_df["DATE"] = pd.to_datetime(SAC_df["DATE"])

SF_df["MONTH"] = SF_df["DATE"].dt.month

SAC_df["MONTH"] = SAC_df["DATE"].dt.month


SF_df['city'] = 'San Francisco'
SAC_df['city'] = 'Sacramento'

combined_df = pd.concat([SF_df, SAC_df], ignore_index=True)

plt.figure(figsize=(16, 6))
sns.boxplot(data=combined_df, x='MONTH', y='TMAX', hue='city', 
            palette={'San Francisco': '#E63946', 'Sacramento': '#F4A261'})
plt.xticks(range(1,13), ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
plt.savefig('graph5_boxplot.png', dpi=150, bbox_inches='tight')
