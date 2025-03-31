from flask import Flask, render_template

# OPEN_API_KEY = 

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():


    return 
    

if __name__ == "__main__":
    app.run(debug=False)