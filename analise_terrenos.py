import json

terrenos = []

with open('terrenos.json', 'r') as f:
    terrenos = json.load(f)['terrenos']

areas = []
distancias = []
precos = []

a_sum = 0
d_sum = 0
p_sum = 0
c = 0

for t in terrenos:
    a_sum += t['area']
    areas.append(t['area'])
    d_sum += t['distancia']
    distancias.append(t['distancia'])
    p_sum += t['preco']
    precos.append(t['preco'])
    c += 1

areas.sort()
distancias.sort()
precos.sort()

a_med = a_sum / c
d_med = d_sum / c
p_med = p_sum / c

print(f"Preço médio: {p_med}")
print(f"Area média: {a_med}")
print(f"Distância média: {d_med}")

print(f"Preço Mediano: {precos[len(precos) // 2]}")
print(f"Area mediana: {areas[len(areas) // 2]}")
print(f"Distancia mediana: {distancias[len(distancias) // 2]}")