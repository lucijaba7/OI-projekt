#import main
import pulp as p
import json

def transfer(x):

  t = open('podaci.json')
  data = json.load(t)
  transfer = data["transfer"]

  #ljudi = main.ljudi
  ljudi = int(x)

  #problem se zove Transfer
  Lp_prob1 = p.LpProblem('Transfer', p.LpMinimize)

  #var odluke
  x1 = p.LpVariable("x1", 0, None, 'Integer')
  x2 = p.LpVariable("x2", 0, None, 'Integer')
  x3 = p.LpVariable("x3", 0, None, 'Integer')
  x4 = p.LpVariable("x4", 0, None, 'Integer')
  x5 = p.LpVariable("x5", 0, None, 'Integer')

  #f cilja
  Lp_prob1 += int(transfer[0]["cijena_km"])*x1 + int(transfer[1]["cijena_km"])*x2 + int(transfer[2]["cijena_km"])*x3 + int(transfer[3]["cijena_km"])*x4 + int(transfer[4]["cijena_km"])*x5 

  #ogranicenja
  Lp_prob1 += int(transfer[0]["kapacitet"])*x1 + int(transfer[1]["kapacitet"])*x2 + int(transfer[2]["kapacitet"])*x3 + int(transfer[3]["kapacitet"])*x4 + int(transfer[4]["kapacitet"])*x5 >= ljudi
    

  Lp_prob1.writeLP("Transfer.lp")

  Lp_prob1.solve()

  #print('------------RJESENJE-------------')

  #print("Vrijednost funkcije cilja: {}".format(p.value(Lp_prob.objective)))

  #print("Varijable odluke: x1 = {}, x2 = {}, x3 = {}, x4 = {}, x5 = {}".format(p.value(x1), p.value(x2), p.value(x3), p.value(x4), p.value(x5)))


  rezultat = p.value(Lp_prob1.objective)

  varijable = {}
  varijable["rez"] = rezultat

  for v in Lp_prob1.variables():
    if(v.varValue):
      varijable[v.name] = v.varValue

  return varijable


    