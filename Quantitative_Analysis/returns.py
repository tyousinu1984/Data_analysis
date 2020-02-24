import numpy as np
import pandas as pd
import datetime as datetime
import matplotlib.pyplot as plt
import pandas_datareader as pdr

start = datetime.datetime(2018,10, 1)
end = datetime.datetime(2019, 10, 4)

df = pdr.DataReader('BABA', 'yahoo', start, end)
df.index = pd.to_datetime(df.index)

df['Returns']=df['Adj Close'].pct_change()
df['Returns'].fillna(value=0, inplace=True)

df['Returns'].plot()
plt.show()
mean_return_daily=np.mean(df['Returns'])
print("日平均收益:{return_daily:f}%".format( return_daily=mean_return_daily*100))
#day =len(df.index)
day = 252

mean_return_annualized = ((1+mean_return_daily)**day)-1
print("平均年化收益:{return_daily:f}%".format( return_daily=mean_return_annualized*100))
