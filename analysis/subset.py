import pandas
import datetime


def subset_timeframe(df:pandas.DataFrame, 
                     date_start:datetime.datetime, 
                     date_end:datetime.datetime):
    """Returns a sub-DataFrame based on a start and end date (both included).

    Args:
        df (pd.DataFrame): contains at least "date" as index
        date_start (datetime.datetime): first date
        date_end (datetime.datetime): last date

    Returns:
        pd.DataFrame: sub-DataFrame with "date" as index
    """

    # Return sub lists of datetime.datetime objects and variable values between two dates (included).
    return df.loc[date_start:date_end]

def subset_period(df:pandas.DataFrame, months:list[int]=[1,2,3,4,5,6,7,8,9,10,11,12]):
    """Returns a sub-DataFrame based on given months.

    Args:
        df (pd.DataFrame): contains at least "date" as index
        months (list[int]): month index (e.g. 1 for January). 
                            Defaults to [1,2,3,4,5,6,7,8,9,10,11,12].

    Returns:
        pd.DataFrame: sub-DataFrame with "date" as index
    """
    df_sub = df.copy(deep=True)
    df_sub["month"] = df_sub.index
    df_sub["month"] = [int(x.month) for x in df_sub["month"].tolist()]
    df_sub = df_sub[df_sub["month"].isin(months)]
    df_sub = df_sub.drop(columns=["month"], axis=1)
    return df_sub