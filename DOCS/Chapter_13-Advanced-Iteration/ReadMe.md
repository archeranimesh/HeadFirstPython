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
