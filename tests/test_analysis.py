import pandas as pd 
import pytest 
import datetime
import sys 
import statistics
from pandas.testing import assert_frame_equal

sys.path.insert(1, 'analysis')
print(sys.path)
from subset import subset_period, subset_timeframe
from principal_values import principal_values
from hyd_year import hyd_year
from basicstatistics import BasicStatistics


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

def test_hyd_year():
       df = pd.DataFrame({
              "date":[datetime.datetime(1999,12,1), 
                     datetime.datetime(2000,1,2), 
                     datetime.datetime(2001,1,1), 
                     datetime.datetime(2001,1,2),
                     datetime.datetime(2001,3,3),
                     datetime.datetime(2010,1,2)],
              "discharge":[1,2,3,4,5,6]
              })
       df = df.set_index("date")
       df_ref = pd.DataFrame({
              "date":[datetime.datetime(1999,12,1), 
                     datetime.datetime(2000,1,2), 
                     datetime.datetime(2001,1,1), 
                     datetime.datetime(2001,1,2),
                     datetime.datetime(2001,3,3),
                     datetime.datetime(2010,1,2)],
              "discharge":[1,2,3,4,5,6],
              "hyd_year": [2000,2000,2001,2001,2001,2010]
              })
       df_ref = df_ref.set_index("date")
       df_test = hyd_year(df, hyd_year_begin_month=11, hyd_year_begin_day=1)
       print(df_test)
       assert_frame_equal(df_test, df_ref)
       

def test_principal_values():
       
       df = pd.DataFrame({
              "date":[datetime.datetime(1999,12,1), 
                      datetime.datetime(2000,1,2), 
                      datetime.datetime(2001,1,1), 
                      datetime.datetime(2001,1,2),
                      datetime.datetime(2001,3,3),
                      datetime.datetime(2010,1,2)],
              "discharge":[1,2,3,4,5,6],
              "hyd_year" : [2000,2000,2001,2001,2001,2010]
              })
       df = df.set_index("date")
       
       tuple_ref = (6.0, 4.0, 3.0, 2.5, 2.0, 1.0, 1.0)
       tuple_test = principal_values(df=df, 
                                     varname="discharge", 
                                     aggr_col_name = "hyd_year",
                                     timeframe_begin=datetime.datetime(1999,1,1), 
                                     timeframe_end=datetime.datetime(2002,1,1),
                                     months=[12,1,2]
                                     )
       
       assert tuple_test == tuple_ref


def test_principal_values_2():
       
       df = pd.DataFrame({
              "date":[datetime.datetime(1999,12,1), 
                      datetime.datetime(2000,1,2), 
                      datetime.datetime(2001,1,1), 
                      datetime.datetime(2001,1,2),
                      datetime.datetime(2001,3,3),
                      datetime.datetime(2010,1,2)],
              "discharge":[1,2,3,4,5,6],
              "hyd_year" : [2000,2000,2001,2001,2001,2010]
              })
       df = df.set_index("date")
       
       tuple_ref = (6.0, 4.0, 2.33, 2.17, 2.0, 1.0, 1.0)
       tuple_test = principal_values(df=df, 
                                     varname="discharge", 
                                     aggr_col_name = "",
                                     timeframe_begin=datetime.datetime(1999,1,1), 
                                     timeframe_end=datetime.datetime(2002,1,1),
                                     months=[12,1,2]
                                     )
       
       assert tuple_test == tuple_ref
       


def test_mean_arithmetic():
       l = [1,2,3,4,5,6]
       bs = BasicStatistics(input=l)
       assert statistics.mean(l) == bs.mean_arithmetic()

def test_mean_geometric():
       l = [1,2,3,4,5,6]
       bs = BasicStatistics(input=l)
       assert statistics.geometric_mean(l) == bs.mean_geometric()
       
def test_mean_exponential():
       l = [1,2,3]
       bs = BasicStatistics(input=l)
       assert 2,1602 == round(bs.mean_exponential(m=2),4)

def test_mean_harmonic():
       l = [1,2,3,4,5,6]
       bs = BasicStatistics(input=l)
       assert statistics.harmonic_mean(l) == bs.mean_harmonic()

def test_mean_median_even():
       l = [1,2,3,4,5,6]
       bs = BasicStatistics(input=l)
       assert statistics.median(l) == bs.mean_median()

def test_mean_median_odd():
       l = [1,2,3,4,5]
       bs = BasicStatistics(input=l)
       assert statistics.median(l) == bs.mean_median()

def test_mode_single():
       bs = BasicStatistics(input=[1,3,3])
       assert [3] == bs.mode()
       
def test_mode_multiple():
       bs = BasicStatistics(input=[1,2,3])
       assert [1,2,3] == bs.mode()
       
def test_range():
       bs = BasicStatistics(input=[1,2,3])
       assert 2 == bs.range()

def test_stdev_biased():
       bs = BasicStatistics(input=[1,2,3])
       assert (2/3)**(1/2) == bs.stdev(biased=True)

def test_stdev_unbiased():
       bs = BasicStatistics(input=[1,2,3])
       assert 1/1 == round(bs.stdev(biased=False),4)

def test_var_biased():
       bs = BasicStatistics(input=[1,2,3])
       assert 2/3 == bs.var(biased=True)

def test_var_unbiased():
       bs = BasicStatistics(input=[1,2,3])
       assert 1/1 == bs.var(biased=False)

def test_skewness_biased():
       bs = BasicStatistics(input=[1,1,1,5])
       assert 1.1547 == round(bs.skewness(biased=True),4)

def test_skewness_unbiased():
       bs = BasicStatistics(input=[1,1,1,5])
       assert 3.0792 == round(bs.skewness(biased=False),4)