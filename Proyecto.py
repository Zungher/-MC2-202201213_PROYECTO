import networkx as nx
import matplotlib.pyplot as plt
# Función para obtener el grafo ingresado por el usuario
def obtener_grafo():
    while True:
        n = int(input("Ingrese el número de vértices del grafo (entre 2 y 8): "))
        if n < 2 or n > 8:
            print("El número de vértices debe estar entre 2 y 8.")
        else:
            break
    G = nx.Graph()
    for i in range(n):
        G.add_node(i)
    for i in range(n):
        for j in range(i+1, n):
            while True:
                peso = input(f"Ingrese el peso de la arista entre los vértices {i} y {j} (o enter para omitir): ")
                if peso == "":
                    break
                try:
                    peso = int(peso)
                    G.add_edge(i, j, weight=peso)
                    break
                except ValueError:
                    print("El peso debe ser un número entero.")
    return G

# Función para mostrar el grafo en una figura
def mostrar_grafo(G):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

# Función para obtener los vértices inicial y final
def obtener_vertices():
    while True:
        ini = input("Ingrese el vértice inicial (un número del 0 al n-1): ")
        try:
            ini = int(ini)
            if ini < 0 or ini >= n:
                print(f"El vértice debe ser un número del 0 al {n-1}.")
            else:
                break
        except ValueError:
            print("El vértice debe ser un número entero.")
    while True:
        fin = input("Ingrese el vértice final (un número del 0 al n-1): ")
        try:
            fin = int(fin)
            if fin < 0 or fin >= n:
                print(f"El vértice debe ser un número del 0 al {n-1}.")
            elif fin == ini:
                print("El vértice final debe ser distinto del inicial.")
            else:
                break
        except ValueError:
            print("El vértice debe ser un número entero.")
    return ini, fin

# Función para obtener el camino simple óptimo y los dos adicionales
def obtener_caminos(G, ini, fin):
    camino_optimo = nx.shortest_path(G, ini, fin, weight="weight")
    caminos_adicionales = []
    for i in range(n):
        for j in range(i+1, n):
            if G.has_edge(i, j):
                if i != ini and j != fin and nx.has_path(G, i, j):
                    camino = nx.shortest_path(G, ini, i, weight="weight")[:-1] + nx.shortest_path(G, i, j, weight="weight") + nx.shortest_path(G, j, fin, weight="weight")[1:]
                    if camino != camino_optimo:
                        caminos_adicionales.append(camino)
    return camino_optimo, caminos_adicionales

# Función para mostrar los caminos obtenidos
def mostrar_caminos(camino_optimo, caminos_adicionales):
    print(f"Caminos simples óptimos de {ini} a {fin}:")
    print(camino_optimo)
    if len(caminos_adicionales) > 0:
        print("Caminos simples adicionales:")
        for camino in caminos_adicionales[:2]:
            print(camino)
    else:
        print("No existen caminos simples adicionales.")
      
n = 0
while n < 2 or n > 8:
    G = obtener_grafo()
    n = len(G.nodes())
mostrar_grafo(G)
ini, fin = obtener_vertices()
camino_optimo, caminos_adicionales = obtener_caminos(G, ini, fin)
mostrar_caminos(camino_optimo, caminos_adicionales)

def mostrar_caminos_en_grafo(G, camino_optimo, caminos_adicionales):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    # Dibujar camino óptimo
    edges_optimo = list(zip(camino_optimo, camino_optimo[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=edges_optimo, edge_color='r', width=2)
    # Dibujar caminos adicionales
    if len(caminos_adicionales) > 0:
        colors = ['g', 'b'] # colores para cada camino adicional
        for i, camino in enumerate(caminos_adicionales[:2]):
            edges_adicional = list(zip(camino, camino[1:]))
            nx.draw_networkx_edges(G, pos, edgelist=edges_adicional, edge_color=colors[i], width=2)
    plt.show()
    n = 0
while n < 2 or n > 8:
    G = obtener_grafo()
    n = len(G.nodes())
ini, fin = obtener_vertices()
camino_optimo, caminos_adicionales = obtener_caminos(G, ini, fin)
mostrar_caminos_en_grafo(G, camino_optimo, caminos_adicionales)
mostrar_caminos(camino_optimo, caminos_adicionales)