import pytest 

import numpy as np
import datetime
import sys 

sys.path.insert(1, 'code/hydrology')
from plot_hydrograph import start_date, end_date


@pytest.fixture
def ds0():
   return []

@pytest.fixture
def ds1():
   return [datetime.datetime(2000,1,1)]

@pytest.fixture
def ds2():
   return [datetime.datetime(2000,1,2), datetime.datetime(2000,1,1)]

@pytest.fixture
def dsnan():
    return [datetime.datetime(2000,1,1), np.NaN]

@pytest.fixture
def dsinf():
    return [datetime.datetime(2000,1,1), np.inf]

def test_start_date_1(ds0):
    with pytest.raises(ValueError):
        start_date(ds0)
    
def test_start_date_2(ds1):
    assert start_date(ds1) == datetime.datetime(2000,1,1)

def test_start_date_3(ds2):
    assert start_date(ds2) == datetime.datetime(2000,1,1)

def test_start_date_4(dsnan):
    with pytest.raises(ValueError):
        start_date(dsnan)

def test_start_date_5(dsinf):
    with pytest.raises(ValueError):
        start_date(dsinf)
        
def test_end_date_1(ds0):
    with pytest.raises(ValueError):
        end_date(ds0)
    
def test_end_date_2(ds1):
    assert start_date(ds1) == datetime.datetime(2000,1,1)
    
def test_end_date_3(ds2):
    assert end_date(ds2) == datetime.datetime(2000,1,2)
    
def test_end_date_4(dsnan):
    with pytest.raises(ValueError):
        end_date(dsnan)

def test_end_date_5(dsinf):
    with pytest.raises(ValueError):
        end_date(dsinf)