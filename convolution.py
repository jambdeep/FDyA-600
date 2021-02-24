# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 17:13:35 2021

@author: JAB
"""
import numpy as np
import matplotlib.pyplot as plt
 
# pulse
N = 8
n = np.arange(0, N)
x = [1,2,-1,0,1,0,0,0]
h = [4,3,2,1,0,0,0,0]

# Convolve pulse with itself
y = np.convolve(x, h)

# plot
plt.figure(figsize=(10, 8))
plt.subplot(2,1,1)
plt.stem(x)
plt.xlim([-2, 14])
#plt.ylim([-0.2, 3.2])
plt.title('x[n]')

plt.subplot(2,1,2)
plt.stem(y)
plt.xlim([-2, 14])
#plt.ylim([-0.2, 3.2])
plt.title('output system')
plt.show()