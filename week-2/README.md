# Variables
Coverage:
- Naming rules
  - Letters, numbers, underscore
  - No spaces, no symbols, no keywords, can't start with a number
- Assignment Operator =
- Left to right
  - 5 + 5 = x is a Syntax error
- literal values integers, float, string
- Incrementing Variables

Code Level Understanding Examples:

In python you create a variable when you assign a value to it. One way this can happen is with a equals statement.

```
>>> x=5
>>> y=2.5
>>> word="Elephant"
>>> z=5*(2+3)
>>> ans=x*y+z-2
>>> print(ans)
35.5
```

Incrementing and Decrementing variable:
```
>>> x=3
>>> x=x+1
>>> print(x)
4
>>> x=x-1
>>> print(x)
3
>>> x=x+1
>>> x=x+1
>>> print(x)
5
```

# Parameter Variables in Functions
Coverage:
- Variable name in the Parenthesis of a Function
- assigned values from the Function call
Code Level Understanding Examples:
```
>>> def parameters1(x,y):
               return x*y

>>> def parameters2(a,b):
               return a>=b

>>> print(parameters1(3,4))
12
>>> print(paramters1(5,2))
Traceback (most recent call last):
File "<pyshell#56>", line 1, in <module>
print(paramters1(5,2))
NameError: name 'paramters1' is not defined
>>> print(parameters1(5,2))
10
>>> print(parameters2(3,3))
True
>>> print(parameters2(2,5))
False
>>> #Notice how you can call functions multiple times with
>>> #different parameters. This is how code grinder tests your code.
```

# Python Comparison Operators
Coverage:
- Equals = , Less than < , Greater than > , not equal to !=
- Boolean values (true or false)
Code level Understanding Examples:
```
>>> print((5+5)==(20-120))
False
>>> print((20/5+3)>=4)
True
>>> print(3>(21/7))
False
>>> print(True==1)
True
>>> print(False==0)
True
```

# Simple Conditional:
Coverage:
- Syntax
  - Keyword if, condition using comparison, colon
  - Keyword else, no condition, colon
- Define control flow
  - If true do one thing, else do the other thing
Code level Understanding Examples:
```
def function1():
    x=4
    if x==3:
        print("That is my favorite number!")
    if x==5:
        print("You are a winner!")
    else:
        print("You lose.")
```

The python language strictly requires indention. Every line that occurs after a colon has to be indented. So far we have seen that a Function definition always ends with a colon. For example:
```
def function1():
```
An if statement also is always followed by a colon as well as an else. There can only be on else statement per if statement and it is attached to the if statement by indention. An if statement is followed by an expression and then the colon.

# Repeating Code
Coverage:
- Keyword For
- Range() Function with one parameter
- incremented variable
  - using variable value loop
- print something x times
- collect a total using a variable
This is an introduction to one use for a for-loop. As the course continues, we will introduce more ways in which a for-loop can be used. Noticed in the following code that i is not in orange. That is because i is a variable name and could be called anything. The keywords are for and in. The word in purple is range. it is python function. That is all that you need to know for now. We will go into more detail later.
Code level Understanding:
```
for i in range(3):

for count in range(5):

for i in range(num):

Look at the following code and make sure that you understand how it works. It is simply printing the word the number of times declared in the range.

>>> for i in range(3):
               print("Hello")

Hello
Hello
Hello
```

# Totaling numbers in a for-loop
You have been introduced to a for-loop and to the concept of incrementing a variable. We are now going to combine those two concepts. Let's say that we want to introduce the concept of multiplication. We have 3 groups of 5 pennies. We want to teach the kids to add the 3 groups together. We tell them to add 5 + 5 + 5 to get a total of 15. How could we write a program that would do a similar concept?
```
def simpleMultiply():
        total=0
        for i in range(3):
                total=total+5
        return total
print(simpleMultiply())
5
```
The numbers 3 and 5 were given to you in this example. They could be replaced by variables.
