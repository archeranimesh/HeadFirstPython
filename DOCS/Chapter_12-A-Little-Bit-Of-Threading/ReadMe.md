# Chapter 12 | A Little Bit of Threading | Dealing With Waiting #

## Introduction ##

* In our application we have have blocking calls which can hamper the user experience.
* In the application we should identify what happens after blocking calls, there are in total 2 possibility.
    1.  There is no code which utilizes the output of the blocking call.
    2. There is some code which utilizes the output of the blocking call.
* The way we handle these 2 above situation leads to proper user experience in the application.
* One of the way is to make the code in situation 1 above execute in parallel.


## Concurrency in Python ##
* Python has few options to run the code concurrently.
* `threading` library provides with a high level interface to the OS level threading interface.
* We can start using the library with a simple `import` statement.
    - `from threading import Thread`
* We can create new Thread of execution by following these steps.
    - The function name which needs to run by the thread has to be passed as named arguments `target`
    - The parameters which the function takes, has to be passed using the named arguments `args`, as a tuple.
    - The Thread object created is assigned to a variable, say `t`.
    - `t.start()` can be called to start the execution of the thread, invoking the target function.

Example of a function which we want to be executed with Threads.

````python
execute_slowly(glacial, plodding, leaden)
````

The above function can be passed to thread by following the above steps.

````python
from threading import Thread
t = Thread(target=execute_slowly, args=(glacial, plodding, leaden))
t.start()
````
