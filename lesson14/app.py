from flask import Flask
app = Flask(__name__)
@app.route("/")
def homepage():
    return "Hello world"

@app.route("/about/")
def about():
    return "Eto sait dly podaji <b> krujek </b>"
app.run()   