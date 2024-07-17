import matplotlib.pyplot as plt
import json
import numpy as np
from scipy.stats import linregress

data = []
real = []
pred = []
with open("resultados.json", "r") as f:
    data = json.load(f)
    real = np.array([d["real"] for d in data])
    pred = np.array([d["predicao"] for d in data])

slope, intercept, _, _, _ = linregress(real, pred)

plt.scatter(real, pred, label='Data Points')

plt.plot(real, slope * real + intercept, color='red', label='Line of Best Fit (Predicted)')
plt.plot(real, real, color='green', linestyle='--', label="Perfect Distribution")

plt.xlabel("Real")
plt.ylabel("Predicted")
plt.title("Real Values vs Fuzzy Values")
plt.legend()

plt.show()