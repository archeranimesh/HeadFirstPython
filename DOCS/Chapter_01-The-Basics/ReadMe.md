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

### Important points ###


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



