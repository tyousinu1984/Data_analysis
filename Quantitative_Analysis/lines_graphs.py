import talib
import numpy as np
import pandas as pd
import datetime as datetime
import matplotlib.pyplot as plt
import mpl_finance as mpf
import pandas_datareader as pdr

start = datetime.datetime(2018,10,1)
end = datetime.datetime(2019, 10,11)

#yahooから株のデータを読み込み
df = pdr.DataReader('7729.T', 'yahoo', start, end)

df.index = pd.to_datetime(df.index)

#移動平均線の計算
closed = np.array(df['Close'])

sma_5 = talib.SMA(closed,5)
#sma_10 = talib.SMA(closed, 10)
sma_20 = talib.SMA(closed, 20)
#sma_30 = talib.SMA(closed, 30)
sma_60 = talib.SMA(closed, 60)

#ストキャスティクス
df['K'], df['D'] = talib.STOCH(df['High'], df['Low'], df['Close'])
df['J']= 3*df['D']-2*df['K']
#df['K'].fillna(value=0, inplace=True)
#df['D'].fillna(value=0, inplace=True)



fig = plt.figure(figsize=(30,15))
ax = fig.add_axes([0,0.40,1,0.3])
ax2 = fig.add_axes([0,0.2,1,0.2])
ax3 = fig.add_axes([0,0,1,0.2])
#ローソク足チャート
mpf.candlestick2_ochl(ax, df['Open'], df['Close'], df['High'],
                      df['Low'], width=0.6, colorup='r', colordown='g', alpha=0.5)

ax.set_xticks(range(0, len(df.index), 5))
#ax.plot(closed,color = 'darkred')
ax.plot(sma_5, label='5 line',color = 'black')
#ax.plot(sma_10, label='10 line')
ax.plot(sma_20, label='20 line',color ='deepskyblue')
#ax.plot(sma_30, label='30 line')
ax.plot(sma_60, label='60 line',color = 'darkgoldenrod')
ax.grid(True)

ax2.set_xticks(range(0, len(df.index), 5))
ax2.plot(df['K'], label='K',color = 'black')
ax2.plot(df['D'], label='D',color = 'blue')
ax2.plot(df['J'],label='J',color = 'red')
ax2.set_xticklabels(df.index[::5])

ax2.grid(True)


mpf.volume_overlay(ax3, df['Open'], df['Close'], df['Volume'],
                   colorup='r', colordown='g', width=0.5, alpha=0.8)
ax3.set_xticks(range(0, len(df.index), 5))
ax3.set_xticklabels(df.index[::5].strftime('%Y-%m-%d'), rotation=30)
ax3.grid(True)

ax.legend();
ax2.legend();

plt.show()
