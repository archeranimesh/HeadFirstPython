# Chapter 11 | Exception Handling | What to do when things go wrong #

## Introduction ##
* Our Code should handle grace fully if things goes south in our code.
* In our web application we have to considers these conditions
    - What happens if the database connection fails?
        + `InterfaceError` is raised when DB Connection fails.
    - Our SQL Statements are protected from SQl Injection?
        + There are 2 main attack vectors
            * **SQL Injection** *(SQLi)*
                - We used the Parameterized SQL strings to protect against this.
            * **Cross-site scripting** *(XSS)*
                - Jinja2 escapes any problematic strings.
    - How to handle if SQL Statements takes longer to execute?
    - What happens if some execution fails?

## Exceptions ##
* Python raises a runtime `Exception`, when something goes wrong in our code.
* This `Exception` is like a mini crash in the application.
* There is a big list of built-in `Exception`s.
* We can also create custom `Exception`.
* Python's `try` statement is used to help manage exception in our code.
* When a `Exception` occurs we get a traceback like this

````python
Traceback (most recent call last):
  File "Chapter_11-Exception-Handling/01_exception.py", line 1, in <module>
    with open("myfile.txt") as fh:
FileNotFoundError: [Errno 2] No such file or directory: 'myfile.txt'
````
* If we ignore a raised exception it is referred to as uncaught exception.
* `try` is used to catch a raised exception.
    - Along with catching a raised exception we also have to do something with the exception.
* When an `exception` occurs, the next statement in the `try` block is not executed.
* The code in `except` block execute.

````python
try:
    with open("myfile.txt") as fh:
        file_data = fh.read()
    print(file_data)
except FileNotFoundError as ex:
    print("The Data File is missing")
````

* The above code protect against 1 `exception`. 
* We can get multiple `exception` in the code, which can be handled with multiple `except` block.

````python
try:
    with open("myfile.txt") as fh:
        file_data = fh.read()
    print(file_data)
except FileNotFoundError as ex:
    print("The Data File is missing")
except PermissionError as px:
    print("This is not allowed")
````

* We have many `exception` in python, and `Exception` is the base class from where all exception's are inherited.
* We can catch all exception possible by adding this generic exception block at the end
    - `except:`
* By catching the generic exception we loose some information about the exception.
    - `sys` module can help in getting the lost information
    - `try/except` syntax can be extended to get the required information.

## Getting Information about Exception ##

* `sys.exc_info()` : provides a 3 valued tuple
    - 1st value gives exception type
    - 2nd value provides exception value
    - 3rd value contains the traceback object.
* Python can extend the `try/except` to provide much better details.
* We can extend the `except` with `as` keyword, which gives the proper error object.
