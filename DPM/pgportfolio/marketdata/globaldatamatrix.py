from __future__ import division
from __future__ import absolute_import
from __future__ import print_function


import numpy as np
import pandas as pd
from pgportfolio.tools.data import panel_fillna
from pgportfolio.constants import *
import sqlite3
from datetime import datetime
import logging
import pickle


def get_TW_stocks(stock_ids):
    stocks = []
    for id in stock_ids:
        stock_data = pd.read_csv(f'./pgportfolio/data/data_{id}.csv',index_col=False).to_numpy()
        stock_data = np.delete(stock_data, 0, 1)
        stocks.append(stock_data)
    stocks = np.vstack(stocks).reshape((9,-1,7))
    return stocks
def get_global_panel_stock(start, end, period=300, features=('close',)):
    """
    :param start/end: linux timestamp in seconds
    :param period: time interval of each data access point
    :param features: tuple or list of the feature names
    :return a panel, [feature, coin, time]
    """
    
     
    coins = ['2883', '2317','2454', '2303', '3231', '3008', '2352', '2330', '2412']
    stock = get_TW_stocks(coins)
    logging.info("feature type list is %s" % str(features))

    stock_cols = ['date', 'high', 'low', 'open', 'close', 'volume', 'quoteVolume']

    time_index = pd.to_datetime(stock[0, :, 0])
    print(time_index)
    
    panel = pd.Panel(items=features, major_axis=coins, minor_axis=time_index, dtype=np.float32)


    for row_number, coin in enumerate(coins):
        chart = stock[row_number, :, :]
        df = pd.DataFrame(chart, columns=['date', 'high', 'low', 'open', 'close', 'volume', 'quoteVolume'])
        df['date'] = pd.to_datetime(df['date'])
        df = df.set_index('date')
        for feature in features:
            panel.loc[feature, coin, :] = df.loc[:,feature].tolist()
            panel = panel_fillna(panel, "both")

    return panel

def get_global_panel_btc(start, end, period=300, features=('close',), stocks=1):
    if stocks == 1:
        panel = pd.read_pickle('pgportfolio/data/btc.pkl')
    elif stocks == 2:
        panel = pd.read_pickle('pgportfolio/data/crix_2.pkl')
    elif stocks == 3:
        panel = pd.read_pickle('pgportfolio/data/crix_3.pkl')
    elif stocks == 4:
        panel = pd.read_pickle('pgportfolio/data/crix_4.pkl')
    else:
        print("no file")
    print(panel.shape)
    return panel