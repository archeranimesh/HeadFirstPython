# Chapter 04 | Code Reuse | Function and Modules #

## Functions ##

* Python supports **modularity**, i.e. to break down big chunk of code into smaller, more manageable pieces called **functions.**
* Functions introduces 2 new keywords: `def` and `return`.
* Functions can accept argument data, which acts a input to the function.
* Functions also like in general Python language are not aware of argument types.
* Python 3 does support indicating the type of argument and return value, but this is not make to do type checking.
* `def` : def is used to create a function.

````
def search4vowels():
    """ Display any vowel found in an asked-for word. """
    vowels = set("aeiou")
    word = input("Provide a word to search for vowels: ")
    found = vowels.intersection(set(word))
    for vowels in found:
        print(vowels)
````
* `def`: starts with the keyword.
* `search4vowels` : a meaningful name for the function.
* `()` : an empty argument list.
* `:` : at the end signifies a block of code is starting.
* `search4vowels()` : we can invoke the function just like this.
* `""" Hello """` : triple quotes can be used to provide a documentation to Python function.
* Python strings can be created using 3 ways.
    - `''` : use single quote.
    - `""` : use double quote.
    - `"""` : use triple quote.
        + The triple quote is called **docstrings**. Their main purpose is to provide documentation in Python.
        + It can span multiple lines.


## PEP 8 ##
* Python provides best practices for formating code. It is called **PEP 8**.
* PEP 8 : Python Enhancement Protocol.
* PEP 8 is the style guide for Python code.
* PEP 257 : Offers documentation on how to format docstring.

## Function Arguments ##
* Function arguments can be provided by giving argument's name within `()`.
* This arguments then becomes variable in the function name.
* Python function can take multiple arguments, we can pass multiple arguments if it is comma separated.


## Function Return ##
* `return` : it is a keyword with which a Python function returns value to the caller.
* A function terminates at `return` statement.

## Boolean ##
* `bool` : Python has a built-in function called `bool`, which return `True` or `False` based on the input provided.
* If an object evaluates to `0`, it is always `False`.
* A empty string, and empty list and an empty dictionary all evaluate to `False`.
* Python `None` value also evaluates to `False`.
* Critically all non-empty data structure evaluates to True.


