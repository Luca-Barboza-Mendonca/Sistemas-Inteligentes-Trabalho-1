import matplotlib.pyplot as plt
import json
import numpy as np
from scipy.stats import linregress

data = []
real = []
pred = []
names = []
with open("resultados.json", "r") as f:
    data = json.load(f)
    real = np.array([d["real"] for d in data])
    pred = np.array([d["predicao"] for d in data])
    names = np.array([d["nome"] for d in data])

slope, intercept, _, _, _ = linregress(real, pred)

plt.scatter(real, pred, label='Pontos de predição')

# for i, label in enumerate(names):
#     plt.annotate(label, (real[i], pred[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.plot(real, slope * real + intercept, color='red', label='Linha de Best Fit (Predito)')
plt.plot(real, real, color='green', linestyle='--', label="Distribuição perfeita")

plt.xlabel("Real")
plt.ylabel("Predito")
plt.title("Valores Reais vs Valores Preditos")
plt.legend()

plt.show()