import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import json

area = ctrl.Antecedent(np.arange(100,800, 1), "area")
distancia = ctrl.Antecedent(np.arange(0,3601, 1), "distancia")
preco = ctrl.Consequent(np.arange(0, 500000, 1), "preco")

area.automf(3)

# area['poor'] = fuzz.trimf(area.universe, [200,200, 300])
# area['average'] = fuzz.trimf(area.universe, [200,300, 500])
# area['good'] = fuzz.trimf(area.universe, [300,500, 800])

distancia['good'] = fuzz.trimf(distancia.universe, [0,0, 300])
distancia['average'] = fuzz.trimf(distancia.universe, [0,300, 1000])
distancia['poor'] = fuzz.trimf(distancia.universe, [300,1000, 2500])

preco.automf(5)

# area.view()
# distancia.view()
# preco.view()
plt.show()

rule1 = ctrl.Rule(area['poor'] & distancia['poor'] , preco['poor'])

rule5 = ctrl.Rule(area['poor'], preco['mediocre'])

rule2 = ctrl.Rule(area['average'] | distancia['average'] , preco['average'])

rule3 = ctrl.Rule(area['good'], preco['decent'])

rule4 = ctrl.Rule(area['good'] & distancia['good'], preco['good'])

preco_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
precificador = ctrl.ControlSystemSimulation(preco_ctrl)

# precificador.input['area'] = 420
# precificador.input['distancia'] = 260

terrenos = []

with open('terrenos.json', 'r') as f:
    terrenos = json.load(f)['terrenos']

val = []

for t in terrenos:
    input_area = t['area']
    input_distancia = t['distancia']

    precificador.input['area'] = input_area
    precificador.input['distancia'] = input_distancia

    precificador.compute()

    out = precificador.output['preco']
    real = t["preco"]
    loss = (abs(real - out)/real) * 100
    val.append({"nome": t["nome"],"predicao": out, "real": real, "Erro percentual": loss})
    print(out)

with open("resultados.json", "w") as f:
    json.dump(val, f)
# preco.view(sim=precificador)

print(val)
s = 0
c = 0
for v in val:
    s += v["Erro percentual"]
    c += 1
erro_percentual_medio = s / c
print(f"Erro percentual médio: {erro_percentual_medio}")

plt.show()

