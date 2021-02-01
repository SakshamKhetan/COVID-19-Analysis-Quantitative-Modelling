# -*- coding: utf-8 -*-
"""Widhya Task

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1znkxG582e9c2H5bofTHxLX2iU89CevTP
"""

import pandas as pd
import numpy as np

df = pd.read_csv("covid19_data.csv",names = ['S.no','Date','State','Indian','Foreign','Cured','Deaths'],skiprows=[0], index_col='S.no')
Date_grp = df.groupby(['Date'],sort=False).sum()
Date_grp['Sum']= Date_grp.sum(axis=1)
Date_grp = Date_grp.reset_index()

import matplotlib.pyplot as plt

fig,ax = plt.subplots()
ax.scatter(Date_grp['Date'],Date_grp['Sum'])
ax.set_title('Covid Dataset')
ax.set_xlabel('Date')
ax.set_ylabel('Total cases')

fig = plt.figure()
ax = plt.axes()
ax.plot(Date_grp['Date'],Date_grp['Sum'])

df = (Date_grp.loc[:,['Date','Sum']]).iloc[34:]
df

r = (df['Sum'].pct_change()).mean()

import math

P_o = 31
t =26 
P_t = P_o*(math.exp(r*t))
P_t

