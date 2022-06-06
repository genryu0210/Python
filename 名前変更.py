# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 15:17:21 2022

@author: 406429
"""

import pandas as pd
month = ['05','06']

for i in range(2):
    mon = month[i]
    for j in range(32):
        if j <10 :
            day = '0' + str(j)
        else : day = str(j)
        try :
            log = pd.read_csv(r'nmact_2022' + mon + day + '.log')
            log.to_csv(r'nmact_2022' + mon + day + '(1).log',encoding = 'shift-jis' , index=None)
        except Exception :
            print()