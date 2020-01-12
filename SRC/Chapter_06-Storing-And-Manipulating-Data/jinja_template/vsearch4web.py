from flask import Flask, render_template, request, redirect
from vsearch import search4letters


app = Flask(__name__)


@app.route("/")
@app.route("/entry")
def entry_page() -> "html":
    return render_template(
        "entry.html", the_title="Welcome to search4letters on the web"
    )


@app.route("/search4", methods=["POST"])
def do_search() -> "html":
    phrase = request.form["phrase"]
    letters = request.form["letters"]
    title = "Here are your results"
    results = str(search4letters(phrase, letters))
    return render_template(
        "results.html",
        the_phrase=phrase,
        the_letters=letters,
        the_title=title,
        the_results=results,
    )


# making it cloud ready, as the run method will be invoked by cloud.
# the below run method should only be used when using it locally.
if __name__ == "__main__":
    # Run the web app in debug mode. It restarts the server everytime we change code.
    app.run(debug=True)
