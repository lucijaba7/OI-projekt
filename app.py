from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home(name="Lucija Babić"):
    return render_template("index.html", name=name)

if __name__== '__main__':
    app.run(port=5000, debug=True)