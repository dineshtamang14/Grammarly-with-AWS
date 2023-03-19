from flask import Flask, render_template, request
from translate import *
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=["POST", "GET"])
def main():
    if request.method == "POST":
        input = request.form.get("input_text")
        selected_lang = request.form.get("selected_language", None)
        if selected_lang is not None:
            lang = selected_lang
        return render_template("index.html", input=input, lang=lang)        


if __name__ == "__main__":
    app.run(debug=True,port=5000, host='0.0.0.0')