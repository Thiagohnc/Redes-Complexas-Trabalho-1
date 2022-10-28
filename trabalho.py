import random

import networkx as nx
import numpy as np

G = nx.Graph()

def calculate_metrics(sample, sample_name):
    print('*', sample_name, '*')
    print('Número de amostras:', len(sample))
    print('Mínimo:', np.min(sample))
    print('Máximo:', np.max(sample))
    print('Média:', round(np.mean(sample), 4))
    print('Mediana:', round(np.median(sample), 4))
    print('Desvio Padrão:', round(np.std(sample), 4))
    print('--------------------')

def degrees(graph):
    return [i[1] for i in nx.degree(graph)]

def connected_component_sizes(graph):
    return [len(i) for i in nx.connected_components(graph)]

def node_clusterization(graph):
    return list(nx.clustering(graph).values())

def distances(graph):
    dist_samples = []
    dist = nx.all_pairs_shortest_path_length(graph)

    for u, dist_u in dist:
        for dist_u_v in dist_u.values():
            dist_samples.append(dist_u_v)

    return dist_samples

def approximate_distance(graph, nrand):
    distances = []
    nodes = list(graph.nodes)
    rand_idx = np.random.randint(0, len(nodes), nrand * 2)
    for i in range(nrand):
        u = nodes[rand_idx[2*i]]
        v = nodes[rand_idx[2*i + 1]]
        distances.append(nx.shortest_path_length(G, str(u), str(v)))
    return distances

with open(r'files\oregon1_010331.txt', 'r') as file:
    lines = file.read().splitlines()
    for line in lines:
        line = line.strip()
        if line[0] == '#':
            continue

        line = line.split('\t')
        G.add_edge(line[0], line[1])

calculate_metrics(degrees(G), 'Grau')
calculate_metrics(connected_component_sizes(G), 'Tamanho das CC')
calculate_metrics(node_clusterization(G), 'Clusterização')  # todo pegar a clusterização global pelos triângulos
#calculate_metrics(distances(G), 'Distância')



calculate_metrics(approximate_distance(G, nrand=1000), 'Teste distância')