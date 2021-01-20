from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        guest = request.form["nm"]
        return redirect(url_for("user", no=guest))
    else: 
        return render_template("index.html")

@app.route("/<no>")
def user(no):
    return f"<h1>Number of guests: {no}</h1>"

if __name__== '__main__':
    app.run(port=5000, debug=True)