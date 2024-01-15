#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


# # Homework #2
# 
# ![slider crank diagram: two links connected to a piston and the ground](../images/slider-crank.svg)

# Consider the slider-crank shown above. Two links are connected by pins to the ground at $A$ and the piston at $C$. Link AB can rotate around $A$ and link BC can rotate around $C$ and the piston maintains contact with the ground. 
# 
# Consider the following kinematic properties:
# 
# - link AB $L_1 = 1~m$
# - link BC $L_2 = 1~m$
# - the angle of link AB rotates at a constant $\dot{\theta}_1 = 1~rad/s$
# 

# __1.__ How many degrees of freedom does the slider-crank have? _How many degrees of freedom and how many constraints?_

# __2.__ The system begins to move with both links horizontal e.g. $\theta_1 = \theta_2 = 0^o$ and $\mathbf{r}_c = 2~m \hat{i}$. Find the positions of $A,~B,~and~C$ for one full rotation, $t = 0...2\pi$.

# __3.__ Plot the positions of $B~and~C$ vs time. 
