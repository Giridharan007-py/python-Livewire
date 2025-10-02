'''
# Python Dictionaries:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# dictionaries:

  * Dictionaries are used to store data values in key:value pairs.

  * A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

  * As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

  * Dictionaries are written with curly brackets, and have keys and values:

# Example: Create and print a dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# ADVERTISEMENT:'Dictionary Items'

  * Dictionary items are ordered, changeable, and do not allow duplicates.

  * Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

# Example:
"Print the "brand" value of the dictionary:"

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

# Ordered or Unordered ?
  * As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

  * When we say that dictionaries are ordered, it means that the items have a defined order
    and that order will not change.

  * Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.

# Changeable:
  * Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

# Duplicates Not Allowed:
  * Dictionaries cannot have two items with the same key:

# Example:
  * Duplicate values will overwrite existing values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

# Dictionary Length:
  * To determine how many items a dictionary has, use the len() function:

# Example:
  * Print the number of items in the dictionary:
         print(len(thisdict))

# Dictionary Items - Data Types:
  * The values in dictionary items can be of any data type:

# Example:
  * String, int, boolean, and list data types:

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
type()

  * From Python's perspective, dictionaries are defined as objects with the data type 'dict':
        <class 'dict'>

# Example:
  * Print the data type of a dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

# The dict() Constructor:
  * It is also possible to use the dict() constructor to make a dictionary.

# Example:

  * Using the dict() method to make a dictionary:

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
'''
# Python Collections (Arrays):
  * There are four collection data types in the Python programming language:

  * List is a collection which is ordered and changeable. Allows duplicate members.

  * Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

  * Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.

  * Dictionary is a collection which is ordered** and changeable. No duplicate members.

  * Set items are unchangeable, but you can remove and/or add items whenever you like.

  * As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

  * When choosing a collection type, it is useful to understand the properties of that type.
    Choosing the right type for a particular data set could mean retention of meaning, and,
    it could mean an increase in efficiency or security.

# Exercise:


Which one of these is a dictionary?


x = ('apple', 'banana', 'cherry')
x = {'type' : 'fruit', 'name' : 'banana'}
x = ['apple', 'banana', 'cherry']

 

# syntax:

name_of_the_dictionary={key1:value1,key2:value2,key3:value3}

  * {} - curly brackets
  * keys - The variable in left hand side of the object
  * values - the object which is assign to the variable





































dic={'name':'giri','age':17}
print(dic["age"])

dic['place']="chennai"  #adding
print(dic)
del dic['age']
print(dic)
print(list(dic))
print(sorted(dic))
print("age" in dic)
print("place" in dic)

a=dict([('bala',18),('siva',15),('bheem',6)])
print(a)

dicti={x:x**2 for x in (3,5,7)}
print(dicti)

a=dict(a=10,b=20,c=30)
print(a)

print(dic.keys())
print(dic.values()) 
'''










