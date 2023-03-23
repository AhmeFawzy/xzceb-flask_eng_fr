from machinetranslation import translator
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def renderIndexPage():
    return render_template("index.html")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    if textToTranslate is None:
        return "No text to translate"
    frenchText = translator.english_to_french(textToTranslate)
    return frenchText

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    if textToTranslate is None:
        return "No text to translate"
    englishText = translator.french_to_english(textToTranslate)
    return englishText

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
