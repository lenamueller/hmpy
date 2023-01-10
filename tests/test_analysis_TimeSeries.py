import pandas as pd
import datetime
from pandas.testing import assert_frame_equal

from flyingfish.timeseries import TimeSeries


def test_subset_timeframe():

    # create test df
    df = pd.DataFrame({
            "date": [
                datetime.datetime(2000, 1, 1),
                datetime.datetime(2000, 1, 2),
                datetime.datetime(2000, 1, 3),
                datetime.datetime(2000, 1, 4)],
            "discharge": [12, 13, 14, 15]
    }).set_index("date")
    ts = TimeSeries(df)
    test = ts.subset_timeframe(
            date_start=datetime.datetime(2000, 1, 2),
            date_end=datetime.datetime(2000, 1, 3))

    # create reference df
    df_ref = pd.DataFrame({
            "date": [
                datetime.datetime(2000, 1, 2),
                datetime.datetime(2000, 1, 3)],
            "discharge": [13, 14]
    }).set_index("date")

    assert_frame_equal(test.df, df_ref)


def test_subset_period():

    # create test df
    df = pd.DataFrame({
            "date": [
                datetime.datetime(2000, 1, 1),
                datetime.datetime(2000, 2, 1),
                datetime.datetime(2000, 3, 1)],
            "discharge": [12, 13, 14]
            }).set_index("date")

    ts = TimeSeries(df=df)
    test = ts.subset_period(months=[2, 3])

    # create reference df
    df_ref = pd.DataFrame({
            "date": [
                datetime.datetime(2000, 2, 1),
                datetime.datetime(2000, 3, 1)],
            "discharge": [13, 14]
            }).set_index("date")

    assert_frame_equal(test.df, df_ref)


def test_hyd_year():

    # create test df
    df = pd.DataFrame({
            "date": [
                datetime.datetime(1999, 12, 1),
                datetime.datetime(2000, 1, 2),
                datetime.datetime(2000, 12, 1)],
            "discharge": [1, 2, 3]
            }).set_index("date")

    ts = TimeSeries(df=df)
    test = ts.hyd_year(hyd_year_begin_month=11, hyd_year_begin_day=1)

    # create reference df
    df_ref = pd.DataFrame({
            "date": [
                datetime.datetime(1999, 12, 1),
                datetime.datetime(2000, 1, 2),
                datetime.datetime(2000, 12, 1),],
            "discharge": [1, 2, 3],
            "hyd_year": [2000, 2000, 2001]
            }).set_index("date")

    assert_frame_equal(test.df, df_ref)


def test_principal_values_given_aggr_col_name():

    # create test tuple
    df = pd.DataFrame({
            "date": [
                datetime.datetime(1999, 12, 1),
                datetime.datetime(2000, 1, 2),
                datetime.datetime(2001, 1, 1),
                datetime.datetime(2001, 1, 2),
                datetime.datetime(2001, 3, 3),
                datetime.datetime(2010, 1, 2)],
            "discharge": [1, 2, 3, 4, 5, 6],
            "hyd_year": [1999, 1999, 2001, 2000, 2000, 2009]
            }).set_index("date")

    ts = TimeSeries(df=df)
    tuple_test = ts.principal_values(
            date_start=datetime.datetime(1999, 1, 1),
            date_end=datetime.datetime(2002, 1, 1),
            varname="discharge",
            aggr_col_name="hyd_year",
            months=[12, 1, 2])

    # create reference tuple
    tuple_ref = (6.0, 4.0, 3.0, 2.83, 2.67, 1.0, 1.0)

    assert tuple_test == tuple_ref

def test_principal_values_no_given_aggr_col_name():

    # create test tuple
    df = pd.DataFrame({
            "date": [
                datetime.datetime(1999, 12, 1),
                datetime.datetime(2000, 1, 2),
                datetime.datetime(2001, 1, 1),
                datetime.datetime(2001, 1, 2),
                datetime.datetime(2001, 3, 3),
                datetime.datetime(2010, 1, 2)],
            "discharge": [1, 2, 3, 4, 5, 6],
            "hyd_year": [2000, 2000, 2001, 2001, 2001, 2010]
            }).set_index("date")

    ts = TimeSeries(df)
    tuple_test = ts.principal_values(
        date_start=datetime.datetime(1999, 1, 1),
        date_end=datetime.datetime(2002, 1, 1),
        varname="discharge",
        aggr_col_name="",
        months=[12, 1, 2])

    # create reference tuple
    tuple_ref = (6.0, 4.0, 2.33, 2.17, 2.0, 1.0, 1.0)

    assert tuple_test == tuple_ref


def test_duplicates():
    df = pd.DataFrame({
            "date": [
                datetime.datetime(1999, 12, 1),
                datetime.datetime(2000, 1, 1),
                datetime.datetime(2000, 1, 1)],
            "discharge": [1, 2, 3],
            "hyd_year": [2000, 2000, 2000]
            }).set_index("date")
    ts = TimeSeries(df)
    
    assert 1 == ts.duplicates()


def test_no_duplicates():
    df = pd.DataFrame({
            "date": [
                datetime.datetime(1999, 12, 1),
                datetime.datetime(2000, 1, 1),
                datetime.datetime(2001, 1, 1)],
            "discharge": [1, 2, 3]
            }).set_index("date")
    ts = TimeSeries(df)
    
    assert 0 == ts.duplicates()


def test_missing_days():
    df = pd.DataFrame({
            "date": [
                datetime.datetime(2000, 1, 1),
                datetime.datetime(2000, 1, 2),
                datetime.datetime(2000, 1, 4)],
            "discharge": [1, 2, 3]
            }).set_index("date")
    ts = TimeSeries(df)
    
    assert 1 == ts.missing_days()


def test_missing_days_2():
    df = pd.DataFrame({
            "date": [
                datetime.datetime(2000, 1, 1),
                datetime.datetime(2000, 1, 3),
                datetime.datetime(2000, 1, 5)],
            "discharge": [1, 2, 3]
            }).set_index("date")
    ts = TimeSeries(df)
    
    assert 2 == ts.missing_days()
