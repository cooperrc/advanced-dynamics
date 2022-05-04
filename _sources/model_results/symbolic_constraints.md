---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

```{code-cell} ipython3
import sympy
import numpy as np
```

+++ {"tags": []}

# Building Constraints in [SymPy](https://www.sympy.org)

It can be difficult to build constraints for general dynamic solutions. Each constraint is realtively straight forward, but keeping track of Jacobian terms or acceleration constraints
- $\mathbf{C_q}$ 
- $\mathbf{Q_d} = -(\mathbf{C_q \dot{q}})_\mathbf{q}\mathbf{\dot{q}} - 2\mathbf{C}_{\mathbf{q}t}\dot{\mathbf{q}}- \mathbf{C}_{tt}$ 

can be cumbersome and confusing. In this notebook, you will use [SymPy](https://www.sympy.org) to 

1. define $\mathbf{q}~and~\dot{\mathbf{q}}$
2. take a Jacobian and find the constraints on acceleration
3. [`lambdify`](https://docs.sympy.org/latest/tutorial/basic_operations.html#lambdify) the constraints, Jacobian, and $\mathbf{Q}_d$

## 1. define $\mathbf{q}~and~\dot{\mathbf{q}}$

First, define the variables using `sympy.Matrix`. SymPy uses `var` to define variables, here you create

$q = \left[\begin{matrix}q_{1}\\q_{2}\\q_{3}\\q_{4}\\q_{5}\\q_{6}\end{matrix}\right],~
\dot{q} = \left[\begin{matrix}dq_{1}\\dq_{2}\\dq_{3}\\dq_{4}\\dq_{5}\\dq_{6}\end{matrix}\right],~t,~and~L$

as SymPy variables. 

```{code-cell} ipython3
sympy.var('q1, q2, q3, q4, q5, q6')
sympy.var('dq1, dq2, dq3, dq4, dq5, dq6')
sympy.var('t, L2')
q = sympy.Matrix([q1, q2, q3, q4, q5, q6])
dq = sympy.Matrix([dq1, dq2, dq3, dq4, dq5, dq6])
```

```{code-cell} ipython3
q
```

$\mathbf{q} = \left[\begin{matrix}q_{1}\\q_{2}\\q_{3}\\q_{4}\\q_{5}\\q_{6}\end{matrix}\right]$

```{code-cell} ipython3
dq
```

## 2. take a Jacobian and find the constraints on acceleration

![two bodies: sliding block and compound pendulum](../images/spring_compound-2_bodies.svg)

In this example, you have two rigid bodies. Body one $[q_1,~q_2,~q_3]$ slides on the x-axis. Body 1 and body 2, $[q_4,~q_5,~q_6]$ are connected by a pin in the center of body 1, $\mathbf{R}_{pin} = q_1\hat{i}+q_2\hat{j}$. 

```{code-cell} ipython3
C = sympy.Matrix([q1  - q4 + L2/2*sympy.cos(q6),
                 q2 - q5 + L2/2*sympy.sin(q6),
                 q2,
                 q3])
C
```

Next, take the Jacobian, $\mathbf{C_q}$. 

```{code-cell} ipython3
Cq = C.jacobian(q)
print('Cq dimensions:', Cq.shape)
Cq
```

Now, you can calculate 

$\mathbf{Q_d} = -(\mathbf{C_q \dot{q}})_\mathbf{q}\mathbf{\dot{q}} - 2\mathbf{C}_{\mathbf{q}t}\dot{\mathbf{q}}- \mathbf{C}_{tt}$ 

```{code-cell} ipython3

Qd = -(C.jacobian(q)@dq).jacobian(q)@dq\
    - 2*sympy.diff(Cq,t)@dq\
    - sympy.diff(C, t, 2)

Qd
```

## 3. [`lambdify`](https://docs.sympy.org/latest/tutorial/basic_operations.html#lambdify) the constraints, Jacobian, and $\mathbf{Q}_d$

Finally, you can create functions that return NumPy arrays with `sympy.lambdify`. The inputs are

```python
sympy.lambdify( inputs, function, "numpy" )
```

where the `inputs` are $\mathbf{q}$, $\dot{\mathbf{q}}$, and other parameters like time or dimensions, $L^2$.

```{code-cell} ipython3
Cq_sys = sympy.lambdify((q, t, L2), Cq, 'numpy')
```

```{code-cell} ipython3
Cq_sys(np.zeros(6), 1, L2 = 1)
```

```{code-cell} ipython3
Q = sympy.lambdify((q, dq, t, L2), Qd, "numpy")
```

```{code-cell} ipython3
Q(np.ones(6), np.ones(6), 0, L2 = 1)
```

```{code-cell} ipython3

```
