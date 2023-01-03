import pandas as pd
import datetime


def hyd_year(
        df: pd.DataFrame,
        hyd_year_begin_month: int = 11,
        hyd_year_begin_day: int = 1):
    """Add column "hyd_year" which contains the hydrological year
    based on the given begin. Defaults to the first of November (Germany).

    Args:
        df (pd.DataFrame): contains at least "date" as index
        hyd_year_begin_month (int, optional): number of month of a year.
            Defaults to 11.
        hyd_year_begin_day (int, optional): number of day of a month.
            Defaults to 1.

    Returns:
        pd.DataFrame: given input DataFrame with new column "hyd_year"
    """

    # Initialize hydrological year with calendric year.
    df["hyd_year"] = df.index.year

    # Increment the hydrological year if it starts before 1st of January.
    for i, row in df.iterrows():
        if i >= datetime.datetime(
                year=i.year,
                month=hyd_year_begin_month,
                day=hyd_year_begin_day):
            row["hyd_year"] += 1

    return df
