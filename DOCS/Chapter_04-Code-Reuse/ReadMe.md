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


## Boolean ##
* `bool` : Python has a built-in function called `bool`, which return `True` or `False` based on the input provided.
* If an object evaluates to `0`, it is always `False`.
* A empty string, and empty list and an empty dictionary all evaluate to `False`.
* Python `None` value also evaluates to `False`.
* Critically all non-empty data structure evaluates to True.


## Function Return ##
* `return` : it is a keyword with which a Python function returns value to the caller.
* A function terminates at `return` statement.
* Function can also returns multiple values, like a list. Even in python we can return a tuple
* An empty set is represented by `set()` and not `{}` which is for a dictionary.

## Annotations ##
* The function we implemented till now, has no way of describing it's input parameter or the return type.
* The best way to do it, is to put it inside the docstring.
* Python 3 now supports annotations(type hints).
* The function annotations are optional and are only informational.
    - `def search4vowels(word: str) -> set:`
* The goal of annotations is to make it easier for the user.
* Annotations are a documentation standard and not a type enforcement mechanism.


## Bullet Points ##
* Function are a name given for a group of code.
* `def` keywords introduces a function.
* triple quote strings can be used for multi line comment or for function documentation called doc string.
* Function can accepts any number of arguments.
* The `return` statement helps in returning any number of values.
* Function annotations can be used to document the type of your function's argument and return type.


## Default Arguments ##
* Any arguments in a function call can be given default value, which will be used if the caller does not provide with that parameter while calling.
* We can assign default values by
    - `def search4letters(phrase: str, letters: str = "Hello") -> set:`


## Positional Vs Keyword Arguments. ##
* We can invoke a function by using key words arguments in-place of depending on the position while passing the values.
* The traditional way of passing arguments is called positional arguments.

## Bullet Points ##
* Functions help in reducing complexity of the code, by abstracting a piece of code into a function.
* Function can be provided with default values, which is used if that value is not passed while calling the function.
* Keywords arguments are a new way of passing values to a function. It use a key-value pair to pass the value.


## Modules ##
* Modules are an efficient way to distribute function.
* A file containing a function is a module.
* Python `import` statement helps in importing both standard modules and user defined.
* `import` statement search for a modules in a **search path**, if the module is not present in the search path it is difficult to import it.

### Module Import ###
* Python `import` statement search for a module in these path.
    - The current working directory.
    - The interpreter's site-packages directory.
    - The standard library location.
* Create a folder and create a python file with the name `vsearch.py`
    - cd to that folder and, open python terminal and give `import vsearch`. The module is imported.
* If we change the folder, there will be import error.
* Python `import` statement does not take path to a file.

### Site-packages ###
* `setuptools` is used to install site-packages.
    - It creates a distribution description.
    - Generate a distribution file.
    - Install the distribution file. 
















