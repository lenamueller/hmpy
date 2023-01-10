import matplotlib.pyplot as plt 


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