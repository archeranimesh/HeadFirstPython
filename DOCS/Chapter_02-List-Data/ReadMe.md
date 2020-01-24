# Chapter 02 | List Data | Working with ordered data #

## Data and Processing ##
Programming is the job of working with data. We are inclined to know these with data.
* acquiring data
* processing data
* understanding data.

The first challenge to work with data is to store it efficiently. Python provides us with these options.
* **Lists**
* **Dictionaries**
* **Tuples**
* **Sets**

## Basic Data Type ##
We can use the basic data type, to work with single data value. 
Basic data types are:-
* **Numbers**
    - A variables takes the type from the values what is assigned.
    - `wait_time = random.randint(1,60)`
* **Strings**
    - Python dynamically assigns type to a variable.
    - `word = "bottles"`
* **Objects**
    - Everything is an object in Python.
    - Since objects can be assigned to variables, an interesting combination occurs in Python.
    - Objects have **state** (attributes and values) and **behavior** (methods).
    - Python's objected oriented programming is optional. We can still write programs in python without using classes.

## Built-in Data Structures. ##
Four Built-in Data Structures in Python, which means this is available as languages basic features without any export.
* **Lists** : an ordered mutable collection of objects
    - It is similar to array in other programming languages, with some added functionality.
    - It is zero indexed.
    - Lists are dynamic or mutable, that is it has APIs to manipulate the size/content of the lists.
    - Lists are also heterogeneous.
* **Tuples** : and ordered immutable collection of objects
    - It is an immutable list or it is a constant list.
    - Tuples are important when we send data to some function and do not expect it to be modified.
* **Dictionaries** : an unordered set of key/value pairs.
    - In other programming language, Dictionaries may be known as associative array, map, symbol or hash.
    - Each unique **key** has a value associated with it.
    - Dictionaries are unordered and mutable.
    - The ordering inside Dictionaries are random, we cannot expect that the order in which we inserted the data is the order in which it will come out.
* **Sets** : and unordered set of unique objects.
    - **Sets** helps in removing duplicates from data.
    - **Sets** are mutable and also unordered.

## List ##

* List is created using a `[]` brackets.
    - `odds = [1,3,5]`

### List Creation ###
* Empty list
    - `prices = []`
* List can contain heterogeneous data.
    - `car_details = ['Toyota', 'RAV4', 2.2, 60807]`
* List can contain list in itself.
    - `odds_and_ends = [[1,2,3], ['a', 'b', 'c'], ['One', 'Two', 'Three']]`

### List Operation ###
* `in` : Find a object inside a List
    - `'a' in 'aeiou'`
* `not in` : Check is a object is not inside a list.
* `append()` : Add an object to the end of the list.
* `remove()` : Takes an object's value and removes the first occurrence of the value.
    * It raises an error if the value is not present in the list.
* `pop()` : takes an optional index value as its arguments.
    * `pop` removes and returns and object from a list.
    * If no index value is specified it removes the last element of the list.
    * Calling `pop` on empty list raises error.
* `append()` : adds a single object to an existing list.
    - passing an empty list in appends, adds that empty list to the existing list.
* `extend()` : takes a list of object as its argument and adds each of its object to an existing list.   
    - No changes when an empty list is passed in `extend`.
* Both `extend()` and `append()` add elements to the end of the list.
* `insert()` : takes an index value and an object as its arguments.

## Bullet Point ##
* List is a great way of storing a collection of related objects.
* List are very similar to array in other languages, but with added functionality, list in python can be extended.
* List is denoted by square brackets, with items separated by comma. `[}`
* An empty list is represented by `[]`.
* `in` operator helps in identifying if an element is present in the list.
* Due to methods like `append()`, `extend()`, `insert()` and `remove()` we can add and remove elements from list.



