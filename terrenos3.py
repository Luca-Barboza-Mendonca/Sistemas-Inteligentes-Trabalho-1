import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import json

# Range das variáveis de entrada e saída
area = ctrl.Antecedent(np.arange(100,800, 1), "area")
distancia = ctrl.Antecedent(np.arange(0,2500, 1), "distancia")
preco = ctrl.Consequent(np.arange(0, 500000, 1), "preco")


# Definição dos grupos fuzzy para cada variável, para area e preco, o automf mostra melhor preformance do que 
# grupos definidos manualmente
area.automf(3)

distancia['good'] = fuzz.trimf(distancia.universe, [0,0, 300])
distancia['average'] = fuzz.trimf(distancia.universe, [0,300, 1000])
distancia['poor'] = fuzz.trimf(distancia.universe, [300,1000, 2500])

preco.automf(5)



# area.view()
# distancia.view()
# preco.view()
plt.show()


# Definição das 5 regras fuzzy utilizadas, desenvolvidas a partir de testes do dataset coletado
rule1 = ctrl.Rule(area['poor'] & distancia['poor'] , preco['poor'])

rule2 = ctrl.Rule(area['poor'], preco['mediocre'])

rule3 = ctrl.Rule(area['average'] | distancia['average'] , preco['average'])

rule4 = ctrl.Rule(area['good'], preco['decent'])

rule5 = ctrl.Rule(area['good'] & distancia['good'], preco['good'])

# Declarar sistema de controle
preco_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
precificador = ctrl.ControlSystemSimulation(preco_ctrl)


# Carregando dados de teste e testando o sistema
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

# Salvar resultados em arquivo json e imprimir na tela
with open("resultados.json", "w") as f:
    json.dump(val, f)

print(val)
s = 0
c = 0
for v in val:
    s += v["Erro percentual"]
    c += 1
erro_percentual_medio = s / c
print(f"Erro percentual médio: {erro_percentual_medio}")

plt.show()

