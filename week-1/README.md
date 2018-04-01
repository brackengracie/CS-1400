# Print Function in Python
Coverage:
- Print() Function
- The python interpreter

```
>>> print("This is a literal string")
This is a literal string
>>> print('I can use double or single quotes')
I can use double or single quotes
>>> print(2+5)
7
>>> print(25*3+9)
84
>>> print("2+5")
2+5
>>> print('25*3+9')
25*3+9
```

# Expressions
Coverage:
- Operators
  - Add +, subtract -, multiply * , divide /
  - Exponents **
  - Negate -
- Order of operation PEMDAS

# Basic Python Function
Coverage:
- Syntax
  - Define the word Syntax
  - Keyword Def
  - Naming rules
  - Parenthesis
  - Colon and indentation
- Return statement
- Defining a Function vs. calling a Function
```
>>> def expression01():
               return 2+2

>>> print(expression01())
4
>>> def expression02():
              return 4/2-3

>>> print(expression02())
-1.0
>>> def expression03():
               return 2**8+5*4-22/11

>>> print(expression03())
274.0
```
The words def and return appear in orange because they are keywords in python. There are less than 40 keywords in python. Every Function must start with the word def. The word "expression01" is not a keyword and we could use a different word instead. It is always followed by Parenthesis and a colon.

A Function does not have to contain a return but all of the code that we will be using in code grinder does have a return. Any code following a colon has to be indented so that return is indented.
