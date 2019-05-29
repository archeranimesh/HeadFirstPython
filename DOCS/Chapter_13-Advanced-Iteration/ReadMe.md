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



## Reference ##
* [Python time strftime() Method ](https://www.tutorialspoint.com/python/time_strftime.htm)
* [Python time strptime() Method](https://www.tutorialspoint.com/python/time_strptime.htm)
  
