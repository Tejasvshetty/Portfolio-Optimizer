# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 15:03:05 2021

@author: Tejas
"""

"""
This module is to scrap data for the portfolio builder using the 
yahoo finance api through the yfinance package
"""

import yfinance as yf
import pandas as pd

def stock_specs(tickerStrings):
    df_list = list()
    for ticker in tickerStrings:
        data = yf.download(ticker, group_by="Ticker", period='3y')
        data['ticker'] = ticker  # add this column because the dataframe doesn't contain a column with the ticker
        df_list.append(data)
    
    # combine all dataframes into a single dataframe
    df = pd.concat(df_list)
    return df