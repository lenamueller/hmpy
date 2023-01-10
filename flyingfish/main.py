import pandas as pd 
import numpy as np

from flyingfish.timeseries import TimeSeries
from flyingfish.numericallist import NumericalList

# from example.parse import parse_data


fn_in = "example/data/nossen_1.txt"
fn_out = "example/data/nossen_1_converted.csv"
df = parse_data(fn_in, fn_out)
ts = TimeSeries(df=df)

diff = (ts.df.index[-1]-ts.df.index[0]).days

if diff+1 == len(ts.df):
    print("Horray")

print((pd.Timestamp(2000,1,2) - pd.Timestamp(2000,1,1)).days)
