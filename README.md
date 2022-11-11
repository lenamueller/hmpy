[![Repo status - Active](https://img.shields.io/badge/Repo_status-Active-00aa00)](https://)
[![python - 3.10.1](https://img.shields.io/badge/python-3.10.1-ffe05c?logo=python&logoColor=4685b7)](https://)
[![field of application - meteorology, hydrology](https://img.shields.io/badge/field_of_application-meteorology%2C_hydrology-00aaff)](https://)

<img src="images/logo.svg" alt="logo" width="600"/>   

An open source library for common hydrological and meteorological issues.
# Content
  ## 1. cleaning: explorative data analysis and data correction
1.  EDA: structure investigation:
- [ ] format
- [ ] size
- [ ] data types: numerical (continuous, discrete) / categorical (binary,ordinal)
- [ ] scales
2. EDA: quality investigation:
- [ ] data gap (e.g. missing date or missing value)
- [ ] missing values (e.g. -999)
- [ ] duplicates
- [ ] homogenity test of time series
3. EDA: content investigation:
- [ ] frequency distribution
- [ ] correlation
- [ ] patterns
4. correction
- [ ] delete duplicates and irrelevant information
- [ ] At which levelof completness data rows or cols should be deleted?
- [ ] correction: mean, fit to periodogram, idw, kriging, inhomogenity
- [ ] precipitation correction after Richter

## 2. analysis
basic statistics
- [ ] mean, mode, median, stdev, range, variance, 
- [ ] empirical distribution
- [ ] parameters for fitting a theoretical distribution

hydrology
- [x] principal values
- [ ] partial series
- [ ] independent events
- [ ] summation curve
- [ ] duration curve

meteorology
- [ ] independent events

## 3. vizualization (reports, plots)
basic
- [ ] empirical and theoretical distribution

hydrology
- [x] hydroraph 
- [ ] hydrograph with precipitation at top axis
- [ ] partial series
- [x] summation curve
- [x] duration curve

meteorology
- [ ] atmospheric sounding
- [ ] wind rose

report
- [ ] write report
