import itertools
import random
import networkx as nx
import matplotlib.pyplot as plt

# Definición de estados y matriz de adyacencia
estados = ["Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Chiapas", "Chihuahua", "Coahuila"]

matriz_adyacencia = [
    [0, 500, 0, 0, 0, 300, 700],  # Aguascalientes
    [500, 0, 0, 1000, 0, 100, 300],     # Baja California
    [0, 0, 0, 0, 0, 800, 150],     # Baja California Sur
    [0, 1000, 0, 0, 500, 1000, 0],    # Campeche
    [0, 0, 0, 500, 0, 200, 100],    # Chiapas
    [0, 100, 800, 0, 200, 0, 400],  # Chihuahua
    [300, 300, 150, 1000, 100, 400, 0]      # Coahuila
]

def calcular_costo(recorrido):
    costo_total = 0
    for i in range(len(recorrido) - 1):
        origen = estados.index(recorrido[i])
        destino = estados.index(recorrido[i + 1])
        costo_total += matriz_adyacencia[origen][destino]
    return costo_total

# Recorrido sin repetir estados
print("Recorrido sin repetir estados:")
recorrido_sin_repetir = ["Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Chiapas", "Chihuahua", "Coahuila"]
print(" -> ".join(recorrido_sin_repetir))
costo_total_sin_repetir = calcular_costo(recorrido_sin_repetir)
print(f"Costo total: {costo_total_sin_repetir} pesos")

# Recorrido con posible repetición de estados
print("\nRecorrido con posible repetición de estados:")
recorrido_con_repeticion = random.choices(estados, k=7)
while len(set(recorrido_con_repeticion)) < len(estados):
    recorrido_con_repeticion = random.choices(estados, k=7)
print(" -> ".join(recorrido_con_repeticion))
costo_total_con_repeticion = calcular_costo(recorrido_con_repeticion)
print(f"Costo total: {costo_total_con_repeticion} pesos")

# Visualizar el grafo
G = nx.Graph()
G.add_nodes_from(estados)
for i in range(len(estados)):
    for j in range(i + 1, len(estados)):
        if matriz_adyacencia[i][j] != 0:
            G.add_edge(estados[i], estados[j], weight=matriz_adyacencia[i][j])

pos = nx.spring_layout(G)  # Layout para visualización

plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_size=1500, node_color="lightblue", font_size=12, font_weight="bold")
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Grafo de Estados y Caminos")
plt.show()
