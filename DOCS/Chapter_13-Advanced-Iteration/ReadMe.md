# Chapter 13 | Advanced Iteration | Looping Like Crazy #

## Introduction ##

* We can optimize loops with this 2 approaches.
    - better loop syntax.
    - better loop performance.
* Python provides both of the above in terms of `comprehension`.

## CSV ##
* CSV can be read by just using the plain vanilla file read. Just that we have to put effort to manipulate the data.
* Python provides an important module called `csv` which solves the issue of reading CSV file.
    - `csv.reader()` : reads 1 line at a time, separates the data based on `,`
    - `csv.DictReader()` : Reads the first row as a key, and the subsequent rows as value of the keys.
* Raw data can also be manipulated by using string's api and list apis.
* `split()` : `split` is a string api, which splits a string based on a delimiter like `,`, and splits into tuple.
* `strip()` : removes the white spaces from a strings start and end, and returns a string.
* We need few conversion, for date time and strings.
    - `strptime()` : Takes a string representation and changes it into time structure, based on the format.
    - `strftime()` : Converts a time structure into a string based on the format passed.
    - Few format specifiers are as below.
        + `%H` : shows hours, use 24 hrs clock.
        + `%I` : shows hours, use 12 hrs clock.
        + `%M` : shows the minutes.
        + `%p` : shows am or pm based on given time value.
* `.title()` : converts a string into a title case.

## Comprehension ##
* Comprehension are a faster and efficient way to write `for` loops.
* We can have these different type of comprehension.
    - List
    - Dict 
    - Set 
### List Comprehensions ###

* `flight_times2 = [convert2ampm(ft) for ft in flights.keys()]`
    - The right side creates a list comprehension, 
    - The for loop is executed first, and each value of `ft` is passed to `convert2ampm`, and stored in list.
    - The above process is repeated for each value in the `flights.keys()`
* The above list comprehension, can also be used to filter values.
    - `flight_times2 = [convert2ampm(ft) for ft in flights.keys() if ft == '17:00']`
        + This comprehension is similar, but the ft is first filtered with the if conditions.
        + Once passing that condition is then stored in the list.

### Dictionary Comprehension ###
* `more_flights = {convert2ampm(k): v.title() for k, v in flights.items()}`
    - The above is an example of dictionary comprehension.
    - The for loop is executed first, and the `k` and `v` from each iteration, is used to form a key value pair
    - `convert2ampm(k): v.title()`
        + The key value is store after conversion, the key is converted to string in `am` or `pm` format.
        + The value(`v`) is converted to title case and stored.
* The dictionary comprehension, just like list comprehension can be filtered.
    * `filtered_flights = {convert2ampm(k): v.title() for k, v in flights.items() if v == "FREEPORT"}` 
        - Everything happens like before, only the value of `k` and `v` is stored when `v == "FREEPORT"` condition is matched.

### Set Comprehension ###
* `found2 = {v for v in vowels if v in message}`
    - The above is an example of set comprehension, it is almost similar to Dictionary comprehension.
    - The main difference between the set and dict comprehension, is the absence `:` in set comprehension.

### Tuple Comprehension or Generator ###

````python
for i in (x ** 3 for x in [1, 2, 3, 4, 5]):
    print(i)
````
* Though the above code looks to be using tuple comprehension, but actually the code within `()` creates an generator.
* When we use list comprehension, all the intermediate data for the comprehensions are stored and then finally the combined data is returned.
* This can cause issues of memory.
* We can replace the same concept but surround it with `()` making it a generator.
* A generator returns only 1 items at a time.

````python
def gen_from_urls(urls: tuple) -> tuple:
    for resp in (requests.get(url) for url in urls):
        # yield returns only 1 items at a time.
        yield len(resp.content), resp.status_code, resp.url
````

* When a functions executes a `return` statement, the function terminates.
* When a functions sees a `yield` statement, it returns only the current value,


## Bullet Points ##
* Python has many different modules in built to work on data, `open()` is one, `csv` module is another.
* Method chaining helps in multiple things done in a single line of code.
* While chaining methods care should be taken, about the data structure returned by the function.
* `for` loop can be reworked into a comprehension.
* Comprehension can used to process existing list, dict, or sets.
* There is nothing called tuple comprehension, as tuple are immutable.
* Generator looks a lot like a tuple comprehension, and uses `yield ` to generate data.



## Reference ##
* [Python time strftime() Method ](https://www.tutorialspoint.com/python/time_strftime.htm)
* [Python time strptime() Method](https://www.tutorialspoint.com/python/time_strptime.htm)
  
