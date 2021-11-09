#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
import numpy as np
from scipy.special import *
plt.style.use('grayscale')
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Plots of Bessel Functions of Positive Integers  ---- First  Kind

# In[2]:


import random

def bessel_pos(num):
   
    colors = iter(cm.rainbow(np.linspace(0,1,num)))
    x = np.linspace(-10,10,100)
    nums = np.arange(1,num+1)
    fig = plt.figure()
    fig.set_dpi(100)
    ax = fig.add_subplot(1,1,1)
    #ax.set_axis_off()
    ax.set_title("Bessel Plot (n = 1,2,...,num)\n")
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    
    for n in nums:
        y = jv(n,x)
        plt.plot(x,y,c=next(colors), label='n=J{}(x)'.format(n))
    plt.legend(loc='upper left',prop={'size':5})
    plt.show()
bessel_pos(8)        


# ## Plots of Bessel Functions of Negative Integers --- First  Kind

# In[3]:


def bessel_neg(num):
    colors = iter(cm.rainbow(np.linspace(0,1,num)))
    x = np.linspace(-10,10,100)
    nums = np.arange(1,num+1)
    fig = plt.figure()
    fig.set_dpi(100)
    ax = fig.add_subplot(1,1,1)
    #ax.set_axis_off()
    ax.set_title("Bessel Plot (n = -1,-2,...,-num)\n")
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    
    for n in nums:
        y = jv(n,x*-1)
        plt.plot(x,y,c=next(colors), label='n=J-{}(x)'.format(n))
    plt.legend(loc='upper left',prop={'size':5})
    plt.show()
bessel_neg(8)        


# ## Plots of Bessel Functions of Positive Half Integers --- First  Kind

# In[4]:


def bessel_pos_half(num):
   
    colors = iter(cm.rainbow(np.linspace(0,1,num+1)))
    x = np.linspace(-10,10,100)
    nums = np.arange(0,num+1)
    fig = plt.figure()
    fig.set_dpi(100)
    ax = fig.add_subplot(1,1,1)
    #ax.set_axis_off()
    ax.set_title("Bessel Plot (n = 0.5,1.5,...,num/2)\n")
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    
    for n in nums:
        y = jv(n,x+0.5)
        plt.plot(x,y,c=next(colors), label='n=J{}(x)'.format(n+0.5))
    plt.legend(loc='upper left',prop={'size':5})
    plt.show()
bessel_pos_half(8)        


# ## Plots of Bessel Functions of Negative Half Integers --- First  Kind

# In[5]:


def bessel_neg_half(num):
   
    colors = iter(cm.rainbow(np.linspace(0,1,num+1)))
    x = np.linspace(-10,10,100)
    nums = np.arange(0,num+1)
    fig = plt.figure()
    fig.set_dpi(100)
    ax = fig.add_subplot(1,1,1)
    #ax.set_axis_off()
    ax.set_title("Bessel Plot (n = -0.5,-1.5,...,-num/2)\n")
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    
    for n in nums:
        y = jv(n,(x+0.5)*-1)
        plt.plot(x,y,c=next(colors), label='n=J{}-(x)'.format(n+0.5))
    plt.legend(loc='upper left',prop={'size':5})
    plt.show()
bessel_neg_half(8)        

