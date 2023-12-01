import yfinance as yf
import time
import pandas as pd
# 讀取csv檔
import numpy as np


historical_data = pd.DataFrame()
stocks = ['2883', '2317','2454', '2303', '3231', '3008', '2352', '2330', '2412']
res = []
for stock in stocks:    
    stock_id = stock + '.TW'
    data = yf.Ticker(stock_id)
    df = data.history(period="max")
    df['date'] = df.index
    df = df[['date', 'High', 'Low', 'Open', 'Close', 'Volume', 'Volume']].rename(columns={'High': 'high', 'Low':'low', 'Open': 'open', 'Close': 'close', 'Volume': 'volume'})
    df_np = df.to_numpy()
    df_np = df_np[-2500:]
   
    DF = pd.DataFrame(df_np)
 
    # save the dataframe as a csv file
    DF.to_csv(f'./pgportfolio/data/data_{stock}.csv')
   



#s = np.load('./pgportfolio/data/stockTW.npy', allow_pickle=True)
# shape (9, 1784, 7) ['date', 'high', 'low', 'open', 'close', 'volume', 'quoteVolume']

# TODO auto pipeline
# 金融 開發金 2883  
# 鋼鐵 中鋼 2002
# 航空 長榮航 2618
# 電子 聯電 2303
# AI 緯創 3231
# 航運 裕民 2606
# 佳士達 2352 
    # historical_data = pd.DataFrame()
    # stocks = ['2883', '2002','2618', '2303', '3231', '2606', '2352']
    # for i in stocks:    
    #     # 抓取股票資料
    #     stock_id = i + '.TW'
    #     data = yf.Ticker(stock_id)
    #     df = data.history(period="max")
    #     # 增加股票代號
    #     df['stock_id'] = i
    #     # 合併
    #     historical_data = pd.concat([historical_data, df])
    #     time.sleep(0.8)
    # historical_data.to_csv('./TWstocks/historical_data.csv')
#####



