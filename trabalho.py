import random

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

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

def plot_normalized_histogram(sample):
    bin_max_number = 0
    bin_size = 1
    x, y, bin_sizes = [], [], []

    sample.sort()
    for i in range(len(sample)):
        if sample[i] <= bin_max_number:
            y[-1] += 1
        else:
            bin_max_number += bin_size
            x.append(bin_max_number)
            y.append(1)
            bin_sizes.append(bin_size)
            bin_size *= 2

    x = np.array(x)
    y = np.array(y)
    y = y/len(sample)  # Getting fraction of the counts
    y = y/bin_sizes  # Normalizing

    plt.loglog(x, y, '.')
    plt.show()

def plot_ccdf(sample):
    x, y, bin_sizes = [], [], []

    sample.sort()
    uniques, counts = np.unique(np.array(sample), return_counts=True)
    total = sum(counts)
    total2 = sum(counts)
    for i in range(len(uniques)):
        x.append(uniques[i])
        y.append(total/total2)
        total -= counts[i]
    plt.loglog(x, y, '.')
    plt.show()

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
        if line[0] in ['#', '%']:
            continue

        if '\t' in line:
            line = line.split('\t')
        else:
            line = line.split(' ')

        G.add_edge(line[0], line[1])

calculate_metrics(degrees(G), 'Grau')
calculate_metrics(connected_component_sizes(G), 'Tamanho das CC')
#calculate_metrics(node_clusterization(G), 'Clusterização')  # todo pegar a clusterização global pelos triângulos
#calculate_metrics(distances(G), 'Distância')
#calculate_metrics(approximate_distance(G, nrand=10000), 'Teste distância')

plot_ccdf(degrees(G))