# -*- coding: utf-8 -*-
"""
Created on Sat May  2 18:19:29 2020

@author: cycle
"""
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import pandas as pd
import random

df={'k':[[1,2],[2,3],[3,1]],'r':[[6,5],[7,7],[8,6]]}

new_features=[1,5]

def kNN(data,predict,k=3):
    if k==len(data):
        print("Warning")
    distances=[]
    for i in data:
        for j in data[i]:
            euclidean_distance=np.linalg.norm(np.array(j)-np.array(predict))
            distances.append([euclidean_distance,i])
    #print(distances)        
    votes=[]
    for i in sorted(distances)[:k]:
        votes.append(i[1])
    vote_result=Counter(votes).most_common(1)
    return vote_result[0][0]

new_group=kNN(df,new_features,k=3)
print(new_group)

df=pd.read_csv('breast-cancer-wisconsin.data.txt')    
df.replace('?',-99999,inplace=True)
df.drop(['1000025'],1,inplace=True)
df
full_data=df.astype(float).values.tolist()
full_data
train
