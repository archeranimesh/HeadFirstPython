# Chapter 06 | Storing and Manipulating Data | Where to put your data #

In the web application we built in the last chapter, we will try to find the answer's to these question in the present chapter

1. How many request have been responded to?
2. What's the most common list of letters?
3. Which IP address are the request coming from?
4. Which browser is being used the most?


## Open | Process | Close ##
* The most easy way to store data is in text file.
* Python comes with built-in support for **open**, **process**, **close**
    - **open** : Open a file
    - **process** : process its data in some way
    - **close** : close the file when finished.
* `todos = open('todo.txt', 'a')`
    - It open a file name `todo.txt`.
    - The file is opened in `a`, i.e. append mode.
    - `todos` is the file stream.
* `print("text", file=todos)`
        + `print()` takes an argument `file`, which redirect the text to the file.
* `todos.close() `: The open files stream should be closed, else we can loose the data.


## Reading Data from File ##
* To read a file we can `open()` the file in default mode, which is the `read` mode.

````python
tasks = open('todo.txt')

for chore in tasks:
    print(chore)

tasks.close()
````

* In the above code `todo.txt` is opened in read mode.
* The python `for` loop when used with a file stream is intelligent enough to read a line of data from the file each time the loop operates.
* There is already new line at the end of each line in the file, in addition `print()` adds extra line, we can pass `end=""` to stop that extra line.
* Modes of file open :
    - `'r'` : Open a file for reading.
    - `'w'` : Open the file for writing. It empty the file content if present.
    - `'a'` : Open the file for append. The old content of the file is preserved.
    - `'x'` : Open a new file, throws error if file exist.
* `'b'` : The above modes of file open is for textual data, if the file has binary data, append the above modes with `'b'`, like `'ab'` or `a+b`.

## `with` statement ##

* `with` statement is preferred in place of the `open`, process and `close` stages.

````python
with open('todos.txt') as task:
    for chore in tasks:
        print(chore, end="")
````
* `with` statement is smart enough to remember to call `close` on our behalf.
* `with` statement conforms to a coding convention called **context management protocol**.
* `with` statement manages the context within the block it runs.

