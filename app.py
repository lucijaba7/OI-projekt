from flask import Flask, redirect, url_for, render_template, request
import transfer as t

app = Flask(__name__)
guest = ""
price = ""
 

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        guest = request.form["nm"]
        price = request.form["nmm"]
<<<<<<< HEAD
        return render_template("ispis.html")
    else: 
=======
        return render_template("ispis.html", rezultat=t.transfer(guest), guest=guest, price=price)
    else:
>>>>>>> e54d12952ef4fa1c0f85adecf994da2b56b78b48
        return render_template("index.html")



@app.route("/podaci")
def user():
    #Dorada output-a
    return render_template("ispis.html")
  
if __name__== '__main__':
    app.run(port=5000, debug=True)