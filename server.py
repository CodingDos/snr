from flask import render_template

OPEN_API_KEY = 

@app.route("/")
def index():
    return render_template("")

@app.route("/upload", methods=["POST"])
def upload():
    