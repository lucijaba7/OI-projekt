from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        guest = request.form["nm"]
        price = request.form["nmm"]
        return f"<h1>Broj turista : { guest } </h1> </br> <h1>Max cijena : { price }</h1>"
    else:
        return render_template("index.html")



@app.route("/podaci")
def user():
    #Dorada output-a
    return render_template("ispis.html")
  
if __name__== '__main__':
    app.run(port=5000, debug=True)