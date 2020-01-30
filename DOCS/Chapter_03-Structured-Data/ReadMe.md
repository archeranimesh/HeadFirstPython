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
* 
