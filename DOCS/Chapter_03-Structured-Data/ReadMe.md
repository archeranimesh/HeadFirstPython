# Chapter 03 | Structured Data | Working with Structured Data #

## Dictionary ##

* Dictionary is a great built-in data structure to manipulate structured data in Python.
* It stores value in the **key/value** pair. The Key is always unique.
* Dictionary is also referred to as associative array.
* Data which has this form is an easy candidate for storing in a Dictionary.
    - Data with 2 columns and multiple rows.
* Dictionary is often used as a lookup table.

### Dictionary Operations ###

````
person = {
    "Name": "Ford Prefect",
    "Gender": "Male",
    "Occupation": "Researcher",
    "Home Planet": "Betelgeuse Seven",
}
````
* Each keys is separated from its value with a `:`.
* The complete Key-Value pair is wrapped inside a `{}`
* `pprint ` is a module which can be used to print a Dictionary.
* The insertion order is not maintained while retrieving values.
* We can access value from a Dictionary using the `[]` notation like this, `person["Name"]`
* Dictionary lookup is very fast.
* The Python Interpreter can access the value associated with a key quickly.
* A new key-value can be added to an existing Dictionary with just this.
    - `person["Age"] = 33`
* Incrementing a value can be done with `+=` operator.
    - `found["a"] += 1`
* Python does not have a `++` operator.
* We can also iterate over the Dictionary using a for loop.

````
for k in found:
    print(k, "was found", found[k], "times.")
````


## Bullet Points ##
* Dictionary is a collection of rows, with each row containing two columns. The first column is called a **Key** and the next is called a **value**.
* Each row is called a key-value pair. Dictionary can grow and shrink in size.
* Insertion order is not maintained by a dictionary.
* Accessing data in a dictionary uses the square bracket notation. Put the key inside the square brackets.
* Python `for` loop can be used to iterate over a dictionary. 


### Dictionary loops ###
* The output for a dictionary is not in any order, we can create the order by passing the dictionary to a `sorted()` method, which sorts the dictionary.
    - `for k in sorted(found):`
    - `sorted()` does not change the actual ordering of the dictionary.
* Dictionary have an interesting function called `items()`, which gives access to a key-value pair as the value for a loop variable.
    - `for k, v in found.items():`

### Dictionary Membership ###
* We can check if a key exists in a dictionary with the help of `in` operator.
* We can also use the `not in` operator to check for non membership.
* `setdefault()` : initializes with a default value if the key is not available in the dictionary.


## Bullet Points ##
* Insertion order is not maintained in Dictionary, we can use `sorted()` method to sort a dictionary.
* `.item()` allows to iterate over a Key-Value pair. On each iteration it returns a pair of key-value.
* When we access non existing Key in dictionary, it leads to `KeyError`.
* `KeyError` can be avoided by using the `in`, `not in` operator, or even we can use the `setdefault()` to initialize the value.


## Sets ##
* Sets do not allow duplicate values. This is by far the most valuable information about sets.
* Sets also support mathematical operations like, union intersection etc.
* Sets are optimize for fast look-up.
* Sets syntax looks like this.
    - `vowels = {'a', 'e', 'i', 'o', u}`
        + This declaration is similar to dictionary, with the major difference being, the absence of `:` for Key-Value pair.
* Sets do not maintained the insertion order. It can be ordered with the help of `sorted()` function.


### Set Operation. ###

* `in` : it can be used to find the existence of an object inside a set.
* `union()` : it combines 2 sets.
* `difference()` : tells what is present in 1 set bit not in other.
* `intersection()` : Returns the common object in 2 sets.

## Bullet Points ##

* Sets do not allow duplicates.
* Sets are enclosed in `{}` but they are missing the `:` with key-value pair used in dictionary.
* Sets also do not maintain the insertion order. `sorted()` helps in getting the order.
* `set()` converts any sequence into a set.
* Union, intersection, difference are some of the well know built-in function of sets.


