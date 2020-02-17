from flask import Flask, render_template
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


@app.route("/search")
def do_search() -> str:
    return str(search4letters("life, the universe, and everything", "eiru"))


app.run()
