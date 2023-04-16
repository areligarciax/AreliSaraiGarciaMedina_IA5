# Areli Sarai García Medina | 20310380

# Definición del grafo de ejemplo
grafo = {
    'A': {'B': 4, 'C': 3, 'D': 1},
    'B': {'A': 4, 'D': 2},
    'C': {'A': 3, 'D': 5, 'E': 6},
    'D': {'A': 1, 'B': 2, 'C': 5, 'E': 7},
    'E': {'C': 6, 'D': 7}
}

# Función para encontrar el árbol de expansión mínimo usando el algoritmo de Kruskal
def kruskal(grafo):
    # Lista de aristas ordenadas por peso
    aristas = []
    for origen in grafo:
        for destino, peso in grafo[origen].items():
            aristas.append((peso, origen, destino))
    aristas.sort()

    # Estructura para almacenar los árboles
    arboles = {}
    for nodo in grafo.keys():
        arboles[nodo] = [nodo]

    # Conjunto para almacenar las aristas del árbol de expansión mínimo
    aem = set()

    # Algoritmo de Kruskal
    for peso, origen, destino in aristas:
        if origen not in arboles[destino]:
            aem.add((origen, destino, peso))
            arboles[origen] += arboles[destino]
            for nodo in arboles[destino]:
                arboles[nodo] = arboles[origen]

    # Retornar el árbol de expansión mínimo
    return aem

# Ejecución del algoritmo y visualización del resultado
aem = kruskal(grafo)
print("Árbol de expansión mínimo:")
for origen, destino, peso in aem:
    print(f"({origen}, {destino}), peso = {peso}")