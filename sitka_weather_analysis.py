import matplotlib.pyplot as plt
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

fig , ax = plt.subplots(1,2,figsize= (10, 5))
ax[0].plot(date ,high , color = "red")

ax[0].set_title("Daily High")

ax[1].plot(date,high,  color = "blue")

ax[1].set_title("Daily Low")

plt.tight_layout()
fig.autofmt_xdate(rotation=45)
plt.show()