# Chapter 09 | The Context Management Protocol | Hooking into Python's with Statement #

## Context Management protocol ##
* Python supports simple context management in the standard library (`contextlib` module)
* The module dictates that, two magic methods should be present
    - `__enter__`
        + The interpreter invokes the object's `__enter__` method before the `with` statement's suite starts.
    - `__exit__`
        + The interpreter always invokes the object's `__exit__` method after the `with` statement suite ends.
* If we create a class with the above two magic method we can safely say it conforms to the context management protocol.
* We can also use `__init__` magic method into the above combination.
    - `__init__` is executed even before `__enter__`.
    - Defining `__init__` is not mandatory in the context management protocol.

````python
with open('todos.txt') as tasks:
    for chore in tasks:
        print(chore, end="")
````

* `__init__` is invoked as soon as the interpreter see the `with` statement.
* `__enter__` is invoked soon after the `__init__` is invoked.
* `__exit__` is invoked at the end of the `with` statement.
    - `__exit__` take's few extra parameter to inform about wrong full termination of `with` statement.
* Flask has an internal configuration called `app.config` which is a dictionary.
