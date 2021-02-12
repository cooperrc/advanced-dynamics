import numpy as np
from scipy.linalg import *

# Homework #6 - _work in progress_
## Linear Algebra for Dynamics

Equations of motion in Newtonian ($F=ma$) or Lagrangian ($\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{x}_{i}}\right)-\frac{\partial L}{\partial x_i} = F_i$) are solved with Linear Algebra equations

$\mathbf{Ax}=\mathbf{b}$ or $\mathbf{Ax}=\lambda \mathbf{x}$

Take the following matrix, saved as array `A`:

A=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
A

A is an $m \times n$ matrix where m=4 rows and n=3 columns

np.shape(A)

The tranpose of A is $3\times 4$

A.T # <array>.T is the numpy method to transpose an array, for our purposes array == matrix

## Problem 1

Try making an array that is 2 rows $\times$ 3 columns. Then take its transpose so it is 3 rows $\times$ 2 columns



## Matrices and vectors are sets of linear equations

Representation of linear equations:

1. $5x_{1}+3x_{2} =1$

2. $x_{1}+2x_{2}+3x_{3} =2$

3. $x_{1}+x_{2}+x_{3} =3$

in matrix form:

$\left[ \begin{array}{ccc}
5 & 3 & 0 \\
1 & 2 & 3 \\
1 & 1 & 1 \end{array} \right]
\left[\begin{array}{c} 
x_{1} \\ 
x_{2} \\
x_{3}\end{array}\right]=\left[\begin{array}{c} 
1 \\
2 \\
3\end{array}\right]$

$Ax=b$

### Vectors 

column vector x (length of 3):

$\left[\begin{array}{c} 
x_{1} \\ 
x_{2} \\
x_{3}\end{array}\right]$

row vector y (length of 3):

$\left[ y_{1} y_{2} y_{3} \right]$

vector of length N:

$\left[\begin{array}{c} 
x_{1} \\ 
x_{2} \\
\vdots  \\
x_{N}\end{array}\right]$

The $i^{th}$ element of x is $x_{i}$

### Matrices

elements in the matrix are denoted $B_{row~column}$

In general, matrix, B, can be any size, $M \times N$ (M-rows and N-columns):

$B=\left[ \begin{array}{cccc}
B_{11} & B_{12} &...& B_{1N} \\
B_{21} & B_{22} &...& B_{2N} \\
\vdots & \vdots &\ddots& \vdots \\
B_{M1} & B_{M2} &...& B_{MN}\end{array} \right]$

## Multiplication

A column vector is a $1\times N$ matrix and a row vector is a $M\times 1$ matrix

**Multiplying matrices is not commutative**

$A B \neq B A$

Inner dimensions must agree, output is outer dimensions. 

A is $M1 \times N1$ and B is $M2 \times N2$

C=AB

Therefore N1=M2 and C is $M1 \times N2$

If $C'=BA$, then N2=M1 and C is $M2 \times N1$

e.g. 
$A=\left[ \begin{array}{cc}
5 & 3 & 0 \\
1 & 2 & 3  \end{array} \right]$

$B=\left[ \begin{array}{cccc}
1 & 2 & 3 & 4 \\
5 & 6 & 7 & 8 \\
9 & 10 & 11 & 12 \end{array} \right]$

C=AB

$[2\times 4] = [2 \times 3][3 \times 4]$

The rule for multiplying matrices, A and B, is

$C_{ij} = \sum_{k=1}^{n}A_{ik}B_{kj}$

In the previous example, 

$C_{11} = A_{11}B_{11}+A_{12}B_{21}+A_{13}B_{31} = 5*1+3*5+0*9=20$


Multiplication is associative:

$(AB)C = A(BC)$

and distributive:

$A(B+C)=AB+AC$

*Note: You can multiply matrices in Python with `@`*

A=np.array([[5,3,0],[1,2,3]]) 
B=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
C=A@B # multiply AB
C

B@A

## Problem 2

Given:

$A=\left[ \begin{array}{cc}
5 & 3 \\
1 & 2 \end{array} \right]$

$B=\left[ \begin{array}{cc}
1 & 2 \\
5 & 6 \end{array} \right]$

$C=\left[ \begin{array}{cc}
11 & 5 \\
5 & 4 \end{array} \right]$

Calculate $D1=A(B+C)$ and $D2=AB+AC$. Are they equal?

A=np.array([[5,3],[1,2]])
B=np.array([[1,2],[5,6]])
C=np.array([[11,5],[5,4]])
D1=A # replace with your algebra
D2=B # replace with your algebra



## Differentiation

In many applications in mechanics, scalar and vector functions that depend on one or more variables are encountered. An example of a scalar function that depends on the system velocities and possibly on the system coordinates is the kinetic energy. Examples of vector functions are the coordinates, velocities, and accelerations that depend on time. Let us first consider a scalar function f that depends on several variables q1, q2, ... , and qn and the parameter t, such that

![](https://learning.oreilly.com/library/view/computational-dynamics-3rd/9780470686157/figs/UEQ260.png)

The total derivative $df/dt$ becomes

![](https://learning.oreilly.com/library/view/computational-dynamics-3rd/9780470686157/figs/UEQ261.png)

![](https://learning.oreilly.com/library/view/computational-dynamics-3rd/9780470686157/figs/UEQ263.png)

Where $\frac{\partial f}{\partial \mathbf{q}}$ can be rewritten as

![](https://learning.oreilly.com/library/view/computational-dynamics-3rd/9780470686157/figs/UEQ264.png)

U=np.array([[1,2,3],[0,4,5],[0,0,6]])
L=np.array([[1,0,0],[2,3,0],[4,5,6]])
D=np.diag([1,2,3])
print('upper triangular matrix, U:')
print(U)
print('lower triangular matrix, L:')
print(L)
print('diagonal matrix, D:')
print(D)

## Problem 3
Make a function that returns the partial derivative of $f(q_1,q_2,q_3,t)$ with respect to $\mathbf{q}$

$\frac{\partial f}{\partial \mathbf{q}}$

![](https://learning.oreilly.com/library/view/computational-dynamics-3rd/9780470686157/figs/U02180.png)

def dfdq(q1,q2,q3,t):
    # your work
    return df

Use your function `dfdq` to create a function that returns the total derivative of $f(q_1,q_2,q_3,t)$ with respect to $t$

if $q_1(t) = 2t$, $q_2(t) = 5t$, and $q_3(t) = t^2$

def dfdt(q1,q2,q3,t):
    df=dfdq(q1,q2,q3,t)
    dfdt = # your work

For a number of functions, $f_1$...$f_n$

![](https://learning.oreilly.com/library/view/computational-dynamics-3rd/9780470686157/figs/UEQ265.png)

The total derivative is a similar form

![](https://learning.oreilly.com/library/view/computational-dynamics-3rd/9780470686157/figs/UEQ268.png)

or

![](https://learning.oreilly.com/library/view/computational-dynamics-3rd/9780470686157/figs/UEQ270.png)

## Problem 4

Create a function that returns $\frac{\partial \mathbf{f}}{\partial\mathbf{q}}$ where $\mathbf{f}$ is defined as

![](https://learning.oreilly.com/library/view/computational-dynamics-3rd/9780470686157/figs/U02182.png)

def dfdq2(q,t):
    '''Here q=[q1,q2,q3] and t = time'''
    # your work here
    return df

Use your `dfdq2` to calculate $\frac{\partial \mathbf{f}}{\partial\mathbf{q}}$ when 

q=[1,3,5], and t=3

q=np.array([1,3,5])
t=3
dfdq2(q,t)

## Inverse of matrices

The inverse of a square matrix, $A^{-1}$ is defined such that

$A^{-1}A=I=AA^{-1}$

Not all square matrices have an inverse, they can be *singular* or *non-invertible*

The inverse has the following properties:

1. $(A^{-1})^{-1}=A$

2. $(AB)^{-1}=B^{-1}A^{-1}$

3. $(A^{-1})^{T}=(A^{T})^{-1}$

A=np.random.rand(3,3)
A

Ainv=inv(A)
inv(Ainv)

B=np.random.rand(3,3)

print(inv(np.dot(A,B)))
print('==')
print(np.dot(inv(B),inv(A)))

inv(A.T)

inv(A).T

### Orthogonal Matrices

Vectors are *orthogonal* if $x^{T}$ y=0, and a vector is *normalized* if $||x||_{2}=1$. A
square matrix is *orthogonal* if all its column vectors are orthogonal to each other and
normalized. The column vectors are then called *orthonormal* and the following results

$U^{T}U=I=UU^{T}$

and 

$||Ux||_{2}=||x||_{2}$

### Determinant

The **determinant** of a matrix has 3 properties

1\. The determinant of the identity matrix is one, $|I|=1$

2\. If you multiply a single row by scalar $t$ then the determinant is $t|A|$:

$t|A|=\left[ \begin{array}{cccc}
tA_{11} & tA_{12} &...& tA_{1N} \\
A_{21} & A_{22} &...& A_{2N} \\
\vdots & \vdots &\ddots& \vdots \\
A_{M1} & A_{M2} &...& A_{MN}\end{array} \right]$

## Determinant (con'd)
3\. If you switch 2 rows, the determinant changes sign:
$-|A|=\left[ \begin{array}{cccc}
A_{21} & A_{22} &...& A_{2N} \\
A_{11} & A_{12} &...& A_{1N} \\
\vdots & \vdots &\ddots& \vdots \\
A_{M1} & A_{M2} &...& A_{MN}\end{array} \right]$

## Determinant (con'd)
4\. inverse of the determinant is the determinant of the inverse:

$|A^{-1}|=\frac{1}{|A|}=|A|^{-1}$

## Calculating the Determinant
For a $2\times2$ matrix, 

$|A|=\left|\left[ \begin{array}{cc}
A_{11} & A_{12} \\
A_{21} & A_{22} \\
\end{array} \right]\right| = A_{11}A_{22}-A_{21}A_{12}$

For a $3\times3$ matrix,

$|A|=\left|\left[ \begin{array}{ccc}
A_{11} & A_{12} & A_{13} \\
A_{21} & A_{22} & A_{23} \\
A_{31} & A_{32} & A_{33}\end{array} \right]\right|=$

$A_{11}A_{22}A_{33}+A_{12}A_{23}A_{31}+A_{13}A_{21}A_{32}
-A_{31}A_{22}A_{13}-A_{32}A_{23}A_{11}-A_{33}A_{21}A_{12}$

For larger matrices, the determinant is more involved

### Special Case for determinants

The determinant of a diagonal matrix $|D|=D_{11}D_{22}D_{33}...D_{NN}$. 

Similarly, if a matrix is upper triangular (so all values of $A_{ij}=0$ when $j<i$), the
determinant is 

$|A|=\left|\left[ \begin{array}{cccc}
A_{11} & A_{12} &...& A_{1N} \\
0 & A_{22} &...& A_{2N} \\
0 & 0 &\ddots & \vdots \\
0 & 0 &...& A_{NN}\end{array} \right]\right|=A_{11}A_{22}A_{33}...A_{NN}$

![eqn](https://learning.oreilly.com/library/view/computational-dynamics-3rd/9780470686157/figs/UEQ212.png)

## Problem 5

Find the sum $A+B$, the determinants, $|A|$ and $|B|$,  trace\($A$\), and trace\($B$\)

![](https://learning.oreilly.com/library/view/computational-dynamics-3rd/9780470686157/figs/U02173.png)

# your work here