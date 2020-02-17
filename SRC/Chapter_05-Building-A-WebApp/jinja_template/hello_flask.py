from flask import Flask, render_template
from vsearch import search4letters


app = Flask(__name__)


@app.route("/entry")
def entry_page() -> "html":
    return render_template(
        "entry_html", the_title="Welcome to search4letters on the web"
    )
