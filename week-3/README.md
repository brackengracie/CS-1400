# String-2
Coverage:
- Text is called strings
- Characters surrounded by quotes
- Double or single quotes
- Concatenation, adding strings
Code level Understanding:
```
>>> print("Strings shouldn't be hard to understand")
Strings shouldn't be hard to understand
>>> print('Python is "easy" to learn')
Python is "easy" to learn
>>> first_name="John"
>>> last_name="Doe"
>>> full_name=first_name + " " + last_name
>>> print(full_name)
John Doe
```

# Intro to lists
Coverage:
- Store multiply values in one place
- Initialize an empty list
- Initialize a non empty list
- Add items to list with append()
- Len() function return how many items in a list
- Indexing values starting at zero
  - Last legal index value
- use a for loop and indexing to read contents for a list
Code level understanding:
my_list = []  # makes an empty list                        
my_list = [1,3,5,7] # Creates a list of 4 odd numbers
Indexing a list:
A list in python is always ordered starting with 0.

To print out what is at index 1 you would use the following command:
```
print (mylist[1])
```
In code grinder you will be asked to return what is at a specific position. You can do that the same way. For example if you were asked to return what was at index 3 you would write:
```
return mylist[3]
```
Changing a list item at a determined index:
To change the list at index 2 from 5 to 3 you would do the following:
```
mylist[2] = 3
```
EXAMPLE:
```
scores = [90, 89, 78, 87, 98, 95, 72, 62]
people = ["Allen", "Bob", "Cindy", "David", "Evan", "Frank", "Gina","Mark"]
print(scores[0]) # 90
print(people[4]) # Evan
print(people[len(people)-1])
for i in range(len(scores)):
        print(people[i], "received a ", scores[i], "percent.")
total = 0
for i in range(len(scores)):
        total = total + scores[i]

songs = []
songs.append("Happy")
songs.append("Hello")
songs.append("Sugar")
print(len(songs))
print(songs[1]) # Hello
```

# Determining the length of a list
We can use the len() function to determine the length of a list.
```
print(len(mylist))
```
The len(mylist) returns 4. There are 4 items in the list. This can get confusing because the indexes start at 0 and go to 3 while the number of items in the list start counting at 1 and go to 4.
Using Len() to access to end of the list:
If we wanted to print the last item in the list we could say:
```
print(mylist[3])   
```
But what if we didn't know how long the list was? How could we print out the last item in the list?
```
print(mylist[len(mylist)-1])
```
Since the len(mylist) will return 4 we have to subtract 1 to get to the index of 3 which is where the last item is located.

# Getting input from the user
We have seen the print function and now we are going to introduce the input function. Both of these functions will not be used in code grinder as they are for user interaction. You will need the input and print functions to complete the homework assignments.

1) The input() function simply waits for the user to enter information and hit the enter/return key.
```
input()  
```
2) This is not very exciting. For example, how does the user know that they are supposed to enter their name? Perhaps the following code would be helpful.
```
print("Enter your name")
input()
```
3) Now the computer prompts the user to enter their name so the user does. However, the computer is not storing that data and the name simply disappears into cyberspace. This is not very helpful. After all if we are asking for information, then we probably want to use it which means that we need to store it somewhere. That means that we need to create a variable. Thus the following code makes sense:
```
print("Enter your name: ")
name = input()
```
4) Since we nearly always are going to prompt the user - meaning we usually want to print something indicating what we want the user to do - we decided to put the prompt inside the parenthesis as follows:
```
name = input("Enter your name:  ")
```
Code level Understanding:
Let's say that we want the user to enter the number of times they print hello. We use the int() function to change the string to an integer. The following code would work.
```
def printHello():
        stringNum=input("Enter a number: ")
        num = int(stringNum)
        for i in range(num):
                print("Hello")
printHello()
```
# Main() function
Coverage:
- Common convention in programming to start a program by calling a "main" function
- call other function from Main
Code level understanding:
```
def do_stuff():
        return "stuff"

def do_more_stuff():
        return "more stuff"

def main():
        # call other functions here
        print(do_stuff())
        print(do_more_stuff())

main()
```
