# -*- coding: utf-8 -*-
"""
Created on Sat May  2 09:19:23 2020

@author: DarshanMohan
"""

from statistics import mean
import numpy as np
import matplotlib.pyplot as plt

xs=np.array([1,2,3,4,5,6])
ys=np.array([5,4,6,5,6,7])

def best_fit_slope(xs,ys):
    m=mean(xs)*mean(ys)
    mcomb=mean(xs*ys)
    
    m_x=pow(mean(xs),2)
    mxcomb=mean(pow(xs,2))
    final=(m-mcomb)/(m_x-mxcomb)
    b=mean(ys)-final*mean(xs)
    return final,b

def squared_error(ys_original,ys_line):
    return sum((ys_line-ys_original)**2)

def coef_determination(ys_original,ys_line):
    y_mean_line=[mean(ys_original) for y in ys_original]
    squared_error_regr=squared_error(ys_original,ys_line)
    squared_error_y_mean=squared_error(ys_original,y_mean_line)
    return 1-(squared_error_regr/squared_error_y_mean)

m,b=best_fit_slope(xs,ys)
regrsn_line=[(m*x)+b for x in xs]
print(coef_determination(ys,regrsn_line))


