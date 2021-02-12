# Working with Python
__Content modified under Creative Commons Attribution license CC-BY 4.0,
code under BSD 3-Clause License © 2020 R.C. Cooper__



## Good coding habits
### naming folders and files

## [Stanford file naming best practices](https://library.stanford.edu/research/data-management-services/data-best-practices/best-practices-file-naming)

1. Include information to distinguish file name e.g. project name, objective of function, name/initials, type of data, conditions, version of file, 
2. if using dates, use YYYYMMDD, so the computer organizes by year, then month, then day
3. avoid special characters e.g. !, #, \$, ...
4. avoid using spaces if not necessary, some programs consider a space as a break in code use dashes `-` or underscores `_` or CamelCase

## Commenting your code

Its important to comment your code 

- what are variable's units,

- what the is the function supposed to do, 

- etc. 


def code(i):
    '''Example of bad variable names and bad function name'''
    m=1
    for j in range(1,i+1):
        m*=j;
    return m

code(10)

## Choose variable names that describe the variable

You might not have recognized that `code(i)` is meant to calculate the [factorial of a number](https://en.wikipedia.org/wiki/Factorial), 

$N!= N*(N-1)*(N-2)*(N-3)*...3*2*1$. 

For example, 

- 4! = 24

- 5! = 120

- 10! = 3,628,800

In the next block, we have rewritten `code` so the output is unchanged, but another user can read the code *and* help debug if there is an issue. 

A function is a compact collection of code that executes some action on its arguments. 

Once *defined*, you can *call* a function as many times as you want. When we *call* a function, we execute all the code inside the function. The result of the execution depends on the *definition* of the function and on the values that are *passed* into it as *arguments*. Functions might or might not *return* values in their last operation.   

The syntax for defining custom Python functions is:

```python
def function_name(arg_1, arg_2, ...):
    '''
    docstring: description of the function
    '''
    <body of the function>
```

The **docstring** of a function is a message from the programmer documenting what he or she built. Docstrings should be descriptive and concise. They are important because they explain (or remind) the intended use of the function to the users. You can later access the docstring of a function using the function `help()` and passing the name of the function. If you are in a notebook, you can also prepend a question mark `'?'` before the name of the function and run the cell to display the information of a function. 

Try it!

def factorial_function(input_value):
    '''Good variable names and better help documentation
     
    factorial_function(input_number): calculates the factorial of the input_number
    where the factorial is defined as N*(N-1)*(N-2)*...*3*2*1
    
    Arguments
    ---------
    input_value: an integer >= 0
    
    Returns
    -------
    factorial_output: the factorial of input_value'''
    
    factorial_output=1 # define 0! = 1
    for factor in range(1,input_value+1):
        factorial_output*=factor; # mutliply factorial_output by 1*2*3*...*N (factor)
    return factorial_output
         

factorial_function(4)

Defining the function with descriptive variable names and inputs helps to make the function much more useable. 

Consider the structure of a Python function:

```python
def factorial_function(input_value):
```
This first line declares that we are `def`-ining a function that is named `factorial_function`. The inputs to the line are given inside the parantheses, `(input_value)`. We can define as many inputs as we want and even assign default values. 

```python
    '''Good variable names and better help documentation
     
    factorial_function(input_number): calculates the factorial of the input_number
    where the factorial is defined as N*(N-1)*(N-2)*...*3*2*1'''
```
The next 4 lines define a help documentation that can be accessed with in a couple ways:

1. `?factorial_function`

2. `factorial_function?`

3. `help(factorial_function)`




factorial_function?

```python
    factorial_output=1 # define 0! = 1
```

This line sets the variable `factorial_output` to 1. In the next 2 lines we update this value based upon the mathematical formula we want to use. In this case, its $1*1*2*3*...*(N-1)*N$

```python
    for factor in range(1,input_value+1):
        factorial_output*=factor; # mutliply m by 1*2*3*...*N (factor)
```        

These two lines perform the computation that we set out to do. The `for`-loop is going to start at 1 and end at our input value. For each step in the `for`-loop, we will mulitply the factorial_output by the factor. So when we calculate 4!, the loop updates factorial_output 4 times:

1. i=1: factorial_output = $1*1=1$

2. i=2: factorial_output = $1*1*2=2$

3. i=3: factorial_output = $1*1*2*3=6$

4. i=4: factorial_output = $1*1*2*3*4=24$



```python
    return factorial_output
```

This final line in our function returns the calculated value, `factorial_output`. We can also return as many values as necessary on this line, 

for example, if we had variables: `value_1`, `value_2`, and `value_3` we could return all three as such,

```python
    return value_1,value_2,value_3
```

## Play with NumPy Arrays


In engineering applications, most computing situations benefit from using *arrays*: they are sequences of data all of the _same type_. They behave a lot like lists, except for the constraint in the type of their elements. There is a huge efficiency advantage when you know that all elements of a sequence are of the same type—so equivalent methods for arrays execute a lot faster than those for lists.

The Python language is expanded for special applications, like scientific computing, with **libraries**. The most important library in science and engineering is **NumPy**, providing the _n-dimensional array_ data structure (a.k.a, `ndarray`) and a wealth of functions, operations and algorithms for efficient linear-algebra computations.

In this lesson, you'll start playing with NumPy arrays and discover their power. You'll also meet another widely loved library: **Matplotlib**, for creating two-dimensional plots of data.

## Importing libraries

First, a word on importing libraries to expand your running Python session. Because libraries are large collections of code and are for special purposes, they are not loaded automatically when you launch Python (or IPython, or Jupyter). You have to import a library using the `import` command. For example, to import **NumPy**, with all its linear-algebra goodness, we enter:

```python
import numpy as np
```

Once you execute that command in a code cell, you can call any NumPy function using the dot notation, prepending the library name. For example, some commonly used functions are:

* [`np.linspace()`](https://docs.scipy.org/doc/numpy/reference/generated/np.linspace.html)
* [`np.ones()`](https://docs.scipy.org/doc/numpy/reference/generated/np.ones.html#np.ones)
* [`np.zeros()`](https://docs.scipy.org/doc/numpy/reference/generated/np.zeros.html#np.zeros)
* [`np.empty()`](https://docs.scipy.org/doc/numpy/reference/generated/np.empty.html#np.empty)
* [`np.copy()`](https://docs.scipy.org/doc/numpy/reference/generated/np.copy.html#np.copy)

Follow the links to explore the documentation for these very useful NumPy functions!

import numpy as np

## Creating arrays

To create a NumPy array from an existing list of (homogeneous) numbers, we call **`np.array()`**, like this:

np.array([3, 5, 8, 17])

NumPy offers many [ways to create arrays](https://docs.scipy.org/doc/numpy/reference/routines.array-creation.html#routines-array-creation) in addition to this. We already mentioned some of them above. 

Play with `np.ones()` and `np.zeros()`: they create arrays full of ones and zeros, respectively. We pass as an argument the number of array elements we want. 

np.ones(5)

np.zeros(3)

Another useful one: `np.arange()` gives an array of evenly spaced values in a defined interval. 

*Syntax:*

`np.arange(start, stop, step)`

where `start` by default is zero, `stop` is not inclusive, and the default
for `step` is one.  Play with it!


np.arange(4)

np.arange(2, 6)

np.arange(2, 6, 2)

np.arange(2, 6, 0.5)

`np.linspace()` is similar to `np.arange()`, but uses number of samples instead of a step size. It returns an array with evenly spaced numbers over the specified interval.  

*Syntax:*

`np.linspace(start, stop, num)`

`stop` is included by default (it can be removed, read the docs), and `num` by default is 50. 

np.linspace(2.0, 3.0)

len(np.linspace(2.0, 3.0))

np.linspace(2.0, 3.0, 6)

np.linspace(-1, 1, 9)

## Array operations

Let's assign some arrays to variable names and perform some operations with them.

x_array = np.linspace(-1, 1, 9)

Now that we've saved it with a variable name, we can do some computations with the array. E.g., take the square of every element of the array, in one go:

y_array = x_array**2
print(y_array)

We can also take the square root of a positive array, using the `np.sqrt()` function:

z_array = np.sqrt(y_array)
print(z_array)

Now that we have different arrays `x_array`, `y_array` and `z_array`, we can do more computations, like add or multiply them. For example:

add_array = x_array + y_array 
print(add_array)

Array addition is defined element-wise, like when adding two vectors (or matrices). Array multiplication is also element-wise:

mult_array = x_array * z_array
print(mult_array)

We can also divide arrays, but you have to be careful not to divide by zero. This operation will result in a **`nan`** which stands for *Not a Number*. Python will still perform the division, but will tell us about the problem.  

Let's see how this might look:

x_array / y_array

## Multidimensional arrays

### 2D arrays 

NumPy can create arrays of N dimensions.  For example, a 2D array is like a matrix, and is created from a nested list as follows:

array_2d = np.array([[1, 2], [3, 4]])
print(array_2d)

2D arrays can be added, subtracted, and multiplied:

X = np.array([[1, 2], [3, 4]])
Y = np.array([[1, -1], [0, 1]])

The addition of these two matrices works exactly as you would expect:

X + Y

What if we try to multiply arrays using the `'*'`operator?

X * Y

The multiplication using the `'*'` operator is element-wise. If we want to do matrix multiplication we use the `'@'` operator:

X @ Y

Or equivalently we can use `np.dot()`:

np.dot(X, Y)

### 3D arrays

Let's create a 3D array by reshaping a 1D array. We can use [`np.reshape()`](https://docs.scipy.org/doc/numpy/reference/generated/np.reshape.html), where we pass the array we want to reshape and the shape we want to give it, i.e., the number of elements in each dimension. 

*Syntax*
 
`np.reshape(array, newshape)`

For example:

a = np.arange(24)

a_3D = np.reshape(a, (2, 3, 4))
print(a_3D)

We can check for the shape of a NumPy array using the function `np.shape()`:

np.shape(a_3D)

Visualizing the dimensions of the `a_3D` array can be tricky, so here is a diagram that will help you to understand how the dimensions are assigned: each dimension is shown as  a coordinate axis. For a 3D array, on the "x axis", we have the sub-arrays that themselves are two-dimensional (matrices). We have two of these 2D sub-arrays, in this case; each one has 3 rows and 4 columns. Study this sketch carefully, while comparing with how the array `a_3D` is printed out above. 

<img src="../images/3d_array_sketch.png" style="width: 400px;"/> 

When we have multidimensional arrays, we can access slices of their elements by slicing on each dimension. This is one of the advantages of using arrays: we cannot do this with lists. 

Let's access some elements of our 2D array called `X`.

X

# Grab the element in the 1st row and 1st column 
X[0, 0]

# Grab the element in the 1st row and 2nd column 
X[0, 1]

##### Exercises:

From the X array:

1. Grab the 2nd element in the 1st column.
2. Grab the 2nd element in the 2nd column.

Play with slicing on this array:

# Grab the 1st column
X[:, 0]

When we don't specify the start and/or end point in the slicing, the symbol `':'` means "all". In the example above, we are telling NumPy that we want all the elements from the 0-th index in the second dimension (the first column).

# Grab the 1st row
X[0, :]

##### Exercises:

From the X array:

1. Grab the 2nd column.
2. Grab the 2nd row.

Let's practice with a 3D array. 

a_3D

If we want to grab the first column of both matrices in our `a_3D` array, we do:

a_3D[:, :, 0]

The line above is telling NumPy that we want:

* first `':'` : from the first dimension, grab all the elements (2 matrices).
* second `':'`: from the second dimension, grab all the elements (all the rows).
* `'0'`       : from the third dimension, grab the first element (first column).

If we want the first 2 elements of the first column of both matrices: 

a_3D[:, 0:2, 0]

Below, from the first matrix in our `a_3D` array, we will grab the two middle elements (5,6):

a_3D[0, 1, 1:3]

##### Exercises:

From the array named `a_3D`: 

1. Grab the two middle elements (17, 18) from the second matrix.
2. Grab the last row from both matrices.
3. Grab the elements of the 1st matrix that exclude the first row and the first column. 
4. Grab the elements of the 2nd matrix that exclude the last row and the last column. 

## NumPy == Fast and Clean! 

When we are working with numbers, arrays are a better option because the NumPy library has built-in functions that are optimized, and therefore faster than vanilla Python. Especially if we have big arrays. Besides, using NumPy arrays and exploiting their properties makes our code more readable.

For example, if we wanted to add element-wise the elements of 2 lists, we need to do it with a `for` statement. If we want to add two NumPy arrays, we just use the addtion `'+'` symbol!

Below, we will add two lists and two arrays (with random elements) and we'll compare the time it takes to compute each addition.

### Element-wise sum of a Python list

Using the Python library [`random`](https://docs.python.org/3/library/random.html), we will generate two lists with 100 pseudo-random elements in the range [0,100), with no numbers repeated.

#import random library
import random

lst_1 = random.sample(range(100), 100)
lst_2 = random.sample(range(100), 100)

#print first 10 elements
print(lst_1[0:10])
print(lst_2[0:10])

We need to write a `for` statement, appending the result of the element-wise sum into a new list we call `result_lst`. 

For timing, we can use the IPython "magic" `%%time`. Writing at the beginning of the code cell the command `%%time` will give us the time it takes to execute all the code in that cell. 

%%time
res_lst = []
for i in range(100):
    res_lst.append(lst_1[i] + lst_2[i])

print(res_lst[0:10])

### Element-wise sum of NumPy arrays

In this case, we generate arrays with random integers using the NumPy function [`np.random.randint()`](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/np.random.randint.html). The arrays we generate with this function are not going to be like the lists: in this case we'll have 100 elements in the range [0, 100) but they can repeat. Our goal is to compare the time it takes to compute addition of a _list_ or an _array_ of numbers, so all that matters is that the arrays and the lists are of the same length and type (integers).

arr_1 = np.random.randint(0, 100, size=100)
arr_2 = np.random.randint(0, 100, size=100)

#print first 10 elements
print(arr_1[0:10])
print(arr_2[0:10])

Now we can use the `%%time` cell magic, again, to see how long it takes NumPy to compute the element-wise sum.

%%time
arr_res = arr_1 + arr_2

Notice that in the case of arrays, the code not only is more readable (just one line of code), but it is also faster than with lists. This time advantage will be larger with bigger arrays/lists. 

(Your timing results may vary to the ones we show in this notebook, because you will be computing in a different machine.)

##### Exercise

1. Try the comparison between lists and arrays, using bigger arrays; for example, of size 10,000. 
2. Repeat the analysis, but now computing the operation that raises each element of an array/list to the power two. Use arrays of 10,000 elements. 

## Time to Plot

You will love the Python library **Matplotlib**! You'll learn here about its module `pyplot`, which makes line plots. 

We need some data to plot. Let's define a NumPy array, compute derived data using its square, cube and square root (element-wise), and plot these values with the original array in the x-axis. 

xarray = np.linspace(0, 2, 41)
print(xarray)

pow2 = xarray**2
pow3 = xarray**3
pow_half = np.sqrt(xarray)

## Introduction to plotting

To plot the resulting arrays as a function of the orginal one (`xarray`) in the x-axis, we need to import the module `pyplot` from **Matplotlib**.



import matplotlib.pyplot as plt

## Set up default plotting parameters

The default Matplotlib fonts and linewidths are a little small. Pixels are free, so the next two lines increase the fontsize and linewidth

plt.rcParams.update({'font.size': 22})
plt.rcParams['lines.linewidth'] = 3

The line `%matplotlib inline` is an instruction to get the output of plotting commands displayed "inline" inside the notebook. Other options for how to deal with plot output are available, but not of interest to you right now. 

We'll use the **pyplot** `plt.plot()` function, specifying the line color (`'k'` for black) and line style (`'-'`, `'--'` and `':'` for continuous, dashed and dotted line), and giving each line a label. Note that the values for `color`, `linestyle` and `label` are given in quotes.

#Plot x^2
plt.plot(xarray, pow2, color='k', linestyle='-', label='square')
#Plot x^3
plt.plot(xarray, pow3, color='k', linestyle='--', label='cube')
#Plot sqrt(x)
plt.plot(xarray, pow_half, color='k', linestyle=':', label='square root')
#Plot the legends in the best location
plt.legend(loc='best')

To illustrate other features, we will plot the same data, but varying the colors instead of the line style. We'll also use LaTeX syntax to write formulas in the labels. If you want to know more about LaTeX syntax, there is a [quick guide to LaTeX](https://users.dickinson.edu/~richesod/latex/latexcheatsheet.pdf) available online.

Adding a semicolon (`';'`) to the last line in the plotting code block prevents that ugly output, like `<matplotlib.legend.Legend at 0x7f8c83cc7898>`. Try it.

#Plot x^2
plt.plot(xarray, pow2, color='red', linestyle='-', label='$x^2$')
#Plot x^3
plt.plot(xarray, pow3, color='green', linestyle='-', label='$x^3$')
#Plot sqrt(x)
plt.plot(xarray, pow_half, color='blue', linestyle='-', label='$\sqrt{x}$')
#Plot the legends in the best location
plt.legend(loc='best'); 

That's very nice! By now, you are probably imagining all the great stuff you can do with Jupyter notebooks, Python and its scientific libraries **NumPy** and **Matplotlib**. We just saw an introduction to plotting but we will keep learning about the power of **Matplotlib** in the next lesson. 

If you are curious, you can explore all the beautiful plots you can make by browsing the [Matplotlib gallery](http://matplotlib.org/gallery.html).

##### Exercise:

Pick two different operations to apply to the `xarray` and plot them the resulting data in the same plot. 

## What we've learned

* Good coding habits and file naming
* How to define a function and return outputs
* How to import libraries
* Multidimensional arrays using NumPy
* Accessing values and slicing in NumPy arrays
* `%%time` magic to time cell execution.
* Performance comparison: lists vs NumPy arrays
* Basic plotting with `pyplot`.

## References

1. [Best practices for file naming](https://library.stanford.edu/research/data-management-services/data-best-practices/best-practices-file-naming). Stanford Libraries

1. _Effective Computation in Physics: Field Guide to Research with Python_ (2015). Anthony Scopatz & Kathryn D. Huff. O'Reilly Media, Inc.

2. _Numerical Python: A Practical Techniques Approach for Industry_. (2015). Robert Johansson. Appress. 

2. ["The world of Jupyter"—a tutorial](https://github.com/barbagroup/jupyter-tutorial). Lorena A. Barba - 2016

## Problems

1. Create a function called `sincos(x)` that returns two arrays, `sinx` and `cosx` that return the sine and cosine of the input array, `x`. 

    a. Document your function with a help file in `'''help'''`
    
    b. Use your function to plot sin(x) and cos(x) for x=$0..2\pi$




def sincos(x):
    '''sincos(x) returns both the sine and cosine of input x
    arguments:
    ---------
    x: input in radians
    outputs:
    -------
    sinx: sin(x)
    cosx: cos(x)'''
    # your code here, replace '''help''' with your documentation
    
    sinx=np.sin(x)
    cosx=np.cos(x)
    
    return sinx, cosx
    

x=np.linspace(0,2*np.pi)
y1,y2 = sincos(x)
plt.plot(x,y1,label='sin(x)')
plt.plot(x,y2,label='cos(x)')
plt.legend();

2. Use a for-loop to create a variable called `A_99`, where every element is the product
of the two indices from 0 to 9 e.g. A_99[3,2]=6 and A_99[4,4]=16. 

    a. time your script using `%%time`    
    
    b. Calculate the mean of `A_99`

    c. Calculate the standard deviation of `A_99`
    



%%time
A_99 = np.zeros((10,10))
for i in range(0,10):
    for j in range(0,10):
        A_99[i,j]=i*j

print('mean of A_99',np.mean(A_99))
print('stdev of A_99',np.std(A_99))

3. Use the two arrays, X and Y, given below to create A_99 using numpy array math rather than a for-loop. 

    a. time your script using `%%time`    
    
    b. Calculate the mean of `A_99`

    c. Calculate the standard deviation of `A_99`
        
    d. create a filled contour plot of X, Y, A_99 [contourf plot documentation](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.contourf.html)


# given X and Y arrays
X,Y=np.meshgrid(np.arange(0,10),np.arange(0,10))

%%time
A_99=X*Y
plt.contourf(X,Y,A_99)

4. The following linear interpolation function has an error. It is supposed to return y(x) given the the two points $p_1=[x_1,~y_1]$ and $p_2=[x_2,~y_2]$. Currently, it just returns and error.

def linInterp(x,p1,p2):
    '''linear interplation function
    return y(x) given the two endpoints 
    p1=np.array([x1,y1])
    and
    p2=np.array([x2,y2])'''
    slope = (p2[1]-p1[1])/(p2[0]-p1[0])
    
    return p1[1]+slope*(x - p1[0])
        

# test cases for linInterp
p1=np.array([0,1])
p2=np.array([2,2])
linInterp(1,p1,p2) # answer should be 1.5

p1=np.array([11,-3])
p2=np.array([12,-5])
linInterp(11.25,p1,p2) # answer should be -3.5

