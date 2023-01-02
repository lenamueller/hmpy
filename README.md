<img align="right" src="images/logo.svg" alt="logo" width="175"/>   

[![Repo status - in process](https://img.shields.io/static/v1?label=Repo+status&message=in+process&color=90EE90&style=for-the-badge)](https://)
[![Python - 3.10.8](https://img.shields.io/static/v1?label=Python&message=3.10.8&color=yellow&style=for-the-badge&logo=python)](https://)

An open source library for common hydrological and meteorological issues.

# Implemented, test covered functions

## analysis
### general
- `subset_timeframe`: subdivide time series based on a timeframe
- `subset_period`: subdivide time series based on a period
- class `BasicStatistics`: calculation of means (`mean_arithmetic`, `mean_geometric`, `mean_exponential`, `mean_harmonic`, `mean_median`) and mode (`mode`), (biased/ unbiased) standard deviation (`stdev`), (biased/ unbiased) variance (`variance`), (biased/ unbiased) skewness (`skewness`)

### hydrology
- `hyd_year`: add column "hyd_year" (hydrological year) based on a given start day and month
- `principal_values`: derive principal values (HHX, HX, MHX, MX, MNX, NX, NNX) from a time series

### meteorology


## cleaning
## visualization
