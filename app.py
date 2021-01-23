from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        guest = request.form["nm"]
        price = request.form["nmm"]
        return redirect(url_for("user", no=guest,nmm=price))
    else: 
        return render_template("index.html")



@app.route("/output/<no><nmm>")
def user(no,nmm):
    #Dorada output-a
    return f"<h1>Broj turista : {int(no)}</h1> </br> <h1>Max cijena : {int (nmm)}</h1>"
  
if __name__== '__main__':
    app.run(port=5000, debug=True)