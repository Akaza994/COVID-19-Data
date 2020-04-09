#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 15:37:14 2020

@author: zhijianli
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

##################################
## process the data from kaggle ##
##################################
'''
df=pd.read_csv('train.csv')
data=df[df['Country_Region']=='US']
data=data[data['Province_State']!='Puerto Rico']
data=data[data['Province_State']!='Virgin Islands']
states=data.Province_State.unique()
state_list=[]
for i in range(len(states)):
    state_list.append(states[i])
data.to_csv('intermediate.csv') 
'''
#there is a mistake in Alaska data (the cumulative data decreases for a day)
#Another mistake: Washington 3/18 should be 1246
#I save a intermediate data and manually fix it  
data=pd.read_csv('intermediate.csv')
days=len(data)/52-1
daily_data=np.zeros((days,52))
daily_death=np.zeros((days,52))
for k, state in enumerate(state_list):
    temp=data[data['Province_State']==state].ConfirmedCases.values
    for i in range(days):
        #get the differece for daily data
        daily_data[i,k]=temp[i+1]-temp[i]
    temp=data[data['Province_State']==state].Fatalities.values
    for i in range(days):
        #get the differece for daily data
        daily_death[i,k]=temp[i+1]-temp[i]
np.savetxt('daily_confirmed.csv',daily_data,delimiter=',')
np.savetxt('daily_death.csv',daily_death,delimiter=',')
with open("states.txt", 'w') as output:
    for state in state_list:
        output.write(state + '\n')
'''

state='CA'
county='Los Angeles'
df=pd.read_csv('cases.csv')
Cal=df[df['state_name']==state]
LA=Cal[Cal['county_name']==county][1:]
LA=LA[LA['confirmed_count']!=0]
LA=LA.drop(LA.columns[[0,2,3,5]],axis=1)
LA=LA.set_index('confirmed_date')
'''