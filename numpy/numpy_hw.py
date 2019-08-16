# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 23:56:31 2019

@author: Mutlu
"""
import numpy as np
import time
counter=0
start_time = time.time()
while True:
    counter+=1
    arr1=np.random.random((20,20))
    arr2=np.random.random((20,20))
    newArr=arr1-arr2
    diagonals=[newArr[i,i] for i in range(20)]
    if all(-0.1<item<0.1 for item in diagonals):
        print(diagonals)
        break
print('Python engine worked '+str(counter)+' times')
print("It  took %s seconds" % (time.time() - start_time))

