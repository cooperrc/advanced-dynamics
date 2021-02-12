import numpy as np
from numpy import sin,cos,pi
import matplotlib.pyplot as plt

def setdefaults():
  plt.rcParams.update({'font.size': 22})
  plt.rcParams['lines.linewidth'] = 3

setdefaults()

from scipy.integrate import solve_ivp # import the ordinary differential equation integrator in Python

# Homework #5 - _work in progress_

![Whirling Roller-coaster](https://drive.google.com/thumbnail?id=1f0tVO6X1HDQiIRcADBUVx3HlnZjH3TZl&authuser=0&sz=w952-h932)

Consider your roller coaster design from HW #4. Assume the cart rolls on the track as a frictionless
point-mass of 100-kg. Determine the equations of motion in terms of the distance from the
lowest point, $q_1=x_2$. 

1. Create a function, cart_ode, that represents the equation of motion for the car in terms of $x_2$

def cart_ode(t,r,w):
    '''Set of 2 ODEs that return dx2/dt and d^2x2/dt^2 with input
    x2 and dx2/dt, dr/dt = f(t,r)'''
    dr=np.zeros(np.shape(r))
    dr[0]=r[1]
    dr[1] #= ... your equation here
    return dr

2. Solve the `cart_ode` initial value problem for x(0)=10 m, dx/dt(0)=0 m/s and $\omega$=0 rad/s

x0=10
v0=0
w=0 # rad/s
end_time=10 # choose an end time that displays one full period

r0 = solve_ivp(lambda t,r: cart_ode(t,r,w),[0, end_time],[x0,v0])

3. Solve the `cart_ode` initial value problem for x(0)=10 m, dx/dt(0)=0 m/s and $\omega$=1 rad/s

x0=10
v0=0
w=3
end_time=10 # choose an end time that displays one full period

r1 = solve_ivp(lambda t,r: cart_ode(t,r,w),[0, end_time],[x0,v0])

4. Solve the `cart_ode` initial value problem for x(0)=10 m, dx/dt(0)=0 m/s and $\omega$=2 rad/s

x0=10
v0=0
w=6
end_time=10 # choose an end time that displays one full period

r2 = solve_ivp(lambda t,r: cart_ode(t,r,w),[0, end_time],[x0,v0])

5. Plot the three solutions together

plt.plot(r0.t,r0.y[0],label='0 rad/s')
plt.plot(r3.t,r3.y[0],label='3 rad/s')
plt.plot(r6.t,r6.y[0],label='6 rad/s')
plt.legend()