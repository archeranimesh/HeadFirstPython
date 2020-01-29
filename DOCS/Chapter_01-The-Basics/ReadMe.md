# Chapter 01 | The Basics | Getting Started Quickly #


## Hello World ##

Hello world is the traditional way to start the first program in any programming language. In Python hello world can just be written as

````
print("Hello World")
````

Since it is this simple, we will start the journey of python with a meatier example.

````
from datetime import datetime

odds = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59,]

right_this_minute = datetime.today().minute

if right_this_minute in odds:
    print("This minutes seems a litte odd.")
else:
    print("Not an odd minute.")

````

### Python Imports ###


* Python execution starts from the first line in the file, python does not need any special function like `main()` to start execution.
* Python interpreter runs the code directly, there is no conversion to any intermediate form like in Java's `.class` file


Now lets be the Python Interpreter for the code we wrote above.

````
from datetime import datetime
````

* `import`s helps in brining some pre-existing software module already present in Python standard library to be used for our use the program.
* In the above we are importing a `datetime` submodule from a module named `datetime`.
* Python standard library is full with lot of reusable code, that is the reason it is called **batteries included**.
* Python community also supports third party modules.

### Data Structures ###

* Python have some very powerful built-in data structures. These built-in data structures provide additional functionality from anything present in other programming language.

#### List ####
List in python is denoted by `[]`, this is similar to array in other programming language, but have additional functionality.

* List in python can store heterogeneous data type and not limited with only homogeneous data type like in other programming language.

In the above example this line creates a list.

````
odds = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59,]
````

* `=` is called an **assignment operator**.
* Variables type need not be pre-defined in python, as it is a dynamically typed language.
* There is no special line character to signal end of line in python.


### Invoking Methods ###

Coming to the next line in the above code.

````
right_this_minute = datetime.today().minute
````

* `today()` is a function invoked on the submodule `datetime` which itself is part of the module `datetime`
* `today()` returns a time object, which conveys lot of information about current time.
* `.` **dot** operator helps in accessing this information returned by `today()`. we are using the `minute` attribute of current time.

To understand further we can split the above code into this.
````
this_now = datetime.today()
right_this_minute = this_now.minute
````

* Since we may not use the `this_now` variable in the future code, it is preferred in python not to create such temporary variable.


### Conditionals ###

* `in` is a special operator which checks if one thing is inside another.
* `in` returns `True` or `False`

````
if right_this_minute in odds:
    print("This minutes seems a little odd.")
else:
    print("Not an odd minute.")
````

* The `if` statement in the above code uses the `in` operator to check if `right_this_minute` value is inside `odds` value.
* Once it evaluates to `True` the first block of code is executed. `print("This minutes seems a little odd.")`
* The above code has two code block, and it can be easily identified as this is always indented.
* Python uses indentation to denote a block of code.
* `:`, the colon character, which denotes the start of block for control statements like `if, else, for`.
* Compiler raises an error if the next line following `:` is not right indented.
* Block of code can further be indented to show the different levels of code flow.
* `else` block is executed with the `if` condition evaluates to `false.`
    - Kindly note there is `:` just after `else`
* `elif` is also special else if condition, which check multiple conditions.

## Bullet Points ##

* The Python interpreter runs the code in the file from top to bottom, executing one line at a time. There is no notion of a `main()` function.
* Python come with a powerful standard library, which gives access of lots of reusable modules including third party.
* There is a collection of standard data structures available in Python with advanced functionality then other programming language. `list` being one of them.
* Python is dynamically typed language, as a result, variables need not be declared in advance with its type. As soon as we assign value to a variable it comes into existence.
* `if/elif/else` statements are decision making statements. These statements are followed by block of code which gets executed based on the conditions.
* Block of code are easy to be identified in Python as it is always indented.
* `:` colon, always signifies the start of block.


## Hello World Improved ##

We will try to better the above Hello World which we wrote. The improvements like make the code run multiple time, and sleep for a random time.

Python since is an REPL(READ, EVAL, PRINT, LOOP), every enhancement for a Python code can follow in these two approach. Though Python helps in the approach of experimentation.

* Experimentation
* Through design. 


### Loops ###

* The `for` loop is perfect for controlling looping when we know ahead of time how many iterations is needed.
    - `for i in [1, 2, 3]:`
* `while` is used when we do not know how many iterations in advance.
* `for` loop can iterate over any sequence, list, strings all are sequence.
    - A sequence is an ordered collection of objects.
* `for` loop does not need to be told how big the sequence is, they figure the length.
    - `for ch in "hello!":`
* `range()` function helps in generating a sequence of numbers on which `for` loop can iterate.
    - In most basic form `range()` accepts only one integer argument, telling how many times the loop will run.
    - `range()` actually takes 3 parameters
        + `start`: Number where `range ` starts
        + `stop`: Number where `range` ends
        + `step`: default is `1`, it defines for step to take.


### import ###
* `import` statement can be used in two ways.
    - `from datetime import datetime`
        + This imports a named function into our program's namespace.
        + This helps in importing without having to link the function back to the imported module.
        + If two module has same function in a different submodule, than this way of importing will cause namespace collation.
    - `import time`
        + This just imports the `time` module.
        + In this way we have to use the dot-notation syntax to access the module's functionality.
        + This module has a function called `sleep()`, which stops the execution of program for amount of time passed as argument.

### Random ###

* `dir()`: it displays all the attributes associated with anything in Python.
* `help()`: it gives Python documentation of related to the name.
* `random.randint()`: gives a random number between the given number.


## Bullet Points ##
* Python programmer favor experimenting with code snippets before giving the solution.
* The `for` loop can be used to iterate a fixed number of times.
    * If you know ahead of time how many times you need a loop, use `for` 
+ When you don't know ahead of time how often you're going to iterate, use Python `while` loop.
+ The `for` loop can iterate over any sequence, as well as execute a fixed number of times.
+ `sleep()` pauses the execution for the number of seconds passed as arguments.
+ `from time import sleep`: imports specific function `sleep` from `time` module.
+ `import time`: importing module we need to give the module name to call the function.
+ `random` has a good function called `randint` which gives a random integer within a specified range.
+ `dir()` and `help()` help in learning about Python function and module.
+ Negative numbers in `range()` last arguments changes the direction of range.

