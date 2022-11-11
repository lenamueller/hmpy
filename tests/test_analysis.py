import pandas as pd 
import pytest 
import datetime
import sys 
from pandas.testing import assert_frame_equal

sys.path.insert(1, 'analysis')
print(sys.path)
from subset import subset_period, subset_timeframe
from principal_values import principal_values


def test_subset_timeframe():
       df = pd.DataFrame({
              "date":[datetime.datetime(2000,1,1),
                     datetime.datetime(2000,1,2),
                     datetime.datetime(2000,1,3),
                     datetime.datetime(2000,1,4)],
              "discharge":[12,13,14,15]
       })
       df = df.set_index("date")
       df_ref = pd.DataFrame({
              "date":[datetime.datetime(2000,1,2),
                      datetime.datetime(2000,1,3)],
              "discharge":[13,14]
       })
       df_ref = df_ref.set_index("date")
       df_test = subset_timeframe(df, datetime.datetime(2000,1,2), datetime.datetime(2000,1,3))
       assert_frame_equal(df_test, df_ref)       


def test_subset_period():
       df = pd.DataFrame({
              "date":[datetime.datetime(2000,1,1), 
                      datetime.datetime(2000,2,1), 
                      datetime.datetime(2000,3,1)], 
              "discharge":[12,13,14]
              })
       df = df.set_index("date")
       df_ref = pd.DataFrame({
              "date":[datetime.datetime(2000,2,1), 
                      datetime.datetime(2000,3,1)], 
              "discharge":[13,14]
              })
       df_ref = df_ref.set_index("date")
       df_test = subset_period(df, [2,3])
       assert_frame_equal(df_test, df_ref)

def test_principal_values():
       
       df = pd.DataFrame({
              "date":[datetime.datetime(2000,1,1), 
                      datetime.datetime(2000,1,2), 
                      datetime.datetime(2001,1,1), 
                      datetime.datetime(2001,1,2),
                      datetime.datetime(2001,3,3),
                      datetime.datetime(2010,1,2)],
              "discharge":[1,2,3,4,5,6]
              })
       df = df.set_index("date")
       tuple_ref = (6.0, 4.0, 3.0, 2.5, 2.0, 1.0, 1.0)
       tuple_test = principal_values(df=df, 
                                     varname="discharge", 
                                     timeframe_begin=datetime.datetime(2000,1,1), 
                                     timeframe_end=datetime.datetime(2002,1,1),
                                     months=[1,2]
                                     )
       
       assert tuple_test == tuple_ref