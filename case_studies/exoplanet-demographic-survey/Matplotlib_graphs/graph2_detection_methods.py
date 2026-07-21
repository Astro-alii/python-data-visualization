import matplotlib.pyplot as plt 
import pandas as pd 

df = pd.read_csv("raw_data_files/exoplanets_raw.csv" , comment = "#")
df_clean = df.dropna(subset = ["discoverymethod"])

method_counts = df_clean["discoverymethod"].value_counts()

fig , ax = plt.subplots(figsize= (14, 7))
ax.barh(method_counts.index , method_counts.values) 
ax.invert_yaxis()

total_planets = sum(method_counts.values)


for index , count in enumerate (method_counts):
    percent = (count / total_planets) * 100
    ax.text (count +30  ,index , f"{count} ({percent:.1f}%)", fontsize = 9 , color= "#333333") 

ax.set_xlabel('Number of Planets')
ax.set_ylabel('Detection Method')
ax.tick_params(axis='y', labelsize=9)
ax.set_title('Exoplanet Discoveries by Detection Method')

plt.tight_layout()
plt.savefig('graph2_detection_methods.png', dpi=150, bbox_inches='tight')
plt.show()
