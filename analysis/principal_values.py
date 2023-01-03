import numpy as np
import pandas as pd
import datetime

from subset import subset_period, subset_timeframe


def principal_values(
        df: pd.DataFrame,
        timeframe_begin: datetime.datetime,
        timeframe_end: datetime.datetime,
        varname: str,
        aggr_col_name: str = "",
        months: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]):
    """Returns principal values HHX, HX, MHX, MX, MNX, NX, NNX
    for a given column name "varname" aggregated by column
    "aggr_col_name" and restricted by a given timeframe and period.

    HHX: highest value ever observed
    HX: highest value within timeframe and months
    MHX: mean of the highest value of each year
    MX: mean of the mean value of each year
    MNX: mean of the lowest value of each year
    NX: lowest value within timeframe and months
    NNX: lowest value ever observed

    Args:
        df (pd.DataFrame): contains at least "date" as index and
            <varname> as variable
        varname (str): column name to derive principle values
            (e.g. "discharge")
        aggr_col_name (str): column name for aggregation
            (e.g. "hyd_year" derived from function hyd_year)
        timeframe_begin (datetime.datetime): first day of time series
        timeframe_end (datetime.datetime): last day of time series
        months (list[int], optional): month index.
            Defaults to [1,2,3,4,5,6,7,8,9,10,11,12].

    Returns:
        float, float, float, float, float: values representing
            HHX, HX, MX, NX, NNX
    """
    # Derive highest and lowest value ever observed
    hhx = np.round(np.max(df[varname]), 2)
    nnx = np.round(np.min(df[varname]), 2)

    # Limit data to timeframe and month
    df = subset_timeframe(
        df, date_start=timeframe_begin, date_end=timeframe_end)
    df = subset_period(df, months=months)

    # Use year from index to aggregate if no other aggregation
    # column name is given.
    if aggr_col_name == "":
        df["year"] = df.index.year
        aggr_col_name = "year"

    df_max = df.groupby([aggr_col_name]).max()
    df_min = df.groupby([aggr_col_name]).min()
    df_mean = df.groupby([aggr_col_name]).mean()

    # Calculate other principal values
    hx = np.round(np.max(df[varname]), 2)
    mhx = df_max[varname].mean().__round__(2)
    mx = df_mean[varname].mean().__round__(2)
    mnx = df_min[varname].mean().__round__(2)
    nx = np.round(np.min(df[varname]), 2)

    return hhx, hx, mhx, mx, mnx, nx, nnx
