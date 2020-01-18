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

* `=` is called an **assignment operator.
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







