import matplotlib.pyplot as plt
import plotly.express as px 
from pathlib import Path  
import csv

#Sitka weather trend over the year 2021
path = Path("weather_data/sitka_weather_07-2021.csv")
data_list =path.read_text().splitlines()
reader = csv.reader(data_list)
reader_ = next(reader)
high = [] #index 4
low = []  # index 5 
for read in reader:
    high.append(int (read[4]))
    low.append (int (read[5]))

fig , ax = plt.subplots(1,2,figsize= (10, 8))
ax[0].plot(high ,color = "red")

ax[1].plot(low , color = "blue")
plt.tight_layout()
plt.show()