# Chapter 08 | A Little Bit of Class | Abstracting Behavior and State #

* Classes let us bundle code behavior and the state together.
* Python borrows its programming approaches from these
    * Object-Oriented
    * Functional
    * Procedural


## Object Oriented Primer ##
* Python with its Object-Oriented Paradigm supports
    - Inheritance
    - Polymorphism
    - Encapsulation
* A class bundles **behavior** and **state**.
    - Behavior means function.
    - State means variables.
* A class in Python has **methods** and **attributes**.
    - Methods is the OOP name given to a function defined inside a Class.
    - Attributes is the name given to variables inside a Class.

## Object Instantiation ##
* To use a class, we have to create an object from it. This process is called Object Instantiation.
* A class is created in this way
    - `class CountFromBy:`
    - The important things are the use of the keyword `class`
    - The Class name starts capital letters which is a convention.
* We create an object of the above Class by using
    - `a = CountFromBy()`
    - The `type(a)` = `<class '__main__.CountFromBy'>`
    - Creating a object is same as calling a function.
* There is well established convention in the Python Community in the difference between naming of function and classes.
    - Functions are always named using lowercase letter, with underscore for emphasis.
    - CamelCase if used for Class names. 
    - Both the above rule is not enforced by the interpreter.
* Each object created from a class shares the behaviors (methods), but maintains its own copy of any state (the attribute).

