import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import plotly.express as px 
from pathlib import Path  
import csv
from datetime import datetime

#Sitka weather trend over the year 2021
path = Path("weather_data/sitka_weather_2021_simple.csv")
data_list =path.read_text().splitlines()
reader = csv.reader(data_list)
reader_ = next(reader)
high = [] #index 4
low = [] # index 5 
date = []
for read in reader:
    high.append( int(read[4]))
    low.append (int(read[5]))
    date.append(datetime.strptime(read[2], "%Y-%m-%d"))

fig =plt.figure(figsize = (12,8))
grid = gridspec.GridSpec(2,2)

#High plot 
ax1 = fig.add_subplot(grid[0,0])
ax1.plot(date ,high , color = "red")
ax1.set_title("Daily High")
ax1.set_ylabel("Temperature (°F)")
#Low plot
ax2 = fig.add_subplot(grid[0,1])
ax2.plot(date,low,  color = "blue")
ax2.set_title("Daily Low")
ax2.set_ylabel("Temperature (°F)")

#Combined High and Low plots
ax3 = fig.add_subplot(grid[1,:])
ax3.plot(date, high, color = "red")
ax3.plot(date , low , color = "blue")
ax3.set_title("Daily High vs Low")
ax3.set_ylabel("Temperature (°F)")

#Shading the combined graph
ax3.fill_between(date , high , low,facecolor ="green" , alpha = 0.3)

plt.subplots_adjust(hspace = 0.6)

for ax in [ax1, ax2, ax3]:
    ax.tick_params(axis='x', labelrotation=45)

plt.show()