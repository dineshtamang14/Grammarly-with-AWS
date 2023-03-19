from flask import Flask, render_template, request, send_file
from translate import *
from sentiment import *
from pos import *
from entity import *
from upload import *
from transcribe import *
from text_to_speech import *


app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST", "GET"])
def upload():
    if request.method == "POST":
        f = request.files["file"]
        file_name = upload_file_s3(f)
        text = do_transcribe(file_name)
        return render_template("index.html", filename=file_name, text=text)


@app.route("/audio", methods=["GET"])
def serve_audio():
    filename = "output.mp3"
    return send_file(filename, mimetype='audio/mpeg', as_attachment=True)


@app.route("/", methods=["POST", "GET"])
def main():
    if request.method == "POST":
        input = request.form.get("input_text")
        selected_lang = request.form.get("selected_language", None)
        if selected_lang is not None:
            lang = selected_lang
            translate = do_translate(input)
            sentiment = do_sentiment_analysis(input)
            part_of_speech = detect_pos(input)
            entities = detect_entity(input)
            p = text_to_speech(input)
        return render_template("index.html", input=input, lang=lang, translate=translate, sentiment=sentiment, part_of_speech=part_of_speech, entities=entities, p=p)        


if __name__ == "__main__":
    app.run(debug=True,port=5000, host='0.0.0.0')