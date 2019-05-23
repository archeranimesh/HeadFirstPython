# Chapter 10 | Function Decorators | Wrapping Functions #

## Function Decorators ##
* Python has a unique technique called **function decorators**, where we can add code to an existing function without having to modify any of the existing code.

## Web - StateFull or StateLess ##
* The current web-app which we developed has all the url's publicly available.
* The web is be default **stateless**
    * Each and every request that a web server receives is treated as independent request.
* HTTP dictates that the web server should err towards performance as a result should forget about request states.
    * The Web server is optimized to respond quickly, but forget fast, and is said to operate in a **stateless** manner.
* The web server does not runs our code as we were running it in our local PC.
    - The web app code is imported in case of running by a web server.
    - The web server can load and unload the web app code as needed esp during inactivity.
    - If the state is preserved in a global variable, we could 
        + The value associated with the global variable can be lost due to loading and un-loading of the app.
        + The global variable will work only for single user, how will it handle multiple users.


## Session ##
We need to achieve these two things to make user authentication work.
* A way to store variables without using global variables.
* A way to keep one webapp's user data from interfering with another's.

The solution is to uses the Flask's `session`.
* Flask's `session` uses these method's
    - Adds a small identification data to the browser - *cookies*
    - Links the above to web server using a *session ID*
* Flask `session` is like a dictionary which can store our web application state.
* Flask `session` makes sure that the data stored in it is available for the entire duration of the web application.
* We can store and retrieve values from Flask `session` just like any other Python dictionary.

## Decorators ##
* A decorator allows to augment an existing function with extra code.
* Decorator's are always prefixed with `@`.
* We can create a decorator, if we can do these 4 things
    - How to create a function
    - Pass a function as an argument to a function.
    - Return a function from a function
    - How to process any number and type of argument.

### Function Passing Function ###
* We can pass function into a function in Python.
* The reason being everything is an object in Python.

````python
msg = "Hello from Head First Python 2e"


def hello():
    print(msg)


if __name__ == "__main__":
    print("Id of message is: ", id(msg))
    print("Id of function is: ", id(hello))
    print("type of function is: ", type(hello))
    print(type(id))
````

* In the above example none of the line causes an error, so it is valid to pass function to a function.

### Invoking Passed Function ###
* The function passed as an argument to a function can also be invoked.

````python
def apply(func: object, value: object) -> object:
    return func(value)


if __name__ == "__main__":
    (apply(print, 42))
    print(apply(id, 42))
    print(apply(type, 42))
    print(apply(len, "marvin"))
````

* The above example uses `apply()` to invoke different built-in functions like `len`, `id`, `type` and `print`.

### Nested Function ###
* We can define a new function inside a function.
* The scope of the inner function is only inside the function.
* We can also return the inner function.

````python
def outer():
    def inner():
        print("This is Inner")
    print("This is outer, invoking inner")
    inner()


if __name__ == "__main__":
    outer()
````

* In the above function the `inner()` is defined inside `outer()` function.
* We can invoke `inner` only from within `outer()` function.

### Function Returning Function ###
* We can even return a function in Python.

````python
def outer():
    def inner():
        print("This is Inner")

    print("This is outer, invoking inner")
    return inner


if __name__ == "__main__":
    i = outer()
    print(type(i))
    i()
````

* In the above example `i` acts as an alias for `inner` function.


## Variable argument to function ##
* There are times when we want to pass variable number of arguments to a function.
* Python provides a special notation which allows to pass zero or more arguments to a function.
* The notation is called `*args`, typically `args` is a tuple.
* We can use this `*` notation to even expand a list.

````python
def myfunc(*args):
    for a in args:
        print(a, end=" ")
    if args:
        print()


if __name__ == "__main__":
    values = [1, 2, 3, 4, 5, 6]
    myfunc(10)
    myfunc()
    myfunc(10, 20, 30, 40, 50)
    myfunc(values)
    myfunc(*values)
````
* In the above `myfunc` we can pass multiple arguments.


### Accepting a Dictionary as arguments ###
* We can also sent multiple key value to a function as arguments.
* The special notation to read it is `**kwargs`, which makes all the arguments as a Key Value pair.
* It can even expand an existing dictionary.

````python
def myfunckw(**kwargs):
    for k, v in kwargs.items():
        print(k, v, sep="->", end=" ")
    if kwargs:
        print()


if __name__ == "__main__":
    dbconfig = {
        "host": "127.0.0.1",
        "user": "vsearch",
        "password": "hello",
        "database": "vsearchlogDB",
    }
    myfunckw(a=10, b=20)
    myfunckw(**dbconfig)
````
* In the above function we can pass multiple key words argument.
* We can combine both `*args` and `**kwargs` to make a function take any no and any type of arguments.
* The below example take both type of argument.

````python
def myfunc_args(*args, **kwargs):
    if args:
        for a in args:
            print(a, end=" ")
        print()
    if kwargs:
        for k, v in kwargs.items():
            print(k, v, sep="->", end=" ")
        print()


if __name__ == "__main__":
    myfunc_args()
    myfunc_args(1, 2, 3)
    myfunc_args(a=10, b=20, c=30)
    myfunc_args(1, 2, 3, a=10, b=20, c=30)
````

## Custom Function Decorators ##

````python
from flask import session
from functools import wraps


def check_logged_in(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "logged_in" in session:
            return func(*args, **kwargs)
        return "You are NOT Logged in"
    return wrapper

````
* We can create the custom function decorator as shown above.
* It still follow the same 4 principal described above.
    - How to create a function
    - Pass a function as an argument to a function.
    - Return a function from a function
    - How to process any number and type of argument.
* The only secret sauce is to call the `@wraps(func)` imported from `functools`
* Logic Abstraction is one of the reasons the 
* Generic Code Template for decorators

````python
from functools import wraps

def decorator_name(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
    # 1. Code to execute BEFORE calling the decorated function
    # 2. Call the decorated function as required, returning its results if needed.
    # 3. Code to execute INSTEAD of calling the decorated function.
    return wrapper
````


## Bullet Points ##
* When you need to store server side state within a Flask webapp, use the `session` dictionary.
* You can pass a function as an argument to another function.
    - Using the function name gives the function object, which can be used just like any other variable.
* We can invoke the passed function as an arguments.
* A function can be nested inside an enclosing function's suite.
* A function can also be returned.
* `*args` = expand to a list of items
* `**kwargs` = expand to a dictionary of K,V
* 




