from flask import Flask, redirect, url_for, render_template, request
import transfer as t
import ponude as p

app = Flask(__name__)
guest = ""
price = ""
 

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        guest = int(request.form["nm"])
        price = request.form["nmm"]
        transfer=t.transfer(guest)
        ponude=p.ponude(guest, transfer, price)  
        prodajna_cijena=round(ponude["REZULTAT"],2)
        po_osobi=round(prodajna_cijena/guest,2)
        ukupni_troskovi=round(prodajna_cijena/1.15,2)
        marza=round(prodajna_cijena - prodajna_cijena/1.15,2)

        if ponude["opt"] == "Infeasible":
            return render_template("index.html", alert="Ne postoji optimalno rješenje. Maksimalna cijena koju želite platiti izlazi iz prostora mogućih rješenja.")
        else:
            return render_template("ispis.html", dict_rjesenja=ponude, ljudi=guest, ukupni_troskovi=ukupni_troskovi, marza=marza, prodajna_cijena=prodajna_cijena, po_osobi=po_osobi)
    else:
        return render_template("index.html")