import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np 

df = pd.read_csv("raw_data_files/exoplanets_raw.csv" , comment = "#")
df_clean = df.dropna(subset = ["pl_orbsmax" , "pl_orbper"])



fig , ax = plt.subplots(figsize = (10,5))
ax.scatter (df_clean["pl_orbsmax"] , df_clean["pl_orbper"],color='#1f77b4', s=8, alpha=0.4) # s=marker size, aplha= transparency control
ax.set_xscale("log")
ax.set_yscale("log")

ax.set_xlabel("Semi-Major Axis (AU)")
ax.set_ylabel("Orbital Period (Earth days)")
ax.set_title("Orbital Period vs. Semi-Major Axis — Verifying Kepler's Third Law")


#theoretically predicted plot , satisfying Kepler's Third Law
a_range = np.logspace(-3, 3, 100)
p_theoretical = a_range ** 1.5 * 365.25
ax.plot(a_range, p_theoretical, color='red', linewidth=2, label="Kepler's 3rd Law: P = a^1.5")

ax.legend()



plt.savefig("graph4_keplers_law.png",dpi=150, bbox_inches='tight')
plt.show()