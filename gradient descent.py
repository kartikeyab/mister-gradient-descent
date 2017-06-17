# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 14:11:15 2017

@author: Kartikeya BHardwaj
"""

import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
df = pd.read_csv('test.csv')


x_points = df['x'].tolist()
y_points = df['y'].tolist()


#equation y = mx+b
m = 0
b = 0
y = lambda x: m*x+b

def plot_line(y , data_values):
    x_values = [i for i in range(int(min(data_values))-1 , int(max(data_values))+2)]
    y_values = [y(x) for x in x_values]
    plt.plot(x_values , y_values , 'r')
    
    

learn = 0.001

def summation(y, x_points , y_points):
    total1 =0
    total2= 0
    for i in range(1,len(x_points)):
        total1 += y(x_points[i]) - y_points[i]
        total2 += ((x_points[i]) - y_points[i])*x_points[i]
    return total1/len(x_points) , total2/len(x_points) 
        
        
        
for i in range(400):
    s1 , s2 = summation(y, x_points , y_points)
    m = m - learn*s1
    b = b - learn*s2
    
    
plot_line(y , x_points)    
plt.plot(x_points, y_points , 'bo')    
    
 
 
 
 
        
        
      
    
    

    
    
    
