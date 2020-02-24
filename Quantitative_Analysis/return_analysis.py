import numpy as np
import pandas as pd
import datetime as datetime
import time
import pandas_datareader as pdr

start = datetime.datetime(2019,2, 24)
end = datetime.datetime(2020, 2, 24)

result = pd.DataFrame(columns=("code","年算术平均收益","年对数收益","近一周平均收盘价","平均收盘价格","日平均收益"))

N=0
for i in range(1300,10000):
    code = "{0}.T".format(i)
    
    try:
    
        df = pdr.DataReader(code, 'yahoo', start, end)
        df.index = pd.to_datetime(df.index)
        
        df['Returns']=df['Adj Close'].pct_change()
        df['Returns'].fillna(value=0, inplace=True)
        mean_close = np.mean(df["Adj Close"])
        
        mean_return_daily=np.mean(df['Returns'])
        if mean_return_daily>0.4:
            continue
        
        last_close = np.mean(df['Adj Close'][-5:-1])

        day = len(df.index)
        
        mean_return_annualized = ((1+mean_return_daily)**day)-1
        
        #############################
        log_return = np.log(df['Adj Close'][-1]/df['Open'][0])
        
        
        
        
        
        print("Code:",code)
        
        result = result.append(pd.DataFrame({"code":[code],
                                             "平均收盘价格":[mean_close],
                                             "近一周平均收盘价":[last_close],
                                             "年算术平均收益":[100*mean_return_annualized],
                                             "年对数收益":[100*log_return],
                                             "日平均收益":[100*mean_return_daily]
                                             }),
                                                ignore_index=True)
    
    except pdr._utils.RemoteDataError:
        pass
    except KeyError:
        pass
    
    N+=1
    
    if N%100 ==0:
        time.sleep(300)
    
