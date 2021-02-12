import numpy as np
from numpy import sin,cos,pi
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

# Homework #2
## Example from class on plotting kinematic solutions

![double pendulum](../images/p1-10_double_pendulum.png)

### define kinematic known values

First, we can define the independent variable, `t`, to complete one full cycle. Then, we can use the inputs for $x,~\theta_1,~and~\theta_2$. 

t=np.linspace(0,2*pi/50,100); # create time varying from 0-0.126 s (or one period)
x=20*sin(50*t);     # define x in terms of time 
dx=20*50*cos(50*t); # define dx/dt in terms of time (note dx=dx/dt)
t1=0.2*pi*cos(50*t); # define theta1 (t1) 
dt1=-10*pi*sin(50*t); # define dtheta1/dt (dt1)
t2=0.2*pi*sin(50*t-pi/3); # define theta2 (t2) ;
dt2=10*pi*sin(50*t-pi/3); # define dtheta2/dt (dt2);
L1=1;L2=1.5; # set lengths for L1 and L2 (none were given in problem so 1 and 1.5 mm were
             # chosen arbitrarily

### define the other dependent kinematic values

In the lecture, you derived the positions of the link connections using the given values. Here, we apply those definitions to get the global positions of each link endpoint. 

rcc=np.array([x+L1*sin(t1),-L1*cos(t1)]) # position of connection between links
rco=np.array([x+L1*sin(t1)+L2*sin(t2),-(L1*cos(t1)+L2*cos(t2))])    # create a row vectors of
                                                                    # x-component and y-component of
                                                                    # pendulum position C (r_C/O) 
vco=np.array([dx+L1*cos(t1)*dt1+L2*cos(t2)*dt2,
     (L1*sin(t1)*dt1+L2*sin(t2)*dt2)]) # create row
                                       # vectors of
                                       # the x- and
                                       # y-component
                                       # velocity of
                                       # point C

### Plot results

Here, you plot the velocity components of the end of the lower link.

plt.plot(t,vco[0,:],label=r'$v_x$')
plt.plot(t,vco[1,:],label=r'$v_y$')
plt.xlabel('time (s)')
plt.ylabel('v (mm/s)')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.title('End velocity')

### Animate the motion

Here, you create an HTML animation for the 2-bar linkage

1. Create function that plots the links at timesteps

2. [matplotlib's animation in HTML5](http://louistiao.me/posts/notebooks/embedding-matplotlib-animations-in-jupyter-as-interactive-javascript-widgets/)

from matplotlib import animation
from IPython.display import HTML

1. Create a figure to display the animation and add fixed background _the dashed line is added to show the path the end point takes_

fig, ax = plt.subplots()

ax.set_xlim(( -30, 30))
ax.set_ylim((-3, 0))
ax.set_xlabel('x-position (m)')
ax.set_ylabel('y-position (m)')

line, = ax.plot([], [])
marker, = ax.plot([], [], 'o', markersize=10)
ax.plot(rco[0,:],rco[1,:],'--')

2. Create an initializing (`init`) function that clears the previous line and marker

def init():
    line.set_data([], [])
    marker.set_data([], [])
    return (line,marker,)

3. Create an animating (`animate`) function that updates the line

def animate(i):
    '''function that updates the line and marker data
    arguments:
    ----------
    i: index of timestep
    outputs:
    --------
    line: the line object plotted in the above ax.plot(...)
    marker: the marker for the end of the 2-bar linkage plotted above with ax.plot('...','o')'''
    line.set_data([x[i],rcc[0,i],rco[0,i]],[0,rcc[1,i],rco[1,i]])
    marker.set_data([rco[0, i], rco[1,i]])
    return (line, marker, )

4. Create an animation (`anim`) variable using the `animation.FuncAnimation`

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=range(0,len(t)), interval=100, 
                               blit=True)

HTML(anim.to_html5_video())

## Problem 1

![Pendulum on train](../images/Wells-Fig_1-5.png)

The axis shown in Fig 1-5 has the following constants

$v_x=1$ m/s. 

$m= 1$ kg

$r= 500$ mm

$l_2 = 1000$ mm

$l_1 = 1200$ mm

$s_2 = 10$ mm

$v_y = 0$ m/s

$a_x = 0$ m/s$^2$

**(a)** Plot the angle of the pendulum for one full period of oscillation given $\theta(0)=\pi/12$ and $\dot{\theta}(0)=0$

 # insert code here

**(b)** make an animation of the position of the mass, $m$, in terms of $X_1$ and $X_2$ for $t=0-0.5$s

# convert theta -> X1 ad X2 positions
X1 = np.array([])
X2 = np.array([])

fig2, ax2 = plt.subplots()

ax2.set_xlim((0, 1))
ax2.set_ylim((0, 1.2))
ax2.set_xlabel('x-position (m)')
ax2.set_ylabel('y-position (m)')

line, = ax2.plot([], [],'o-') # add marker at end points
marker, = ax2.plot([], [], 'o', markersize=10)
ax2.plot(X1,X2,'--', label = 'path')

def animate2(i):
    '''function that updates the line data for the pendulum
    arguments:
    ----------
    i: index of timestep
    outputs:
    --------
    line: the line object plotted in the above ax.plot(...)
    '''
    line.set_data([0,X1[i]],[0,X2[i]])

anim2 = animation.FuncAnimation(fig, animate2, init_func=init,
                               frames=range(0,len(X1)), interval=100, 
                               blit=True)

HTML(anim2.to_html5_video())

**(c)** Plot the angle $\theta$ for one period of oscillation for 2 conditions, label your two lines on one graph:

1. $a_x=$ 0 m/s$^2$

2. $a_x=$ 4 m/s$^2$

 #your work here