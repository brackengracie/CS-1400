Python 3.6.4 (v3.6.4:d48ecebad5, Dec 18 2017, 21:07:28) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> a=7
>>> b=a*3
>>> print (b)
21
>>> length=6
>>> width=4
>>> def area(length,width) :
	area=length*width
	return area
>>> print (area(length,width))
SyntaxError: invalid syntax
>>> print (area(length,width))
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print (area(length,width))
NameError: name 'area' is not defined
>>> for i in range (10) :
	print("hello")

	
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
>>> length=6
>>> width=4
>>> def area(length,width) :
	area=length*width
	return(area)

>>> print(area(length,width))
24
>>> if (a<b) :
	print("a<b")

	
a<b
>>> if (a<b) :
	print("Less")
	else
	
SyntaxError: invalid syntax
>>> 
>>> if a<b:
	print("less")

	
less
>>> if a<b:
	print("less")
else:
	print("Greater")

	
less
>>> x=5
>>> y=2.5
>>> word="elephant"
>>> z=5*(2+3)
>>> ans=x*y+z-2
>>> print(ans)
35.5
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
>>> def parameters1(x,y) :
	return(x,y)

>>> def parameters2(a,b) :
	return(a>=b)

>>> print(parameter1(3,4))
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    print(parameter1(3,4))
NameError: name 'parameter1' is not defined
>>> print(parameters1(3,4))
(3, 4)
>>> def function1() :
	x=4
	if x==3
	
SyntaxError: invalid syntax
>>> def function() :
	if x==3:
		print("thats my fav number")
	if x==5:
		print("you are a winner")
	else:
		print("you lose")
	function1()

	
>>> function1()
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    function1()
NameError: name 'function1' is not defined
>>> function()
you are a winner
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    function()
  File "<pyshell#75>", line 8, in function
    function1()
NameError: name 'function1' is not defined
>>> 
>>> function()
you are a winner
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    function()
  File "<pyshell#75>", line 8, in function
    function1()
NameError: name 'function1' is not defined
>>> for num in range(101) :
	total=0

	
>>> def adder(num) :
	total=0
	for i in range(num+1) :
		total=total+i
		return(total)

	
>>> total
0
>>> 100
100
>>> def adder(num) :
	total=0
	for i in range(num+1)
	
SyntaxError: invalid syntax
>>> print(adder(100))
0
>>> def adder(num) :
	total=0
	for i in range(num+1)
	
SyntaxError: invalid syntax
>>> def adder(num) :
	total=0
	for i in range(num+1) :
		total=total+1
	return total

>>> print(adder(100))
101
>>> 
