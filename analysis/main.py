import pandas as pd 
import numpy as np
import datetime 

from plot_hydrograph import plot

df = pd.read_csv('data/discharge_Friedrichstadt_19990101_20221028.csv', delimiter=',', usecols=["Datum", "Durchfluss"])
df["date"] = [datetime.datetime.strptime(x, "%d.%m.%Y") for x in df["Datum"]]
df["discharge"] = [float(val.replace(",", ".")) for val in df["Durchfluss"]]
dc = df["discharge"].tolist()
dt = df["date"].tolist()

plot("images/hydrograph.png", dt,dc)