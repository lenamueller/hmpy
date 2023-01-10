import math 
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd 
import datetime 


def start_date(df:pd.DataFrame):
    """Get earliest datetime.

    Args:
        df (pd.DataFrame): contains at least the column "date"
                            with datetime.datetime objects

    Returns:
        datetime.datetime: earliest datetime
    """
    return min(df["date"].tolist())
    
def end_date(df:pd.DataFrame):
    """Returns latest datetime.

    Args:
        df (pd.DataFrame): contains at least the column "date"
                            with datetime.datetime objects

    Returns:
        datetime.datetime: latest datetime
    """
    return max(df["date"].tolist())

def timesteps_between_two_dates(date_start:datetime.datetime, 
                              date_end:datetime.datetime, 
                              res:int="days"):
    """Return the number of time steps between two days, start 
    and end date are including, based on a given temporal resolution.

    Args:
        date_start (datetime.datetime): start date (included)
        date_end (datetime.datetime): end date (included)
        res (int): temporal resolution from "days", "hours", "minutes". Defaults to "days". 

    Returns:
        int: number of time steps
    """
    delta:datetime.timedelta = date_end - date_start
    nb_days:int = delta.days +1

    match res:
        case "days":
            return nb_days
        case "hours":
            return nb_days*24
        case "minutes":
            return nb_days*24*60
        case _:
            sys.exit("""Arg. 'res' from function timesteps_between_two_dates 
                     only alows values 'days', 'hours', 'minutes'""")
        
def create_datetime_list(date_start:datetime.datetime, 
                         date_end:datetime.datetime, 
                         res:int="days"):
    """ 
    Returns a list of datetime.datetime objects from given start and end date.
    
    Args:
        date_start (datetime.datetime): start date (included)
        date_end (datetime.datetime): end date (included)
        res (int): temporal resolution from "days", "hours", "minutes". Defaults to "days". 
    
    Returns:
        list[datetime.datetime]: datetime.datetime objects
    
    """
    match res:
        case "days":
            date_list:list[datetime.datetime] = [
                date_start + datetime.timedelta(days=x) for x in range(0, (date_end-date_start).days+1)]
            return date_list
        case "hours":
            date_list:list[datetime.datetime] = [
                date_start + datetime.timedelta(hours=x) for x in range(0, (date_end-date_start).hours+1)]
            return date_list
        case "minutes":
            date_list:list[datetime.datetime] = [
                date_start + datetime.timedelta(minutes=x) for x in range(0, (date_end-date_start).minutes+1)]
            return date_list
        case _:
            sys.exit("""Arg. 'res' from function timesteps_between_two_dates 
                     only alows values 'days', 'hours', 'minutes'""")


def remove_nan_from_list(list):
    """Remove all np.Nan from a list."""
    return [x for x in list if x is not np.NaN]

def remove_inf_from_list(list):
    """Remove all np.Inf from a list."""
    return [x for x in list if x is not np.Inf]

def clean_nan_inf(list):
    """Remove all np.Nan and np.Inf from a list."""
    return remove_inf_from_list(remove_nan_from_list(list))

def clean_nan_inf_2_rows(list1, list2):    
    list1_new, list2_new = [], []
    for i in range(len(list1)):
        if list1[i] not in [np.NaN, np.Inf] and list2[i] not in [np.NaN, np.Inf]:
            list1_new.append(list1[i])
            list2_new.append(list2[i])
    return list1_new, list2_new
    
def start_date(dt):
    """Get earliest datetime from a list of datetime.datetime objects."""
    dt = clean_nan_inf(dt)
    if dt:
        return min(dt)
    else:
        raise ValueError("start_date argument dt is empty")

def end_date(dt):
    """Get latest datetime from a list of datetime.datetime objects."""
    dt = clean_nan_inf(dt)
    if dt: 
        return max(dt)
    else:
        raise ValueError("end_date argument dt is empty")

def nb_days(dt):
    """Return number of given days from a list of datetime.datetime objects 
    and the number of days between the earliest and latest datetime.datetime object."""
    
    dt = clean_nan_inf(dt)
    
    nb_days_given = len(dt)

    if nb_days_given==0:
        return 0,0
    else:
        delta = end_date(dt) - start_date(dt)
        nb_days_true = int(delta.days) +1
        return nb_days_given, nb_days_true

def create_datetime_list(start_date, end_date):
    """Return a list of datetime.datetime objects from given start and end 
    datetime.datetime object"""
    
    end_date += datetime.timedelta(days=1)
    
    return [start_date+datetime.timedelta(days=x) for x in range((end_date-start_date).days)]

def missing_dates(test_list, ref_list):
    """Return a list of datetime.datetime objects from ref_list which are 
    not found in the test_list"""
    return sorted(list(set(ref_list) - set(test_list)))

def start_and_end_of_data_gaps(missing_days):
    """Return a list of tuples with start and end datetime.datetime objects for data gaps
    defined as consecutive dates in a list. If the gap has the length 1, end equals start"""
    
    diff_list = []
    if missing_days != []:
        start = missing_days[0]
        for i in np.arange(1, len(missing_days), 1):
            delta = missing_days[i]-missing_days[i-1]
            diff = delta.days
            if diff>1:
                diff_list.append((start,missing_days[i-1]))
                start = missing_days[i]            
        diff_list.append((start, missing_days[-1]))
        
        return diff_list
    else:
        return []

def _cumulate(var):
    """Return cumulated time series."""
    # TODO: Should nan be replaced by zero?
    if np.inf in var:
        raise ValueError("List contains inf.")                
    else:
        if np.nan in var:
            var = [0 if math.isnan(x) else x for x in var]
        else:
            pass
        return np.cumsum(var)    
