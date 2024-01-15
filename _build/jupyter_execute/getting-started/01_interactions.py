#!/usr/bin/env python
# coding: utf-8

# # Interacting with Python
# 
# __Content modified under Creative Commons Attribution license CC-BY 4.0,
# code under BSD 3-Clause License © 2020 R.C. Cooper__

# These notebooks are a combination of original work and modified notebooks from [Engineers Code](https://github.com/engineersCode/EngComp.git) learning modules. The learning modules are covered under a Creative Commons License, so we can modify and publish *and give credit to L.A. Barba and N.C. Clementi*.
# 
# Our first goal is to interact with Python and handle data in Python.
# But let's also learn a little bit of background.

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


# ## What is Python?
# 
# Python was born in the late 1980s. Its creator, [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum), named it after the British comedy "Monty Python's Flying Circus." His goal was to create "an easy and intuitive language just as powerful as major competitors," producing computer code "that is as understandable as plain English."
# 
# We say that Python is a _general-purpose_ language, which means that you can use it for anything:  organizing data, scraping the web, creating websites, analyzing sounds, creating games, and of course _engineering computations_.
# 
# Python is an _interpreted_ language. This means that you can write Python commands and the computer can execute those instructions directly. Other programming languages—like C, C++ and Fortran—require a previous _compilation_ step: translating the commands into machine language.
# A neat ability of Python is to be used _interactively_. [Fernando Perez](https://en.wikipedia.org/wiki/Fernando_Pérez_(software_developer) famously created **IPython** as a side-project during his PhD. The "I" in IPython stands for interactive: a style of computing that is very powerful for developing ideas and solutions incrementally, thinking with the computer as a kind of collaborator. 

# ## Why Python?
# 
# 
# _Because it's fun!_ With Python, the more you learn, the more you _want_ to learn.
# You can find lots of resources online and, since Python is an open-source project, you'll also find a friendly community of people sharing their knowledge. 
# _And it's free!_
# 
# Python is known as a _high-productivity language_. As a programmer, you'll need less time to develop a solution with Python than with most other languages. 
# This is important to always bring up whenever someone complains that "Python is slow."
# Your time is more valuable than a machine's!
# (See the Recommended Readings section at the end of this lesson.)
# And if we really need to speed up our program, we can re-write the slow parts in a compiled language afterwards.
# Because Python plays well with other languages :–)
# 
# The top technology companies use Python: Google, Facebook, Dropbox, Wikipedia, Yahoo!, YouTube… Python took the No. 1 spot in the interactive list of [The 2017 Top Programming Languages](http://spectrum.ieee.org/computing/software/the-2017-top-programming-languages), by _IEEE Spectrum_ ([IEEE](http://www.ieee.org/about/index.html) is the world's largest technical professional society). 

# #### _Python is a versatile language, you can analyze data, build websites (e.g., Instagram, Mozilla, Pinterest), make art or music, etc. Because it is a versatile language, employers love Python: if you know Python they will want to hire you._ —Jessica McKellar, ex Director of the Python Software Foundation, in a [2014 tutorial](https://youtu.be/rkx5_MRAV3A).

# ## Let's get started
# 
# You could follow this first lesson using IPython. If you have it installed in the computer you're using, you enter the program by typing `ipython` on the command-line interface (the **Terminal** app on Mac OSX, and on Windows the **PowerShell** or a similar app). 
# A free service to try IPython online, right from your browser, is [Python Anywhere](https://www.pythonanywhere.com/try-ipython/). You can execute all the examples of this lesson in IPython using this service. 
# 
# You can also use Jupyter: an environment that combines programming with other content, like text and images, to form a "computational narrative." All of these lessons are written in Jupyter notebooks. 
# 
# For this lesson, we will assume you have been guided to open a blank Jupyter notebook, or are working interactively with this lesson. 
# On a blank Jupyter notebook, you should have in front of you the input line counter:
# 
# `In[1]:`
# 
# That input line is ready to receive any Python code to be executed interactively. The output of the code will be shown to you next to `Out[1]`, and so on for successive input/output lines in IPython, or code cells in Jupyter.

# ### Your first program
# 
# In every programming class ever, your first program consists of printing a _"Hello"_ message. In Python, you use the `print()` function, with your message inside quotation marks.

# In[2]:


print("Hello world!!")


# Easy peasy!! You just wrote your first program and you learned how to use the `print()` function. Yes, `print()` is a function: we pass the _argument_ we want the function to act on, inside the parentheses. In the case above, we passed a _string_, which is a series of characters between quotation marks. Don't worry, we will come back to what strings are later on in this lesson.  
# 
# ##### Key concept: function
# 
# A function is a compact collection of code that executes some action on its _arguments_.  Every Python function has a _name_, used to call it, and takes its arguments inside round brackets. Some arguments may be optional (which means they have a default value defined inside the function), others are required. For example, the `print()` function has one required argument: the string of characters it should print out for you.
# 
# Python comes with many _built-in_ functions, but you can also build your own. Chunking blocks of code into functions is one of the best strategies to deal with complex programs. It makes you more efficient, because you can reuse the code that you wrote into a function. Modularity and reuse are every programmer's friends.

# ### Python as a calculator
# 
# Try any arithmetic operation in IPython or a Jupyter code cell. The symbols are what you would expect, except for the "raise-to-the-power-of" operator, which you obtain with two asterisks: `**`. Try all of these:
# 
# ```python
# +   -   *   /   **   %   //
# ```
# 
# The `%` symbol is the _modulo_ operator (divide and return the remainder), and the double-slash is _floor division_.

# In[3]:


2 + 2


# In[4]:


1.25 + 3.65


# In[5]:


5 - 3


# In[6]:


2 * 4


# In[7]:


7 / 2


# In[8]:


2**3


# Let's see an interesting case:

# In[9]:


9**1/2


# ##### Discuss with your neighbor:
# _What happened?_ Isn't $9^{1/2} = 3$? (Raising to the power $1/2$ is the same as taking the square root.) Did Python get this wrong?
# 
# Compare with this:

# In[10]:


9**(1/2)


# Yes! The order of operations matters! 
# 
# If you don't remember what we are talking about, review the [Arithmetics/Order of operations](https://en.wikibooks.org/wiki/Arithmetic/Order_of_Operations). A frequent situation that exposes this is the following:

# In[11]:


3 + 3 / 2


# In[12]:


(3 + 3) / 2


# In the first case, we are adding $3$ plus the number resulting of the operation $3/2$. If we want the division to apply to the result of $3+3$, we need the parentheses.

# ##### Exercises:
# Use Python (as a calculator) to solve the following two problems:
# 
# 1. The volume of a sphere with radius $r$ is $\frac{4}{3}\pi r^3$. What is the volume of a sphere with diameter 6.65 cm?
# 
#     For the value of $\pi$ use 3.14159 (for now). Compare your answer with the solution up to 4 decimal numbers.
# 
#     Hint: 523.5983 is wrong and 615.9184 is also wrong.
#     
# 2. Suppose the cover price of a book is $\$ 24.95$, but bookstores get a $40\%$ discount. Shipping costs $\$3$ for the first copy and $75$ cents for each additional copy. What is the total wholesale cost for $60$ copies? Compare your answer with the solution up to 2 decimal numbers.
# 

# In[13]:


print('V of r=6.65-cm sphere ={:.4f} cm^3'.format(4/3*3.14159*(6.65/2)**3))
print('total cost of 60 copies =${:.2f}'.format(60*24.95*0.6+59*0.75+3))


# To reveal the answers, highlight the following line of text using the mouse:

# Answer exercise 1: <span style="color:white"> 153.9796 </span> Answer exercise 2: <span style="color:white"> 945.45 </span>

# In[14]:


945.45/60


# ### Variables and their type
# 
# Variables consist of two parts: a **name** and a **value**. When we want to give a variable its name and value, we use the equal sign: `name = value`. This is called an _assignment_. The name of the variable goes on the left and the value on the right. 
# 
# The first thing to get used to is that the equal sign in a variable assignment has a different meaning than it has in Algebra! Think of it as an arrow pointing from `name` to `value`.
# 
# 
# <img src="./images/variables.png" style="width: 400px;"/> 
# 
# We have many possibilities for variable names: they can be made up of upper and lowercase letters, underscores and digits… although digits cannot go on the front of the name. For example, valid variable names are:
# 
# ```python
#     x
#     x1
#     X_2
#     name_3
#     NameLastname
# ```
# Keep in mind, there are reserved words that you can't use; they are the special Python [keywords](https://docs.python.org/3/reference/lexical_analysis.html#keywords).
#   
# OK. Let's assign some values to variables and do some operations with them: 

# In[15]:


x = 3 


# In[16]:


y = 4.5


# ##### Exercise:
# Print the values of the variables `x` and `y`.

# In[ ]:





# Let's do some arithmetic operations with our new variables:

# In[17]:


x + y


# In[18]:


2**x


# In[19]:


y - 3


# And now, let's check the values of `x` and `y`. Are they still the same as they were when you assigned them?
# 

# In[20]:


print(x)


# In[21]:


print(y)


# ### String variables
# 
# In addition to name and value, Python variables have a _type_: the type of the value it refers to. For example, an integer value has type `int`, and a real number has type `float`. A string is a variable consisting of a sequence of characters marked by two quotes, and it has type `str`.
# 

# In[22]:


z = 'this is a string'


# In[23]:


w = '1'


#  What if you try to "add" two strings?

# In[24]:


z + w


# The operation above is called _concatenation_: chaining two strings together into one. Insteresting, eh? But look at this:  
# 
# `>> x + w`
# 
# _Error!_ Why? Let's inspect what Python has to say and explore what is happening. 
# 
# Python is a _dynamic language_, which means that you don't _need_ to specify a type to invoke an existing object. The humorous nickname for this is "duck typing":
# 
# #### "If it looks like a duck, and quacks like a duck, then it's probably a duck."
# 
# In other words, a variable has a type, but we don't need to specify it. It will just behave like it's supposed to when we operate with it (it'll quack and walk like nature intended it to).
# 
# But sometimes you need to make sure you know the type of a variable. Thankfully, Python offers a function to find out the type of a variable: `type()`.

# In[25]:


type(x)


# In[26]:


type(w)


# In[27]:


type(y)


# ### More assignments
# 
# Here we assign a new variable to the result of an operation that involves other variables.

# In[28]:


sum_xy = x + y
diff_xy = x - y


# In[29]:


print('The sum of x and y is:', sum_xy)
print('The difference between x and y is:', diff_xy)


# Notice what we did above: we used the `print()` function with a string message, followed by a variable, and Python printed a useful combination of the message and the variable value. This is a pro tip! You want to print for humans. Let's now check the type of the new variables we just created above:

# In[30]:


type(sum_xy)


# In[31]:


type(diff_xy)


# ## Reflection point
# When we created `sum_xy` and `diff_xy` two new variables were created that depended upon previously created variables `x` and `y`.  How else can we accomplish this? Could we make a function? Could we combine the commands in one block as a script?

# ### Special variables
# 
# Python has special variables that are built into the language. These are: 
# `True`, `False`, `None` and `NotImplemented`. 
# For now, we will look at just the first three of these.
# 
# **Boolean variables** are used to represent truth values, and they can take one of two possible values: `True` and `False`.
# _Logical expressions_ return a boolean. Here is the simplest logical expression, using the keyword `not`:
# 
# ```Python
#   not True
# ```
# 
# It returns… you guessed it… `False`.
# 
# The Python function `bool()` returns a truth value assigned to any argument. Any number other than zero has a truth value of `True`, as well as any nonempty string or list. The number zero and any empty string or list will have a truth value of `False`. Explore the `bool()` function with various arguments.
# 

# In[32]:


bool(0)


# In[33]:


bool('Do we need oxygen?')


# In[34]:


bool('We do need oxygen')


# **None is not Zero**: `None` is a special variable indicating that no value was assigned or that a behavior is undefined. It is different than the value zero, an empty string, or some other nil value. 
# 
# You can check that it is not zero by trying to add it to a number. Let's see what happens when we try that:

# In[35]:


a = None

b = 3


# ```python
# >>> a + b
# 
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-71-ca730b97bf8a> in <module>
# ----> 1 a+b
# 
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
# ```
# 

# ### Logical and comparison operators
# 
# The Python comparison operators are: `<`, `<=`, `>`, `>=`, `==`, `!=`. They compare two objects and return either `True` or `False`: smaller than, smaller or equal, greater than, greater or equal, equal, not equal. Try it!

# In[36]:


x = 3
y = 5


# In[37]:


x > y


# We can assign the truth value of a comparison operation to a new variable name:

# In[38]:


z = x > y


# In[39]:


z


# In[40]:


type(z)


# Logical operators are the following: `and`, `or`, and `not`. They work just like English (with the added bonus of being always consistent, not like English speakers!).  A logical expression with `and` is `True` if both operands are true, and one with `or` is `True` when either operand is true. And the keyword `not` always negates the expression that follows.
# 
# Let's do some examples:

# In[41]:


a = 5
b = 3
c = 10


# In[42]:


a > b and b > c


# Remember that the logical operator `and` is `True` only when both operands are `True`. In the case above the first operand is `True` but the second one is `False`. 
# 
# If we try the `or` operation using the same operands we should get a `True`. 

# In[43]:


a > b or b > c


# And the negation of the second operand results in …

# In[44]:


not b > c


# What if we negate the second operand in the `and` operation above?
# 
# ##### Note: 
# 
# Be careful with the order of logical operations. The order of precedence in logic is:
# 
# 1. Negation
# 2. And
# 3. Or
# 
# If you don't rememeber this, make sure to use parentheses to indicate the order you want. 

# ##### Exercise:
# 
# What is happening in the case below? Play around with logical operators and try some examples. 

# In[45]:


a > b and not b > c


# ## What we've learned
# 
# * Using the `print()` function. The concept of _function_.
# * Using Python as a calculator.
# * Concepts of variable, type, assignment.
# * Special variables: `True`, `False`, `None`.
# * Supported operations, logical operations. 
# * Reading error messages.

# ## References
# 
# Throughout this course module, we will be drawing from the following references:
# 
# 1. _Effective Computation in Physics: Field Guide to Research with Python_ (2015). Anthony Scopatz & Kathryn D. Huff. O'Reilly Media, Inc.
# 2. _Python for Everybody: Exploring Data Using Python 3_ (2016). Charles R. Severance. [PDF available](http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf)
# 3. _Think Python: How to Think Like a Computer Scientist_ (2012). Allen Downey. Green Tea Press.  [PDF available](http://greenteapress.com/thinkpython/thinkpython.pdf)

# ## Problems
# 
# 1. Calculate some properties of a rectangular box that is 12.5"$\times$11"$\times$14" and weighs 31 lbs
# 
#     a. What is the volume of the box?
#     
#     b. What is the average density of the box?
#     
#     c. What is the result of the following logical operation, `volume>1000` (in inches^3)
# 
# 
# 

# In[46]:


V = 12.5*11*14
rho = 31/V

print('volume = {} in^3\ndensity = {} lb/in^3\nVolume>1000 in^3 =={}'.format(V,rho,V>1000))


# 2. Use the variables given below, `str1` and `str2`, and check the following 
# 
#     a. `str1<str2`
#     
#     b. `str1==str2`
#     
#     c. `str1>str2`
#     
#     d. How could you force (b) to be true? [Hint](https://docs.python.org/3/library/stdtypes.html?highlight=str.lower#str.lower) or [Hint](https://docs.python.org/3/library/stdtypes.html?highlight=str.lower#str.upper)
# 

# In[47]:


str1='Computational Mechanics'
str2='computational mechanics'

print('a. ',str1<str2)
print('b. ',str1==str2)
print('c. ',str1>str2)
print('d. ',str1.lower()==str2.lower())


# 3. The following code has an error, fix the error so that the correct result is returned:
# 
# ```y is 20 and x is less than y```
# 
# ```python jupyter={"source_hidden": true}
# x=1
# y=20
# 
# if x<y and y==20:
#     print('y is 20 and x is less than y')
# else:
#     print('x is not less than y')
# ```
# 
# 4. Create a script that takes the clock hour in 24 hours and prints the clock hour with am or pm. 
# 
#     Hint: Use an if-else statement with `print` commands
# 

# In[48]:


test_time=10

if test_time<=12:
    print(test_time,':00 AM')
elif test_time>12:
    print(test_time-12,':00 PM')


# In[49]:


test_time=16
if test_time<=12:
    print(test_time,':00 AM')
elif test_time>12:
    print(test_time-12,':00 PM')


# 
