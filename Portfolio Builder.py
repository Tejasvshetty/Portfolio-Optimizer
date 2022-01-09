# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 14:04:15 2021

@author: Tejas
"""

import pandas as pd
from stock_info import stock_specs

symbols = ['TD', 'AMZN', 'AC']
stocks = stock_specs(symbols)

#display options for Pandas
pd.set_option('display.max_colwidth',  None)
pd.set_option('expand_frame_repr', False)


stocks = stocks[['Adj Close', 'ticker']]
stocks = stocks.pivot(
    columns = 'ticker',
    values = 'Adj Close'
    )

stocks.to_csv('C:/Projects/Portfolio Builder/stock_data.csv')
