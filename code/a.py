from hydrology.plot_hydrograph import subset_period
import datetime


dt = [datetime.datetime(2000,1,1),
      datetime.datetime(2000,1,2),
      datetime.datetime(2000,1,3)
      ]

var = [1,2,3]

print(subset_period(dt, var, 
                    begin_day=1, begin_month=1, 
                    end_day=1, end_month=1
                    ))