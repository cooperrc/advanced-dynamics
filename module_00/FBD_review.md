# Review of creating and using Free Body Diagrams

Free body diagrams are **the most useful** engineering tool you have.
With a good free body diagram you can define:
1. equations of motion
2. work-energy of a system
3. impulse-momentum of a system

That way you will have all the necessary definitions to define what
caused the motion. 

Take a working example, you will start very simple, and add complexity

## Driving a car without dampers

<iframe width="560" height="315"
src="https://www.youtube.com/embed/rYAMGy9LxVY" title="YouTube video
player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
encrypted-media; gyroscope; picture-in-picture"
allowfullscreen></iframe>

In the video above, the Ford Focus shocks are drained and then its
driven down the road (_don't try this at home_). To start, consider the
system as a single degree of freedom, just up-down motion

### Simplified 1-DOF FBD
![Simplified car FBD](../images/simple_car_FBD.svg)

In the _very simple_ up-down motion of the car, you have already found
some helpful information. The only force supporting the car, is the force
applied from the springs. The resulting simplified equation of motion is
as such

$ma = F_s - mg\rightarrow a = -k(y_{car} - L_0) - g$

where $y_{car}$ is the height of the car and $L_0$ is unstretched spring
length.


### More involved 2-DOF FBD

![More involved 2-DOF car that can rotate](../images/2dof_car_FBD.svg)

In this more involved FBD, I have added the _kinetic diagram_ to
describe the motion. I am not concerned with its forward acceleration,
$\ddot{x}$, but instead I want to call attention to the _coupled_ ODE's
for rotation and upward motion. 

1. $\sum F_y = m\ddot{y}_{com}$
2. $\sum M_G = I_G\ddot{\theta}$

The forces acting on the car are $mg$, $F_1 = -k(y_1- L_0)$, and 
$F_2 = -k(y_2 - L_0)$. 
where the angle $\theta = \sin^{-1}\frac{y_2 - y_1}{wheel-base}$ where
$wheel-base = 2.64~m~or~104"$ for a Ford Focus. 

Since the Ford Focus has an engine in the front, I'm making an educated
guess that the center of mass is closer to the front of the car, maybe a
60-40 split

1. $\ddot{y}_{com} = -\frac{k}{m}(y_1 - L_0)-\frac{k}{m}(y_2 - L_0) -
   mg$
2. $I\ddot{\theta} = 1.06~m\cdot(\frac{k}{m}(y_1 - L_0)) -
   1.58~m\cdot(-\frac{k}{m}(y_2 - L_0))$

In these 2 equations of motion, you have 4 unknown variables,
$y_1,~y_2,~y_{com},~and~\theta$. _But_, if you know 2-out-of-4, you know
the rest, because $\sin\theta \approx \theta = \frac{y_2 - y_1}{wheel-base} =
\frac{y_{com} - y_1}{wheel-base \cdot 0.6}$. So, you can substitute for
**2 chosen degrees of freedom**. 


1. $\ddot{y}_{com} = -\frac{k}{m}(\theta - L_0)-\frac{k}{m}(y_2 - L_0) -
   mg$
2. $I\ddot{\theta} = 1.06~m\cdot(\frac{k}{m}(y_1 - L_0)) -
   1.58~m\cdot(-\frac{k}{m}(y_2 - L_0))$
