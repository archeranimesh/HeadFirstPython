from flask import Flask, render_template, request
from vsearch import search4letters


app = Flask(__name__)


@app.route("/entry")
def entry_page() -> "html":
    return render_template(
        "entry.html", the_title="Welcome to search4letters on the web"
    )


@app.route("/")
def hello() -> str:
    return "Hello world from flask"


@app.route("/search4", methods=["POST"])
def do_search() -> str:
    phrase = request.form["phrase"]
    letters = request.form["letters"]
    return str(search4letters(phrase, letters))


# Run the web app in debug mode. It restarts the server everytime we change code.
app.run(debug=True)
