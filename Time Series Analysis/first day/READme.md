Why Time Series Ananlysis?
i. You have just one variable - Time
ii. You can analse time series data in order to extract meaningful statistics and other characteristics.

What is TIme Series?
i. A time series is a set of observation taken at specified times usually at equal intervals(a day, a week, a year, etc).
ii. It is used to predict the future values based on the previous observed values.

Importance of Time Series:
i. Business Forecasting
ii. Understand past behaviour
iii. Plan for the future
iv. Evaluate current accomplishment

Components of Time Series:
i. Trend:
    a movement to relatively higher or lower values over a long period of time. When the time series analysis shows a general pattern that is up firt, we call it an uptrend and also it the rend exhibits a lower pattern that is down we call it a downtrend and if there is no trend we call it a horizontal trend.
    Trend is something that happens for some time then disappears
ii. Seasonality:
    is basically the upward or downward swings of a repeating pattern within a fixed time period eg. Christmas
iii. Irregularity:
    also called noise. These are erratic in nature or unsystematic. It's also called residual and this happens basically for short duration and it's non repeating. eg. when COVID struck and the price/worth of nose masks increased
iv. Cyclic:
    it's basically repeating up and down movements so this means you can go over more than a year. They don't have a fixed pattern so they can happen anythime let's say in two years, then fourth year then maybe in six months. So they keep on repeating and they are much harder to predict now.

When Not to Use Time Series Analysis?
i. When values are constant
ii. When values are in the form of functions

What is Stationarity?
It has a particular behaviour over time, there is a very high probability that it will follow the same in the future. Time series requires the reader to be stationary so any kind of statistical model that will apply on time series the data should be stationary.
Necessities:
    i. constant mean
    ii. constant variance
    iii. autocovariance that does not depend on time

Tests to Check Stationarity
i. Rolling Statistics
    Plot the moving average or moving variance and see if it varies with time. MOre of a visual technique.
ii. ADCF test
    Null hypothesis is that the TS is non-stationary. The test results comprise of a Test Statistic and some Critical values.

What is ARIMA Model?
AR + MA 
where AR = Auto Regressive (correlation between the previous time period and the current time period)
      MA = Moving Average ()

AR I MA => AR --> P = authoregressive lags
            I --> d = order of diffrentiation (INTEGRATION)
           MA --> Q = moving average

    