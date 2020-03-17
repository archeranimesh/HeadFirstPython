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

## Method Invocation ##
* A Object can invoke a method from a class in this way.
    - `c.increase()`
* This is interpreted as 
    - `CountFromBy.increase(c)` by the interpreter. The object is passed as a parameters to the method.
* The first argument of a methods is called `self` by convention in Python.
* The interpreter supplies the first argument to a method, we do not have to pass it explicitly.
* Not adding `self` to a method definition cause to raise `TypeError`.
* Each Object maintains it's own copy of attributes, which is possible the use of `self`.

## Variable scope ##
* A variable defined inside a function's suite, exists while the function runs.
* Outside the function suite these variable's give `NameError:`
* When we attach a variable with `self` inside a class method, it's scope is preserved outside the scope of the method.
* The value in `self` is an alias that points back to the object invoking the method.

## Class Init ##

* In Python, we have to initialize variables with a starting value, before we can use them in expression.
* In Python Class, the magic method to initialize if `__init__()`
* The methods are called dunders, and it provide hooks into every class standard behavior.
* The `__init__` standard behavior is implemented in a class called `object`.
* All Python Class automatically inherits from `object` class.
* There are certain times when we would like to override the dunder methods.
    - `__init__` : when initializing a class
    - `__eq__` : when we want to make sure our class reacts to `==` operator.



