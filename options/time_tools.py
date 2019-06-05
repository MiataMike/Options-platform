from alpha_vantage.timeseries import TimeSeries
import math

trading_days = 260
apikey = 'HB012PXU24EQA3JL'
apikey = 'DONT1C40C86U80WO'

ts = TimeSeries(key=apikey,output_format='pandas', indexing_type='date')

def hist_vol(ticker, days):
    daily_data = ts.get_daily(symbol=ticker, outputsize='compact')
    close_prices = daily_data[0]['4. close']

    #build returns
    daily_returns = []
    samples = len(close_prices)
    start = 0
    start = samples - days
    total = 0
    for i in range(start,samples-1):
        day_return =  math.log(close_prices[i+1]/close_prices[i])
        daily_returns.append(day_return)
        total += day_return
    average = total / (len(daily_returns))
    sum_sq_dev = 0
    for gain in daily_returns:
        sum_sq_dev += ((gain - average)) ** 2
    variance = sum_sq_dev / len(daily_returns)
    return math.sqrt(variance)*math.sqrt(trading_days)

