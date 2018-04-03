# Slicing
Coverage:
- start and stop str[start:stop]
- default start str[:stop]
- default stop str[:start]
- default start stop str[:]
- step str[start:stop:step]
- just step str[::step]
- slicing lists
- slicing strings

Slicing Strings:

```
mystr = slicing-py
```
- 1.1 Index: A simple slice is an index or just a single item which you have already done.
```
print(mystr[4])
i
```
- 1.2 A slice with a start and going up to but not including the final position
```
print(mystr[3:6])
cin
```
- 1.3 A slice with a start, stop, and step
```
print(mystr[1:8:2])
icn-
```
- 1.4 DEFAULT settings: when you don't enter numbers, the default settings apply. The default start is 0. The default stop is the length of the object you are attached to and the default step is 1.
```
print(mystr[0:len(mystr:1])
slicing-py
print(mystr[::])
slicing-py
```
slicing lists:
Lists can also be sliced the same as strings.
```
mylist = [1,3,2,4,6,4,3]
print(mylist[1:5:2])
[3,4]
```
# adjacent items in list and strings
print all the numbers that directly follow a 13 in the list
```
def lucky13(nums):
  for i in range(len(nums)-1):
    if nums[i] == 13:
      print(nums[i+1], end = "")
lucky13([0,13,4,33,14,13,3,13])
[4,3]
```
find number of occurrences of q followed by a u in a string
```
def find_qus(str):
  count = 0
  for i in range(len(str)-1):
    if str[i] == 'q' and str[i+1] == 'u':
      count = count + 1
  return count
print(find_qus("The queen was quietly making a quilt"))
3
```
total all the numbers in the list except numbers right after a 7
```
def hungry7(nums):
  total = nums[0]
  for i in range(1, len(nums)):
    if nums[i-1] != 7:
      total = total + nums[i]
  return total
print(hungry7([77,3,7,4,6,7,4,7,5,7]))
41
```
# Break and Pass
```
def instructions():
  Pass # I just want to remind myself to fill code later

def another_while_loop():
  instructions()
  while true:
    print("play or quit? (p/q): ")
    ans = input()
    if and == 'q':
      Break
      print("play Play play")
    print("goodbye")
```





# IN CLASS
(Reverse a string):
```
lst[::-1]

xstr =  "CS1410 NEXT FALL"
xstr[4] -> '1'
xstr[-1] -> 'L'
xstr[1:4] -> 'S14'
xstr[0:6:2] -> 'C11'
xstr[0:16:1] -> 'CS1410 NEXT FALL'
xstr[::-1] -> 'LLAF TXEN 0141SC'

def slice(xstr,st,en):
  result = ""
  for i in range(st,en):
    result += xstr[i]
  return result
```
or
```
def slice(xstr,st,en):
  return xstr[st:en]

def fun(xstr,pos,char):
  result = ""
  for i in range(pos-1):
    result += xstr[i]
result += char
for i in range(pos+1,len(xstr)):
  result += xstr[i]
return result
```
or
```
def fun(xstr,pos,char):
  return xstr[:pos]+char+xstr[pos+1]

flag = true
while flag:
  name = input("name -> ")
  if name = "end":
    flag = false

name = input("name ->")
while name != "end"
  name = input("name ->")

while true:
  name = input("name ->")
  if name = "end"
    break
```
