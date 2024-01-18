# Candle Chart
# https://github.com/matplotlib/mplfinance/

import FinanceDataReader as fdr
import mplfinance as mpf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Define Function for Market data

def getData(code, start, end) :
    df = fdr.DataReader(code, start, end).drop(columns='Change')
    return df

# Marcap : 시가총액
def getSymbols(market='KOSPI', sort='Marcap') :
    df = fdr.StockListing(market)
    ascending = True
    if sort == 'Marcap' :
        ascending = False
    df.sort_values(by=sort, ascending=ascending, inplace=True)
    return df[['Code', 'Name', 'Market']]

code = '005930' 
#code = '373220'

start = (datetime.today() - timedelta(days=30)).date()
end = datetime.today().date()

df = getData(code, start, end)

# print chart

chart_style = 'classic'                     # 'default', 'binance', 'classic', 'yahoo'...
market_colors = mpf.make_marketcolors(up='red', down='blue')
mpf_style = mpf.make_mpf_style(base_mpf_style=chart_style, marketcolors=market_colors)

fig, ax = mpf.plot(
    data=df,
    volume=False,
    type='candle',
    style=mpf_style,
    figsize=(10, 7),
    fontscale=1.1,
    mav=(5, 10, 30),
    mavcolors=('red', 'green', 'blue'),
    returnfig=True
)

plt.show()
    



























