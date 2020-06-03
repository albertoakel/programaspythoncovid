#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 10:04:36 2020

@author: akel
programa para leitura de arquivos cvc
"""


import matplotlib.pyplot as plt
from matplotlib.dates import (YEARLY, DateFormatter,
                              rrulewrapper, RRuleLocator, drange)
from matplotlib.dates import num2date,datestr2num
import numpy as np
import datetime
import pandas as pd
import scipy.io as spio
plt.close('all')


# file = gp.create_model('Tutorial_ch1_1_Basics')

# data_path = 'https://raw.githubusercontent.com/cgre-aachen/gempy_data/master/'



# temp=pd.read_csv('book.cvs')





cabecalho=['date','state','city','place_type','confirmed','deaths','is_last','estimated_population_2019','city_ibge_code','confirmed_per_100k_inhabitants','death_rate']
temp=pd.read_csv('/home/akel/Downloads/covid19-3d539980b41c4abeb5d0ecf6fab11644.csv',header=None, names=cabecalho)
NL=np.size(temp.to_numpy(),axis=0) #número de colunas

t=temp['date']
D=temp['deaths']
C=temp['confirmed']


t=t[1:NL].to_numpy(dtype='M')
C=C[1:NL].to_numpy(dtype='float')
D=D[1:NL-1].to_numpy(dtype='float')

t=np.flipud(t)
C=np.flipud(C)
D=np.flipud(D)


formatter = DateFormatter('%d/%m/')

dif=np.zeros(NL-1)
dif[1:NL-1]=np.diff(C)

# dif=np.diff(C)



fig1, ax = plt.subplots()
ax.plot(t,C)
plt.xlim(pd.Timestamp('2020-03-18'),pd.Timestamp('2020-05-27'))
#plt.yscale('symlog')

ax.xaxis.set_major_formatter(formatter)
ax.grid('on')


fig2, ax = plt.subplots()
#ax.bar(t,dif)
ax.plot(t,dif,'-o')
plt.xlim(pd.Timestamp('2020-03-18'),pd.Timestamp('2020-05-27'))

ax.xaxis.set_major_formatter(formatter)
# ax.grid('on')
