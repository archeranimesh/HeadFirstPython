# Chapter 10 | Function Decorators | Wrapping Functions #

## Function Decorators ##
* Python has a unique technique called **function decorators**, where we can add code to an existing function without having to modify any of the existing code.

## Web - StateFull or StateLess ##
* The current web-app which we developed has all the url's publicly available.
* The web is be default **stateless**
    * Each and every request that a web server receives is treated as independent request.
* HTTP dictates that the web server should err towards performance as a result should forget about request states.
    * The Web server is optimized to respond quickly, but forget fast, and is said to operate in a **stateless** manner.
* The web server does not runs our code as we were running it in our local PC.
    - The web app code is imported in case of running by a web server.
    - The web server can load and unload the web app code as needed esp during inactivity.
    - If the state is preserved in a global variable, we could 
        + The value associated with the global variable can be lost due to loading and un-loading of the app.
        + The global variable will work only for single user, how will it handle multiple users.
