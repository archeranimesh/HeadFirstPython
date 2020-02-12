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

