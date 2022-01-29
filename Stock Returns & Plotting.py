# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 21:58:37 2022

@author: zacharywe
"""

import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline

file = pd.read_excel('Stock Data.xlsx')

df = pd.DataFrame(file)
df.set_index('Date',inplace=True,drop=True)

tech_port = df['AAPL']+df['MSFT']+df['FB']+df['GOOG']

market = df['SPY']

df2 = pd.concat([tech_port,market],axis=1,join='inner')


day_tech = df2.pct_change()
day_tech = day_tech[1:]

cum_returns_tech = (1 + day_tech).cumprod()-1
cum_returns_tech = cum_returns_tech.reset_index()

day_mkt = df2.pct_change()
day_mkt = day_mkt[1:]

cum_returns_mkt = (1 + day_mkt).cumprod()-1
cum_returns_mkt = cum_returns_mkt.reset_index()


ret_df = pd.concat([cum_returns_tech,cum_returns_mkt['SPY']],axis=1,join="inner")

ret_df2 = ret_df.rename(columns={0: 'Tech Portfolio', 'SPY': 'Market'})
ret_df2 = ret_df2.T.drop_duplicates().T
ret_df2.set_index('Date',inplace=True,drop=True)


#Plotting Reutrns
fig,ax1 = plt.plot(ret_df2)
ret_df2.plot(label='Test')
plt.title('Cumulative Returns: FAMG vs Market (1/7/2017 - 1/7/2021')
plt.ylabel('Cumulative Return')
plt.xlabel('Year')
plt.show()




    





