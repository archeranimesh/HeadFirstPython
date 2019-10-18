from flask import Flask, render_template, request, redirect, escape, session
from vsearch import search4letters
from DBcm import UseDatabase
from checker import check_logged_in
from time import sleep

app = Flask(__name__)

app.secret_key = "HowIsLife"

# app.config is a regular python dict, we added `dbconfig` into it.
app.config["dbconfig"] = {
    "host": "127.0.0.1",
    "user": "vsearch",
    "password": "hello1",
    "database": "vsearchlogDB",
}


@app.route("/")
@app.route("/entry")
def entry_page() -> "html":
    return render_template(
        "entry.html", the_title="Welcome to search4letters on the web"
    )


# Added log_request, fo adding all request and response onto a file.
def log_request(req: "flask_request", res: str) -> None:
    with UseDatabase(app.config["dbconfig"]) as cursor:
        _SQL = """insert into log (phrase, letters, ip, browser_string, results)
                values (%s, %s, %s, %s, %s)"""
        cursor.execute(
            _SQL,
            (
                req.form["phrase"],
                req.form["letters"],
                req.remote_addr,
                req.user_agent.browser,
                res,
            ),
        )


@app.route("/search4", methods=["POST"])
def do_search() -> "html":
    phrase = request.form["phrase"]
    letters = request.form["letters"]
    title = "Here are your results"
    # uncommnent below line to create a delay in results
    # sleep(15)
    # Uncomment the below line to raise a exception
    # raise
    results = str(search4letters(phrase, letters))
    try:
        log_request(request, results)
    except Exception as err:
        print("***** Logging Failed with this error: ", str(err))
    return render_template(
        "results.html",
        the_phrase=phrase,
        the_letters=letters,
        the_title=title,
        the_results=results,
    )


@app.route("/viewlog")
@check_logged_in
def view_the_log() -> str:
    """ Display the content of the log file as a HTML Table"""
    with UseDatabase(app.config["dbconfig"]) as cursor:
        _SQL = """select phrase, letters, ip, browser_string, results from log"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()
    titles = ("Form Data", "Remote_addr", "User_agent", "Results")
    return render_template(
        "viewlog.html", the_title="View Log", the_row_titles=titles, the_data=contents,
    )


@app.route("/login")
def do_login() -> str:
    session["logged_in"] = True
    return "You are now logged in"


@app.route("/logout")
def do_logout() -> str:
    if "logged_in" in session:
        session.pop("logged_in")
        return "You are now logged out"
    else:
        return "Please Login to Logout"


# making it cloud ready, as the run method will be invoked by cloud.
# the below run method should only be used when using it locally.
if __name__ == "__main__":
    # Run the web app in debug mode. It restarts the server everytime we change code.
    app.run(debug=True)
