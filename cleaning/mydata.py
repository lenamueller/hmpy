import numpy as np
import pandas as pd


class MyTimeSeries:
    """
    A class to represent time series data. 
    
    Attributes
    ----------
    data: pd.DataFrame
        data (main object to analyse and visualize)
    status: str
        If status is raw, the data needs cleaning. 
        If status is ready, analysis methods can be applied.
        
    Merthods
    ----------
    get_status:
        Returns the status.
    set_status_ready:
        Sets the status to "ready".
    set_status_raw:
        Sets the status to "raw".
    """
    
    def __init__(self, data:pd.DataFrame):
        
        self.data:pd.DataFrame = data
        self.status:str = "raw"
    
    def get_status(self):
        return self.status 
    
    def set_status_ready(self):
        self.status = "ready"
        return 0
    
    def set_status_raw(self):
        self.status = "raw"
        return 0

    
class MyTimeStamp:
    """
    A class to represent time stamp data (e.g. radar image).
    
    Attributes
    ----------
    data: np.array
        data (main object to analyse and visualize)
    status: str
        If status is raw, the data needs cleaning. 
        If status is ready, analysis methods can be applied.
        
    Merthods
    ----------
    get_status:
        Returns the status.
    set_status_ready:
        Sets the status to "ready".
    set_status_raw:
        Sets the status to "raw".
    """
    
    def __init__(self, data:np.array):
        
        self.data:np.array = data
        self.status:str = "raw"
        
    def get_status(self):
        return self.status 
    
    def set_status_ready(self):
        self.status = "ready"
        return 0
    
    def set_status_raw(self):
        self.status = "raw"
        return 0