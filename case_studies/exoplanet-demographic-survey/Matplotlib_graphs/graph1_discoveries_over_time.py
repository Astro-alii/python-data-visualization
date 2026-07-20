import matplotlib.pyplot as  plt 
import pandas as pd

df = pd.read_csv("raw_data_files/exoplanets_raw.csv" , comment = "#")
df_clean = df.dropna(subset=['disc_year', 'discoverymethod'])

grouped = df_clean.groupby(['disc_year', 'discoverymethod'])



counts = grouped.size()
clean_table = counts.unstack(fill_value =0)

years = clean_table.index
# discovery methods
transit = clean_table["Transit"] 
radial_velocity = clean_table["Radial Velocity"]
microlensing = clean_table["Microlensing"]
imaging = clean_table["Imaging"]
transit_timing_variations = clean_table["Transit Timing Variations"]
eclipse_timing_variations = clean_table["Eclipse Timing Variations"]
orbital_brightness_modulation = clean_table["Orbital Brightness Modulation"]
pulsar_timing = clean_table ["Pulsar Timing"]
astrometry = clean_table["Astrometry"]
pulsation_timing_variation = clean_table["Pulsation Timing Variations"]
disk_kinematics = clean_table["Disk Kinematics"]


bar_width = 0.85
fig , ax = plt.subplots(figsize = (14 , 7))
plt.bar(years , transit , color = "#1f77b4" , label = "Transit" , width= bar_width)
plt.bar(years , radial_velocity , color = "#ff7f0e" ,label = "Radial Velocity", width = bar_width)
plt.bar(years , microlensing , color = "#17becf" , label = "Microlensing", width = bar_width)
plt.bar(years , imaging, color = "#9467bd" , width = bar_width , label = "Imaging")
plt.bar(years , transit_timing_variations , color = "#2ca02c" , width = bar_width, label = "Transit Timing Variations")
plt.bar(years , eclipse_timing_variations , color = "#e377c2" , width = bar_width, label = "Eclipse Timing Variations")
plt.bar(years , orbital_brightness_modulation , color = "#8c564b" , width = bar_width, label = "Orbital Brightness Modulation")
plt.bar(years , pulsar_timing , color = "#7f7f7f" , width = bar_width , label = "Pulsar Timing")
plt.bar(years , astrometry , color = "#bcbd22" , width = bar_width , label = "Astrometry")
plt.bar(years , pulsation_timing_variation , color = "#c7c7c7" , width = bar_width, label = "Pulsation Timing Variation")
plt.bar(years , disk_kinematics , color = "#dbdb8d", width = bar_width, label = "Disk Kinematics")


ax.set_xlabel('Discovery Year')
ax.set_ylabel('Number of Planets Discovered')
ax.set_title('Exoplanet Discoveries Over Time by Detection Method')
ax.legend(title='Detection Method', bbox_to_anchor=(1.02, 1), loc='upper left', fontsize='small')

ax.axvline(x=2009, color='red', linestyle='--', alpha=0.5, linewidth=1)
ax.text(2009.3, 1300, 'Kepler launch (2009)', color='red', fontsize=9, rotation=0)

ax.axvline(x=2018, color='darkred', linestyle='--', alpha=0.5, linewidth=1)
ax.text(2018.3, 1300, 'TESS launch (2018)', color='darkred', fontsize=9)




plt.tight_layout()
#plt.savefig("graph1_discoveries_over_time.png", dpi=150, bbox_inches='tight')
plt.show()