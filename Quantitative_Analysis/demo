import datetime as datetime
import matplotlib.pyplot as plt
import pandas_datareader as pdr
import numpy as np
import seaborn as sns


def cumulative_returns_plot(name_list):
    for name in name_list:
        CumulativeReturns = ((1+StockReturns[name]).cumprod()-1)
        CumulativeReturns.plot(label=name)
    plt.legend()
    plt.show()

######################################################

start = datetime.datetime(2018,10,1)
end = datetime.datetime(2019, 10, 7)
companys=[
        'AAPL'
        ,'GE'
        ,'GOOG'
        ,'IBM'
        ,'MSFT'
           ]

portfolio_weights=np.array([0.2, 0.2, 0.2, 0.2,0.2])

dfcomp = pdr.DataReader(companys,'yahoo',start=start,end=end)['Adj Close']

StockReturns = dfcomp.pct_change()
stock_return = StockReturns.copy()

WeightedReturns = stock_return.mul(portfolio_weights, axis=1)

StockReturns['Portfolio'] = WeightedReturns.sum(axis=1)

# 绘制组合收益随时间变化的图
StockReturns.Portfolio.plot()
plt.grid()
plt.show()

# 计算累积的组合收益，并绘图
CumulativeReturns = ((1+StockReturns["Portfolio"]).cumprod()-1)
CumulativeReturns.plot()
plt.show()


# 计算相关矩阵
correlation_matrix = stock_return.corr()

sns.heatmap(correlation_matrix,
            annot=True,
            cmap="YlGnBu")

plt.tight_layout()
plt.xticks(rotation=90)
plt.yticks(rotation=0) 
plt.show()
