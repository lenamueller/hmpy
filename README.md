<img align="right" src="images/logo.svg" alt="logo" width="175"/>   

[![Repo status - in process](https://img.shields.io/static/v1?label=Repo+status&message=in+process&color=90EE90&style=for-the-badge)](https://)
[![Python - 3.10.8](https://img.shields.io/static/v1?label=Python&message=3.10.8&color=yellow&style=for-the-badge&logo=python)](https://)

An open source library for common hydrological and meteorological issues.

# Content
## analysis
### class `TimeSeries`
- `subset_timeframe`: subdivide time series based on a timeframe
- `subset_period`: subdivide time series based on a period
- `hyd_year`: add column "hyd_year" (hydrological year) based on a given start day and month
- `principal_values`: derive principal values (HHX, HX, MHX, MX, MNX, NX, NNX) from a time series
- extract partial series: TODO
- extract independent events: TODO

### class `NumericalList`
#### basic statistics
- `mean_arithmetic`, `mean_geometric`, `mean_exponential`, `mean_harmonic`, `mean_median`: means
- `mode`: mode
- `stdev`: (un-) biased standard deviation
- `variance`: (un-) biased variance
- `skewness`: (un-) biased skewness)
- kurtosis: TODO


#### distributions
- calculate empirical distribution: TODO
- fitting theoretical distribution: TODO
### class `MultiNumericalList`
- covariance: TODO
- correlation: TODO

## cleaning
- consistency: data gaps, missing values, duplicate: TODO
- homogenity: TODO
- precipitation correction after Richter: TODO
 
## visualization
- plot empirical and theoretical distribution: TODO
- plot hydrograph: TODO
- plot summation curve: TODO
- plot duration curve: TODO
- plot wind rose: TODO
- plot atmospheric sounding: TODO