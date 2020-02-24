import datetime as datetime
import matplotlib.pyplot as plt
import pandas_datareader as pdr


start = datetime.datetime(2018,10,1)
end = datetime.datetime(2019, 10, 7)

dfcomp = pdr.DataReader(['AAPL', 'GE', 'GOOG', 'IBM', 'MSFT'],
                        'yahoo',start=start,end=end)['Adj Close']

retscomp = dfcomp.pct_change()
corr = retscomp.corr()

plt.scatter(retscomp.mean(), retscomp.std())
plt.xlabel('Expected returns')
plt.ylabel('Risk')

for label, x, y in zip(retscomp.columns, retscomp.mean(), retscomp.std()):

    plt.annotate(label,xy = (x, y),
                 xytext = (-20, 20),
                 textcoords = 'offset points', 
                 ha = 'right', va = 'bottom',
                 bbox = dict(boxstyle = 'round,pad=0.5',  alpha = 0.2),
                 arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))
