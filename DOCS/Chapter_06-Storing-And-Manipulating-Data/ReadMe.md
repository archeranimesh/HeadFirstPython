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
