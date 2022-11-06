import pytest 
import numpy as np
import datetime
import sys 

sys.path.insert(1, 'code/hydrology')
from plot_hydrograph import start_date, end_date, nb_days, _cumulate, create_datetime_list, missing_dates, start_and_end_of_data_gaps, subset_timeframe, subset_period, _list_of_doy_between_two_dates, principal_values


@pytest.fixture
def ds0():
   return []

@pytest.fixture
def ds1():
   return [datetime.datetime(2000,1,1)]

@pytest.fixture
def ds2():
   return [datetime.datetime(2000,1,2), 
           datetime.datetime(2000,1,1)]

@pytest.fixture
def ds3():
    return [datetime.datetime(2000,1,2), 
            datetime.datetime(2000,1,1), 
            datetime.datetime(2000,1,4)]
@pytest.fixture
def dsnan():
    return [datetime.datetime(2000,1,1), 
            datetime.datetime(2000,1,3),
            np.NaN]

@pytest.fixture
def dsinf():
    return [datetime.datetime(2000,1,1), 
            datetime.datetime(2000,1,3),
            np.inf]

# ---------------------------------------------------------

def test_start_date_1(ds0):
    with pytest.raises(ValueError):
        start_date(ds0)
    
def test_start_date_2(ds1):
    assert start_date(ds1) == datetime.datetime(2000,1,1)

def test_start_date_3(ds2):
    assert start_date(ds2) == datetime.datetime(2000,1,1)

def test_start_date_4(dsnan):
    assert start_date(dsnan) == datetime.datetime(2000,1,1)

def test_start_date_5(dsinf):
    assert start_date(dsinf) == datetime.datetime(2000,1,1)

# ---------------------------------------------------------

def test_end_date_1(ds0):
    with pytest.raises(ValueError):
        end_date(ds0)
    
def test_end_date_2(ds1):
    assert start_date(ds1) == datetime.datetime(2000,1,1)
    
def test_end_date_3(ds2):
    assert end_date(ds2) == datetime.datetime(2000,1,2)
    
def test_end_date_4(dsnan):
    assert start_date(dsnan) == datetime.datetime(2000,1,1)

def test_end_date_5(dsinf):
    assert start_date(dsinf) == datetime.datetime(2000,1,1)

# ---------------------------------------------------------

def test_nb_days_1(ds3):
    nb_given, nb_true = nb_days(ds3)
    assert (nb_given, nb_true) == (3,4)
    
def test_nb_days_2(dsnan):
    nb_given, nb_true = nb_days(dsnan)
    assert (nb_given, nb_true) == (2,3)
    
def test_nb_days_3(dsinf):
    nb_given, nb_true = nb_days(dsinf)
    assert (nb_given, nb_true) == (2,3)

def test_nb_days_4(ds1):
    nb_given, nb_true = nb_days(ds1)
    assert (nb_given, nb_true) == (1,1)

def test_nb_days_5(ds0):
    nb_given, nb_true = nb_days(ds0)
    assert (nb_given, nb_true) == (0,0)

# ---------------------------------------------------------

def test_create_datetime_list_1():
    test = create_datetime_list(datetime.datetime(2000,1,1), datetime.datetime(2000,1,1))
    assert test == [datetime.datetime(2000,1,1)]

def test_create_datetime_list_2():
    test = create_datetime_list(datetime.datetime(2000,1,1), datetime.datetime(2000,1,2))
    assert test == [datetime.datetime(2000,1,1), datetime.datetime(2000,1,2)]

def test_create_datetime_list_3():
    test = create_datetime_list(datetime.datetime(2000,1,2), datetime.datetime(2000,1,1))
    assert test == []

# ---------------------------------------------------------

def test_missing_dates_1():
    complete = [datetime.datetime(2000,1,1), datetime.datetime(2000,1,2)]
    incomplete = [datetime.datetime(2000,1,1)]
    miss = missing_dates(incomplete, complete)
    assert miss == [datetime.datetime(2000,1,2)]

def test_missing_dates_2():
    complete = [datetime.datetime(2000,1,1), datetime.datetime(2000,1,2)]
    incomplete = []
    miss = missing_dates(incomplete, complete)
    assert miss == complete

def test_missing_dates_3():
    complete = [datetime.datetime(2000,1,1)]
    incomplete = [datetime.datetime(2000,1,1), datetime.datetime(2000,1,2)]
    miss = missing_dates(incomplete, complete)
    assert miss == []
    
# ---------------------------------------------------------

def test_start_and_end_of_data_gaps_1():
    missing_days = [datetime.datetime(2000,1,1), 
                    datetime.datetime(2000,1,2),
                    datetime.datetime(2000,1,3),
                    datetime.datetime(2000,1,5)]
    test = start_and_end_of_data_gaps(missing_days)
    ref = [(datetime.datetime(2000,1,1), datetime.datetime(2000,1,3)),
           (datetime.datetime(2000,1,5),datetime.datetime(2000,1,5))
           ]
    assert test == ref

def test_start_and_end_of_data_gaps_2():
    missing_days = [datetime.datetime(2000,1,1)]
    test = start_and_end_of_data_gaps(missing_days)
    ref = [(datetime.datetime(2000,1,1), datetime.datetime(2000,1,1))]
    assert test == ref

def test_start_and_end_of_data_gaps_3():
    missing_days = []
    test = start_and_end_of_data_gaps(missing_days)
    assert test == []
        
# ---------------------------------------------------------

def test_cumulate_1():
    test_list = _cumulate([1,2,3])
    ref_list = [1,3,6]
    assert len(test_list) == len(ref_list)
    assert all([a == b for a, b in zip(test_list, ref_list)])
        
def test_cumulate_2():
    with pytest.raises(ValueError):
        _cumulate([1,np.inf,3])
    
def test_cumulate_3():
    test_list = _cumulate([1,np.nan,3])
    ref_list = [1,1,4]
    assert len(test_list) == len(ref_list)
    assert all([a == b for a, b in zip(test_list, ref_list)])

# ---------------------------------------------------------

def test_subset_timeframe_1():
    dt = [datetime.datetime(2000,1,1), 
          datetime.datetime(2000,1,2),
          datetime.datetime(2000,1,3),
          datetime.datetime(2000,1,4),
          datetime.datetime(2000,1,5)
          ]
    var = [1,2,3,4,5]
    
    first_date = datetime.datetime(2000,1,2)
    last_date = datetime.datetime(2000,1,4)
    dt_test, var_test = subset_timeframe(dt, var, first_date, last_date)
    dt_ref = [datetime.datetime(2000,1,2),
              datetime.datetime(2000,1,3),
              datetime.datetime(2000,1,4)]
    var_ref = [2,3,4]
    assert dt_test == dt_ref
    assert var_test == var_ref

def test_subset_timeframe_2():
    dt = [datetime.datetime(2000,1,1), 
          datetime.datetime(2000,1,2)
          ]
    var = [1,2]
    
    first_date = datetime.datetime(2000,1,10)
    last_date = datetime.datetime(2000,1,11)
    dt_test, var_test = subset_timeframe(dt, var, first_date, last_date)
    assert dt_test == []
    assert var_test == []

def test_subset_timeframe_3():
    dt = [datetime.datetime(2000,1,1), 
          datetime.datetime(2000,1,2),
          datetime.datetime(2000,1,3)
          ]
    var = [1,2,3]
    
    first_date = datetime.datetime(2000,1,3)
    last_date = datetime.datetime(2000,1,2)
    dt_test, var_test = subset_timeframe(dt, var, first_date, last_date)
    assert dt_test == []
    assert var_test == []

def test_subset_timeframe_4():
    dt = [datetime.datetime(2000,1,1), 
          datetime.datetime(2000,1,2),
          datetime.datetime(2000,1,3)
          ]
    var = [1,2,3]
    
    first_date = datetime.datetime(2000,1,2)
    last_date = datetime.datetime(2000,1,2)
    dt_test, var_test = subset_timeframe(dt, var, first_date, last_date)
    assert dt_test == [datetime.datetime(2000,1,2)]
    assert var_test == [2]

def test_subset_timeframe_5():
    dt = [datetime.datetime(2000,1,1), 
          np.NaN,
          datetime.datetime(2000,1,3),
          np.Inf
          ]
    var = [1,2,np.NaN,4]
    
    first_date = datetime.datetime(2000,1,1)
    last_date = datetime.datetime(2000,1,3)
    dt_test, var_test = subset_timeframe(dt, var, first_date, last_date)
    assert dt_test == [datetime.datetime(2000,1,1)]
    assert var_test == [1]
    
# ---------------------------------------------------------
@pytest.mark.skip(reason="todo")
def test_subset_period_1():
    pass

# ---------------------------------------------------------
@pytest.mark.skip(reason="todo")
def test_list_of_doy_between_two_dates():
    _list_of_doy_between_two_dates()
    pass 

# ---------------------------------------------------------
@pytest.mark.skip(reason="todo")
def test_principal_values_1():
    principal_values()
    pass