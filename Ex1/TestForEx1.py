# -*- coding: utf-8 -*-
"""
Created on Tue Feb 06 11:30:55 2018

@author: Pleun
"""
import numpy as np

a = np.array([1,2,3,4])
b = np.array([[5,6],
              [7,8]])
#print(b.dot(a))
print(a.transpose().dot(a))
print(1**2+2**2+3**2+4**2)
