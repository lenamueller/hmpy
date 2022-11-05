import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd 
import datetime 
import proplot as pplt


def start_date(dt):
    """Get earliest datetime from a list of datetime.datetime objects."""
    try:
        return min(dt)
    except:
        raise ValueError("Empty list has no min().")

def end_date(dt):
    """Get latest datetime from a list of datetime.datetime objects."""
    try: 
        return max(dt)
    except:
        raise ValueError("Empty list has no max().")

def nb_days(dt):
    """Return number of given days from a list of datetime.datetime objects 
    and the number of days between the earliest and latest datetime.datetime object."""
    
    nb_days_given = len(dt)
    delta = end_date(dt) - start_date(dt)
    nb_days_true = int(delta.days) +1
    
    if nb_days_given != nb_days_true:
        print("Data contains {} days plus {} missing days".format(
            nb_days_given, nb_days_true-nb_days_given))
    
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
    
    missing_days = sorted(missing_days)
    diff_list = []
    
    start = missing_days[0]
    for i in np.arange(1, len(missing_days), 1):
        delta = missing_days[i]-missing_days[i-1]
        diff = delta.days
        if diff>1:
            diff_list.append((start,missing_days[i-1]))
            start = missing_days[i]            
    diff_list.append((start, missing_days[-1]))
    
    return diff_list

def plot(fn, dt, dc):
    """Plot the hydrograph with data gaps from a list of discharge values (float)
    in m^3/s and datetime.datetime objects"""
    
    _, ax = plt.subplots(ncols=1, nrows=1, figsize=(10,3))
    
    # plot data gaps
    miss = missing_dates(dt, create_datetime_list(start_date(dt), end_date(dt)))
    gaps = start_and_end_of_data_gaps(miss)
    for (begin, end) in gaps:
        ax.axvspan(begin,end, alpha=0.5, facecolor='red', label="data gap")
    
    # plot hydrograph
    plt.bar(dt, dc)
    
    plt.savefig(fn, dpi=800, bbox_inches="tight")
    return 0