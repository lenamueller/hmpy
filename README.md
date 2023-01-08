<img align="right" src="images/logo.svg" alt="logo" width="175"/>   

[![Repo status - in process](https://img.shields.io/static/v1?label=Repo+status&message=in+process&color=90EE90&style=for-the-badge)](https://)
[![contributions - welcome](https://img.shields.io/static/v1?label=contributions&message=welcome&color=90EE90&style=for-the-badge)](https://)
[![Python - 3.10.8](https://img.shields.io/static/v1?label=Python&message=3.10.8&color=yellow&style=for-the-badge&logo=python)](https://)
[![OS - Linux](https://img.shields.io/badge/OS-Linux-blue?style=for-the-badge&logo=linux&logoColor=white)](https://)
[![license - MIT](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge&)](https://lbesson.mit-license.org/)

An open source library for common hydrological and meteorological issues.

# Content
## analysis
### class `TimeSeries`
- `subset_timeframe`: subdivide time series based on a timeframe
- `subset_period`: subdivide time series based on a period
- `hyd_year`: add column "hyd_year" (hydrological year) based on a given start day and month
- `principal_values`: derive principal values (HHX, HX, MHX, MX, MNX, NX, NNX) from a time series
- extract partial series: TODO #5
- extract independent events: TODO #6

### class `NumericalList`
#### exploratory data analysis
- estimates of location: `arithmetic_mean`, `weighted_arithmetic_mean`, `trimmed_mean`,`geometric_mean`,`exponential_mean`,`harmonic_mean`,`median`,`weighted_median`,`percentile`
- estimate_of_variability: `mu`, `avg_absolute_deviation_from_mean`, `avg_absolute_deviation_from_median`, `median_absolute_deviaton`,`variance`, `stdev`, `range`, `iqr`
- estimates of distribution: `coefficient_of_skewness`, `coefficient_of_kurtosis` TODO #7, `mode`

#### data distributions
- calculate empirical distribution: TODO #8
- fitting theoretical distribution: TODO #4
#### Error statistics

### class `MultiNumericalList`
- covariance: TODO #9
- correlation: TODO #10


## cleaning
- consistency: data gaps, missing values, duplicate: TODO #12
- homogenity: TODO #13
- precipitation correction after Richter: TODO #14
 
## visualization
- plot hydrograph: TODO #15
- plot summation curve: TODO #16
- plot duration curve: TODO #17
- plot wind rose: TODO #18
- plot atmospheric sounding: TODO #19