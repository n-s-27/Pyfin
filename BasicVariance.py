import pandas as pd
import pandas_datareader.data as web
import pandas_datareader.wb as wb
import numpy as np

from datetime import datetime as dt


gold_prices = pd.read_csv('gold_prices.csv')
print(gold_prices)

crude_oil_prices = pd.read_csv('crude_oil_prices.csv')
print(crude_oil_prices)

start = dt(1999, 1, 1)
end = dt(2019, 1, 1)

nasdaq_data = web.DataReader('NASDAQ100', 'fred', start, end)

print(nasdaq_data)

sap_data = web.DataReader('SP500', 'fred', start, end)

print(sap_data)

gdp_data = wb.download(indicator='NY.GDP.MKTP.CD', country=['US'], start = start, end=end)

print(gdp_data)
export_data = wb.download(indicator='NE.EXP.GNFS.CN', country=['US'], start = start, end=end)

print(export_data)
# natural_log(current price/previous price)
def log_return(prices):
  return np.log(prices)

gold_returns = log_return(gold_prices['Gold_Price'])

crudeoil_returns = log_return(crude_oil_prices['Crude_Oil_Price'])

nasdaq_returns = log_return(nasdaq_data['NASDAQ100'])

sap_returns = log_return(sap_data['SP500'])

print('Gold: ', gold_returns.var())
print('Oil: ', crudeoil_returns.var())
print('S&P 500: ', sap_returns.var())
print('NASDAQ: ', nasdaq_returns.var())

