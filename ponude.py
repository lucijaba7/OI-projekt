import transfer as t
import pulp as p
import json

def ponude(x, y, z):

    t = open('podaci.json')
    data = json.load(t)
    smjestaj = data["smjestaj"]
    izleti = data["izleti"]
    degustacije = data["degustacije"]

    Lp_prob2 = p.LpProblem('Ponude', p.LpMaximize)

    ljudi = int(x)
    transfer=y["rez"]
    lista_smjestaji=[]
    lista_izleti=[]
    lista_degustacije=[]

    def f_cijena(rijecnik):
        if(ljudi >= 70):
            return int(rijecnik["min_70"])
        elif(ljudi >= 50):
            return int(rijecnik["min_50"])
        elif(ljudi >= 30):
            return int(rijecnik["min_30"])
        elif(ljudi >= 10):
            return int(rijecnik["min_10"])
        else:
            return int(rijecnik["min_1"])

    def moze_nemoze(smjestaj_grad, izlet_gradovi, deg_grad):
        pom = 0
        for i in izlet_gradovi:
            if smjestaj_grad == i:
                pom += 1
            if deg_grad == i:
                pom += 1
        if pom == 2:
            return 1
        return 0

    def marza(x):
        return x * 0.15 + x


    #liste cijena za smjestaj, izlet i degustaciju
    for i in smjestaj:
        lista_smjestaji.append(2*transfer*int(i["udaljenost"])+ljudi*int(i["cijena_nocenje"]))

    for i in izleti:
        lista_izleti.append(transfer*int(i["ukupno_km"])+400)

    for i in degustacije:
        lista_degustacije.append(ljudi*f_cijena(i))

    rijecnik = {}

    #var odluke
    for i in range(9):
        for j in range(9):
            for k in range(9):
                var = "x{}{}{}".format(i+1,j+1,k+1)
                rijecnik[var] = p.LpVariable(var, 0, None, 'Integer')

    #funkcija cilja
    pom = 0

    for i in range(9):
        for j in range(9):
            for k in range(9):
                var = "x{}{}{}".format(i+1,j+1,k+1)
        
                pom += marza(lista_smjestaji[i]+lista_izleti[j]+lista_degustacije[k])*rijecnik[var]
        
    Lp_prob2 += pom 

    print(lista_degustacije)
    print(lista_izleti)
    print(lista_smjestaji)

    #ogranicenje na ukupnu cijenu
    Lp_prob2 += pom <= int(z)*ljudi

    #ogranicenje kapacitet smjestaja
    pom = 0

    for i in range(9):
        for j in range(9):
            for k in range(9):
                var = "x{}{}{}".format(i+1,j+1,k+1)

                pom += int(smjestaj[i]["kapacitet"])*rijecnik[var]

    Lp_prob2 += pom >= ljudi

    #ogranicenje moze/nemoze
    pom = 0      

    for i in range(9):
        for j in range(9):
            for k in range(9):
                var = "x{}{}{}".format(i+1,j+1,k+1)

                pom += moze_nemoze(smjestaj[i]["grad"], izleti[j]["gradovi"], degustacije[k]["grad"])*rijecnik[var]
        
    Lp_prob2 += pom == 1

    #ogranicenje sume var. ćelija
    Lp_prob2 += sum(rijecnik.values()) == 1


    Lp_prob2.writeLP("Ponude.lp")

    status = Lp_prob2.solve()
    
    rjesenje = (p.LpStatus[status])

    #('------------RJESENJE-------------')

    varijable = {}
    varijable["opt"] = rjesenje

    for v in Lp_prob2.variables():
        if(v.varValue):
            varijable[v.name] = v.varValue

    return varijable
