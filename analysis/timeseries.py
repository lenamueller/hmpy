import collections
import matplotlib.pyplot as plt
import pandas as pd
from enum import Enum
import numpy as np


class Status(Enum):
    RAW = 0
    READY = 1


class TimeSeries:

    def __init__(
            self,
            df: pd.DataFrame,
            status: Status = Status.RAW):
        """Constructor

        Args:
            df (pd.DataFrame): contains at least "date" as index
            status (Status, optional): Status of the NumericalList,
                which can be set or turned to Status.READY, if the
                data is been cleaned. Defaults to Status.RAW.
        """
        self.df: pd.DataFrame = df
        self.status: Status = status

    def subset_timeframe(
            self,
            date_start: pd.Timestamp,
            date_end: pd.Timestamp):
        """Returns a sub-DataFrame based on a start and end date
        (both included).

        Args:
            date_start (datetime.datetime): first date
            date_end (datetime.datetime): last date

        Returns:
            pd.DataFrame: sub-DataFrame with "date" as index
        """
        df_sub = self.df.loc[date_start:date_end]
        return TimeSeries(df_sub)

    def subset_period(
            self,
            months: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]):
        """Returns a sub-DataFrame based on given months.

        Args:
            months (list[int]): month index (e.g. 1 for January).
                Defaults to [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12].

        Returns:
            pd.DataFrame: sub-DataFrame with "date" as index
        """
        df_sub = self.df.copy(deep=True)
        df_sub["month"] = df_sub.index
        df_sub["month"] = [int(x.month) for x in df_sub["month"].tolist()]
        df_sub = df_sub[df_sub["month"].isin(months)]
        df_sub = df_sub.drop(columns=["month"], axis=1)
        return TimeSeries(df_sub)

    def hyd_year(
            self,
            hyd_year_begin_month: int = 11,
            hyd_year_begin_day: int = 1):
        """Add column "hyd_year" which contains the hydrological year
        based on the given begin. Defaults to the first of November (Germany).

        Args:
            hyd_year_begin_month (int, optional): number of month of a year.
                Defaults to 11.
            hyd_year_begin_day (int, optional): number of day of a month.
                Defaults to 1.

        Returns:
            pd.DataFrame: given input DataFrame with new column "hyd_year"
        """
        df_copy = self.df.copy(deep=True)
        
        # Initialize hydrological year with calendric year.
        df_copy['hyd_year'] = df_copy.index.year
        
        # Increment the hydrological year if it starts before 1st of January.
        for index, _ in df_copy.iterrows():
            hyd_new_year = pd.Timestamp(
                year=index.year,
                month=hyd_year_begin_month,
                day=hyd_year_begin_day)
            
            if index >= hyd_new_year:
                df_copy.loc[index,"hyd_year"] = int(index.year + 1)
            else:
                df_copy.loc[index,"hyd_year"] = int(index.year)

        return TimeSeries(df_copy)

    def principal_values(
            self,
            date_start: pd.Timestamp,
            date_end: pd.Timestamp,
            varname: str,
            aggr_col_name: str = "",
            months: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]):
        # df (pd.DataFrame): contains at least "date" as index and
        # <varname> as variable
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
            date_start (datetime.datetime): first day of time series
            date_end (datetime.datetime): last day of time series
            months (list[int], optional): month index.
                Defaults to [1,2,3,4,5,6,7,8,9,10,11,12].
            varname (str): column name to derive principle values
                (e.g. "discharge")
            aggr_col_name (str): column name for aggregation
                (e.g. "hyd_year" derived from function hyd_year)

        Returns:
            float, float, float, float, float: values representing
                HHX, HX, MX, NX, NNX
        """

        # Create new TimeSeries instance
        df_copy = self.df.copy(deep=True)
        ts_new = TimeSeries(df=df_copy)
        
        # Derive highest and lowest value ever observed
        hhx = np.round(np.max(ts_new.df[varname]), 2)
        nnx = np.round(np.min(ts_new.df[varname]), 2)

        # limit data to timeframe and months
        ts_new = (ts_new.subset_timeframe(date_start, date_end)).subset_period(months)
        df_new = ts_new.df

        # Use year from index to aggregate if no other aggregation
        # column name is given.
        if aggr_col_name == "":
            aggr_col_name = "year"
            df_new[aggr_col_name] = df_new.index.year
            

        df_max = df_new.groupby([aggr_col_name]).max()
        df_min = df_new.groupby([aggr_col_name]).min()
        df_mean = df_new.groupby([aggr_col_name]).mean()

        # Calculate other principal values
        hx = np.round(np.max(df_new[varname]), 2)
        mhx = df_max[varname].mean().__round__(2)
        mx = df_mean[varname].mean().__round__(2)
        mnx = df_min[varname].mean().__round__(2)
        nx = np.round(np.min(df_new[varname]), 2)

        return hhx, hx, mhx, mx, mnx, nx, nnx

    def ausreisser(self):
        solving = "drop_outlier"
        match solving:
            case "drop_outlier":
                pass
            case "cap_outlier":
                pass
        return 0

    def duplicates(self):
        """Returns the number of duplicate dates [int]."""
        dates = list(self.df.index.values)
        n_duplicates = len([item for item, count in collections.Counter(dates).items() if count > 1])
        return n_duplicates

    def missing_days(self):
        """Returns the number of missing days [int]"""
        diff = (self.df.index[-1]-self.df.index[0]).days
        n_missing = (diff+1) - len(self.df)
        return n_missing
