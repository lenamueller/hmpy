import pandas
import datetime
from enum import Enum
import numpy as np


class Status(Enum):
    RAW = 0
    READY = 1


class TimeSeries:

    def __init__(
            self,
            df: pandas.DataFrame,
            status: Status = Status.RAW):
        """Constructor

        Args:
            df (pandas.DataFrame): contains at least "date" as index
            status (Status, optional): Status of the NumericalList,
                which can be set or turned to Status.READY, if the
                data is been cleaned. Defaults to Status.RAW.
        """
        self.df: pandas.DataFrame = df
        self.status: Status = status

    def subset_timeframe(
            self,
            date_start: datetime.datetime,
            date_end: datetime.datetime):
        """Returns a sub-DataFrame based on a start and end date
        (both included).

        Args:
            date_start (datetime.datetime): first date
            date_end (datetime.datetime): last date

        Returns:
            pd.DataFrame: sub-DataFrame with "date" as index
        """
        return self.df.loc[date_start:date_end]

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
        self.df["month"] = self.df.index
        self.df["month"] = [int(x.month) for x in self.df["month"].tolist()]
        self.df = self.df[self.df["month"].isin(months)]
        self.df = self.df.drop(columns=["month"], axis=1)
        return self.df

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

        # Initialize hydrological year with calendric year.
        self.df["hyd_year"] = self.df.index.year

        # Increment the hydrological year if it starts before 1st of January.
        for i, row in self.df.iterrows():
            if i >= datetime.datetime(
                    year=i.year,
                    month=hyd_year_begin_month,
                    day=hyd_year_begin_day):
                row["hyd_year"] += 1

        return self.df

    def principal_values(
            self,
            date_start: datetime.datetime,
            date_end: datetime.datetime,
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

        # Derive highest and lowest value ever observed
        hhx = np.round(np.max(self.df[varname]), 2)
        nnx = np.round(np.min(self.df[varname]), 2)

        # Limit data to timeframe and month
        self.df = self.subset_timeframe(date_start, date_end)
        self.df = self.subset_period(months)

        # Use year from index to aggregate if no other aggregation
        # column name is given.
        if aggr_col_name == "":
            aggr_col_name = "year"
            self.df[aggr_col_name] = self.df.index.year
            

        df_max = self.df.groupby([aggr_col_name]).max()
        df_min = self.df.groupby([aggr_col_name]).min()
        df_mean = self.df.groupby([aggr_col_name]).mean()

        # Calculate other principal values
        hx = np.round(np.max(self.df[varname]), 2)
        mhx = df_max[varname].mean().__round__(2)
        mx = df_mean[varname].mean().__round__(2)
        mnx = df_min[varname].mean().__round__(2)
        nx = np.round(np.min(self.df[varname]), 2)

        return hhx, hx, mhx, mx, mnx, nx, nnx
