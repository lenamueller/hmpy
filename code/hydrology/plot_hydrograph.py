import math 
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd 
import datetime 


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

def subset_timeframe(dt,var, first_date, last_date):
    """Return sub lists of datetime.datetime objects and variable values 
     between two dates (included). """
    
    dt, var = clean_nan_inf_2_rows(dt, var)
    df = pd.DataFrame(list(zip(dt, var)), columns =['date', 'var'])
    
    after_start_date = df["date"] >= first_date
    before_end_date = df["date"] <= last_date
    df_sub = df.loc[after_start_date & before_end_date]
    
    dt_sub = df_sub["date"].tolist()
    var_sub = df_sub["var"].tolist()
    
    return dt_sub, var_sub

def subset_period(dt, var, begin_day=1, begin_month=1 , end_day=31, end_month=12):
    """Return subsets of the input lists dt (datetime.datetime objects) and var 
    (float values) which fit the period definied by period_begin and period_end."""

    assert begin_month <= end_month, "subset_period: period_end_month musst be larger than period_begin_month"
    assert begin_day <= end_day, "subset_period: period_end_day musst be larger than period_begin_day"
    
    dt_sub, var_sub = [], []
    for i in range(len(dt)):
        dt_i = dt[i]
        var_i = var[i]
        year = dt_i.year
        
        begin = datetime.datetime(year, begin_month, begin_day)
        end = datetime.datetime(year, end_month, end_day)
        if begin <= dt_i <= end:
            dt_sub.append(dt_i)
            var_sub.append(var_i)
            
    return dt_sub, var_sub

def principal_values(dt, var, period_begin, period_end, timeframe_begin, timeframe_end):
    """Return principal values of a variable (e.g. discharge) based
    on a time frame and period (datetime.datetime objects).
    e.g. period from 1.11. bis 30.11. and timeframe 2000 - 2020 returns principial 
    values for all novembers between 2000 and 2020"""
    
    assert len(dt) == len(var), "principal_values args have different lenghts"
    
    dt, va = subset_timeframe(dt, va, timeframe_begin, timeframe_end)
    dt, va = subset_period(dt, va, period_begin, period_end) # todo
    year = [int(date_i.year) for date_i in dt]
    
    df = pd.DataFrame(list(zip(year, va)), columns =['year', 'va'])
    df_max = df.loc[df.groupby("year")["va"].idxmax()]
    df_min = df.loc[df.groupby("year")["va"].idxmin()]
        
    hhx = np.round(max(va),2)
    hx = df_max["va"].mean().__round__(2)
    mx = np.round(np.mean(va),2)
    nx = df_min["va"].mean().__round__(2)
    nnx = np.round(min(va),2)
    
    return hhx, hx, mx, nx, nnx

def plot_hydrograph(fn, dt, var):
    """Plot the hydrograph with data gaps from a list of float values (e.g. discharge
    in m^3/s and a list of datetime.datetime objects"""
    
    assert len(dt) == len(var), "plot_hydrograph args dt and var have different lenghts"
    
    fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(10,3))
    
    # plot data gaps
    miss = missing_dates(dt, create_datetime_list(start_date(dt), end_date(dt)))
    if miss != []:
        gaps = start_and_end_of_data_gaps(miss)
        for (begin, end) in gaps:
            ax.axvspan(begin,end, alpha=0.5, facecolor='red', label="data gap")
    
    # plot hydrograph
    plt.bar(dt, var)
    plt.savefig(fn, dpi=800, bbox_inches="tight")
    plt.close()
    
    return fig

def plot_summation_curve(fn, dt, var):
    """Plot the summation curve with data gaps from a list of float values (e.g. 
    discharge in m^3/s) and a list of datetime.datetime objects. """
    
    assert len(dt) == len(var), "plot_summation_curve args dt and var have different lenghts"
    
    fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(10,3))
    
    # plot data gaps
    miss = missing_dates(dt, create_datetime_list(start_date(dt), end_date(dt)))
    if miss != []:
        gaps = start_and_end_of_data_gaps(miss)
        for (begin, end) in gaps:
            ax.axvspan(begin,end, alpha=0.5, facecolor='red', label="data gap")
        
    # plot hydrograph
    plt.bar(dt, _cumulate(var))
    plt.savefig(fn, dpi=800, bbox_inches="tight")
    plt.close()
    
    return fig

def plot_duration_curve(fn, dt, var, year, descending):
    """Plot the duration curve for a given year."""
    
    assert len(dt) == len(var), "plot_duration_curve args dt and var have different lenghts"

    fig, var_sub = subset_timeframe(dt, var, 
                                      first_date=datetime.datetime(year, 1, 1), 
                                      last_date=datetime.datetime(year, 12, 31)
                                      )
    
    plt.subplots(ncols=1, nrows=1, figsize=(10,3))
    plt.bar(np.arange(1, 366, 1), sorted(var_sub, reverse=descending))
    plt.savefig(fn, dpi=800, bbox_inches="tight")
    plt.close()
    
    return fig