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







