# Chapter 05 | Building A WebApp | Getting Real #

## WebApp ##
* Everything on the WWW is about request and response.
* A web request is sent from a web browser to a web server, when a user does some action.
* A web response is formulated on the web server and then sent back to the browser.
* These are the five steps which happens in the above flow.
    - **Step 1:** User enters a URL on the browser, or clicks a link on the browser.
    - **Step 2:** The web browser converts the user action into a web request and send it over Internet.
    - **Step 3:** The web server, receives the request and has to decide one of the two,
        + **Static Content:** If the request is only for static content like, html file, images, or anything stored in web server, the web server locates its and send the request back.
        + **Dynamic Content:** This is the content which is generated at runtime, such as search runtime
    - **Step 4:** The Web server send the response back.
    - **Step 5:** The web browser receives the response and displays the response.

## Flask ##
* Flask is a popular web frameworks, and it is not part of the standard library.
* Third party library needs to install first before use.
* We can install `flask`, by using `pip` and give this command `python -m pip --upgrade pip`
* It installs these 4 dependencies along with `flask`
    - `Jinja2`
    - `MarkupSafe`
    - `Werkzeug`
    - `itsdangerous`
* `flask` is a micro web framework, in that it provides the minimum set of technologies needed for the task.
* We can execute a `flask` application just like any other python application.
    - `python hello_flask.py`
* We can see the logs where it says `Running on http://127.0.0.1:5000/`, so `flask` is serving the web page on port `5000`, just click on the link and it should take you to a browser.

### Hello World Flask Application ###

````python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello() -> str:
    return "Hello world from flask"


app.run()
````
Lets understand the above code one line at a time.

* `from flask import Flask` : We are importing `Flask` class from `flask` module.
* `app = Flask(__name__)` : The `Flask` object is created and assigned to `app` object.
    - `__name__` : It provides the currently active module. 
    - `Flask` class needs to know the current value of `__name__` when creating new flask object.
    - `Flask` with this one line of code have abstracted a lot of initial setup for web development away from the programmer.
* `@app.route("/")` : This introduces a new concept in python called **Decorators**.
    - Decorators adjust the behavior of an existing function without actually changing the function code.
    - Decorators can be applied to both function and classes, but if applied primarily applied to function.
    - The above decorators makes an arrangement that when the web application is requested of `/` page, it invokes the `hello()` function.
* The next is the function definition.
* `app.run()` : Its ask flask to run the web application.
* `127.0.0.1` : This is the loop back URL, which is also called as localhost.
* `:5000` : The protocol port number on which the server is running.  

## Jinja ##
* We cannot put complete HTML as raw text string in python, it will become unmanageable.
* We can always use a **template engine**.
* We can define a top level template, called **base template**, which is then inherited by others.
* `Jinja2` is the template engine shipped with `Flask`.
* We add special characters inside HTML, which is understood or replaced by `Jinja`
    - `{{ TEXT }}` : The value of `TEXT` will be provided by `jinja` before rendering.
    - `{% block start %}, {% end block %}`: A block of HTML code will be supplied by `jinja`.


