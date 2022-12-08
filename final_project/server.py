from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/englishToFrench", methods=['POST'])
def englishToFrench():
    textToTranslate = request.form.get('textToTranslate')
    translatedtext = translator.english_to_french(textToTranslate)

    return render_template('index.html',result=translatedtext)

@app.route("/frenchToEnglish", methods=("GET", "POST"))
def frenchToEnglish():
    if request.method == "POST":
        textToTranslate = request.args.get('textToTranslate')
        translatedtext = translator.french_to_english(textToTranslate)


    return render_template('index.html', result=translatedtext)

@app.route("/")
def renderIndexPage():
     return render_template('index.html', result="result")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
