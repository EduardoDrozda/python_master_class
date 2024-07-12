# Integer
x = 1
print("Integer: ", x)

# Float
y = 1.0
print("Float: ", y)

print("Type of x: ", type(x))
print("Type of y: ", type(y))

# SUM
z = x + y
print("Sum: ", z)

# Division
z = x / y
print("Division: ", z)

# Multiplication
z = x * y
print("Multiplication: ", z)

# Subtraction
z = x - y
print("Subtraction: ", z)

# Exponentiation
z = x ** y
print("Exponentiation: ", z)

# Modulus
z = x % y
print("Modulus: ", z)

# Floor division
z = x // y
print("Floor division: ", z)

# Numer methods

# Absolute
# Returns the absolute value of a number

x = -1
z = abs(x)
print("Absolute: ", z)

# Round
# Rounds a number to the nearest integer

x = 1.5
z = round(x)

print("Round: ", z)


# String

# Single quotes
# Single quotes are used when the string contains double quotes

a = 'Hello, World!'
print("Single quotes: ", a)

# Double quotes
# Double quotes are used when the string contains single quotes

a = "Hello, World!"
print("Double quotes: ", a)

# Triple quotes
# Triple quotes are used when the string is spread over multiple lines

a = '''Hello, World!'''

# String concatenation
a = "Hello"
b = "World"
c = a + b
print("String concatenation: ", c)

# String multiplication
a = "Hello"
b = 3

c = a * b
print("String multiplication: ", c)

# String methods

# Capitalize
# Converts the first character to upper case

a = "hello, world!"

c = a.capitalize()
print("Capitalize: ", c)

# Casefold
# Converts string into lower case

a = "Hello, World!"

c = a.casefold()

print("Casefold: ", c)

# Center

# Returns a centered string

a = "Hello, World!"
b = 20

c = a.center(b)

print("Center: ", c)

# Count
# Returns the number of times a specified value occurs in a string

a = "Hello, World!"
b = "o"

c = a.count(b)

print("Count: ", c)

# Encode

# Returns an encoded version of the string

a = "Hello, World!"

c = a.encode()

print("Encode: ", c)

# Endswith

# Returns true if the string ends with the specified value

a = "Hello, World!"

c = a.endswith("d")

print("Endswith: ", c)

# Expandtabs

# Sets the tab size of the string

a = "Hello, World!"

c = a.expandtabs(2)

print("Expandtabs: ", c)

# Lists

# A list is a collection which is ordered and changeable. In Python lists are written with square brackets.

# Create a List:

thislist = ["apple", "banana", "cherry"]

print(thislist)

# Access Items

# You access the list items by referring to the index number:

thislist = ["apple", "banana", "cherry"]

print(thislist[1])

# Negative Indexing
print(thislist[-1])

# Change Item Value

# To change the value of a specific item, refer to the index number:

thislist = ["apple", "banana", "cherry"]

thislist[1] = "blackcurrant"

print(thislist)

# Loop Through a List

# You can loop through the list items by using a for loop:

thislist = ["apple", "banana", "cherry"]

for x in thislist:
    print(x)

#Loop through index
# Loop Through the Index Numbers

# You can also loop through the list items by referring to their index number. Use the range() and len() functions:

thislist = ["apple", "banana", "cherry"]

for i in range(len(thislist)):
    print(thislist[i])
    
    
# Print all items by referring to their index number:
thislist = ["apple", "banana", "cherry"]
print(thislist[1:3])
# Check if Item Exists

# To determine if a specified item is present in a list use the in keyword:

thislist = ["apple", "banana", "cherry"]

if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")
    
# List Length

# To determine how many items a list has, use the len() method:

thislist = ["apple", "banana", "cherry"]

print(len(thislist))

# Add Items

# To add an item to the end of the list, use the append() method:

thislist = ["apple", "banana", "cherry"]

thislist.append("orange")

print(thislist)

# To add an item at the specified index, use the insert() method:

thislist = ["apple", "banana", "cherry"]

thislist.insert(1, "orange")

print(thislist)

# Remove Item

# There are several methods to remove items from a list:

# The remove() method removes the specified item:

thislist = ["apple", "banana", "cherry"]

thislist.remove("banana")

print(thislist)

# The pop() method removes the specified index, (or the last item if index is not specified):

thislist = ["apple", "banana", "cherry"]

thislist.pop()

print(thislist)

# The del keyword removes the specified index:

thislist = ["apple", "banana", "cherry"]

del thislist[0]

print(thislist)

# The del keyword can also delete the list completely:

thislist = ["apple", "banana", "cherry"]

del thislist

# The clear() method empties the list:

thislist = ["apple", "banana", "cherry"]

thislist.clear()

print(thislist)

# Copy a List

# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

# There are ways to make a copy, one way is to use the built-in List method copy().
# Make a copy of a list with the copy() method:

thislist = ["apple", "banana", "cherry"]

mylist = thislist.copy()

print(mylist)

# Another way to make a copy is to use the built-in method list().

# Make a copy of a list with the list() method:

thislist = ["apple", "banana", "cherry"]

mylist = list(thislist)

print(mylist)

# Join Two Lists

# There are several ways to join, or concatenate, two or more lists in Python.

# One of the easiest ways are by using the + operator.

# Join two list:

list1 = ["a", "b", "c"]

list2 = [1, 2, 3]

list3 = list1 + list2

print(list3)

# Another way to join two lists are by appending all the items from list2 into list1, one by one:

# Append list2 into list1:

list1 = ["a", "b", "c"]

list2 = [1, 2, 3]

for x in list2:
    list1.append(x)
    
print(list1)

# Tuple

# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

# Create a Tuple:

thistuple = ("apple", "banana", "cherry")

print(thistuple)

# Access Tuple Items

# You can access tuple items by referring to the index number, inside square brackets:

thistuple = ("apple", "banana", "cherry")

print(thistuple[1])

# Negative Indexing

# Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.

thistuple = ("apple", "banana", "cherry")

print(thistuple[-1])

# Range of Indexes

# You can specify a range of indexes by specifying where to start and where to end the range.

# When specifying a range, the return value will be a new tuple with the specified items.

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print(thistuple[2:5])

# Change Tuple Values

# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

# Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")

y = list(x)

y[1] = "kiwi"

x = tuple(y)

print(x)

# Loop Through a Tuple

# You can loop through the tuple items by using a for loop.

thistuple = ("apple", "banana", "cherry")

for x in thistuple:
    print(x)
    
# Check if Item Exists

# To determine if a specified item is present in a tuple use the in keyword:

thistuple = ("apple", "banana", "cherry")

if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")
    
# Tuple Length

# To determine how many items a tuple has, use the len() method:

thistuple = ("apple", "banana", "cherry")

print(len(thistuple))

# Add Items

# Once a tuple is created, you cannot add items to it. Tuples are unchangeable.

# Create a new tuple with the value you want to add:

thistuple = ("apple", "banana", "cherry")

y = list(thistuple)

y.append("orange")

thistuple = tuple(y)

print(thistuple)

# Remove Items

# Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:

# Convert the tuple into a list, remove "apple", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")

y = list(thistuple)

y.remove("apple")

thistuple = tuple(y)

print(thistuple)

# The del keyword can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")

del thistuple

# The tuple() Constructor

# It is also possible to use the tuple() constructor to make a tuple.

thistuple = tuple(("apple", "banana", "cherry"))  # note the double round-brackets

print(thistuple)

# Set

# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.

# Create a Set:

thisset = {"apple", "banana", "cherry"}

print(thisset)

# Access Items

# You cannot access items in a set by referring to an index, since sets are unordered the items has no index.

# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

# Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)
    
# Check if "banana" is present in the set:

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)


# Dictionary

# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

# Create and print a dictionary:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict)

# Accessing Items

# You can access the items of a dictionary by referring to its key name, inside square brackets:

x = thisdict["model"]

# There is also a method called get() that will give you the same result:

x = thisdict.get("model")

# Change Values

# You can change the value of a specific item by referring to its key name:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict["year"] = 2018

# Loop Through a Dictionary

# You can loop through a dictionary by using a for loop.

# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

# Print all key names in the dictionary, one by one:

for x in thisdict:
    print(x)
    
# Print all values in the dictionary, one by one:

for x in thisdict:
    print(thisdict[x])
    
# You can also use the values() function to return values of a dictionary:

for x in thisdict.values():
    print(x)
    

# Loop through both keys and values, by using the items() function:

for x, y in thisdict.items():
    print(x, y)
    
# Check if Key Exists

# To determine if a specified key is present in a dictionary use the in keyword:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
    
# Dictionary Length

# To determine how many items (key-value pairs) a dictionary has, use the len() method.

print(len(thisdict))

# Adding Items

# Adding an item to the dictionary is done by using a new index key and assigning a value to it:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}


