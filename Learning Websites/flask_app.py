from flask import Flask

app = Flask(__name__)

@app.route("/")
def yeet():
    return "hi jah"

app.run("0.0.0.0")