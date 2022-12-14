import networkx as nx
import numpy as np


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


def connected_components_sizes(graph):
    return [len(i) for i in nx.connected_components(graph)]


def strongly_connected_components_sizes(graph):
    return [len(i) for i in nx.strongly_connected_components(graph)]


def weakly_connected_components_sizes(graph):
    return [len(i) for i in nx.weakly_connected_components(graph)]


def node_clusterization(graph):
    return list(nx.clustering(graph).values())


def distances(graph):
    dist_samples = []
    dist = nx.all_pairs_shortest_path_length(graph)

    for u, dist_u in dist:
        for dist_u_v in dist_u.values():
            dist_samples.append(dist_u_v)

    return dist_samples


def vertices_distance(graph, u, v):
    try:
        return nx.shortest_path_length(graph, str(u), str(v))
    # if the graph is a DiGraph and there is no path from u to v, try again from v to u
    except nx.exception.NetworkXNoPath:
        if isinstance(graph, nx.DiGraph):
            return nx.shortest_path_length(graph, str(v), str(u))


def approximate_distance(graph, nrand):
    dists = []
    nodes = list(graph.nodes)
    rand_idx = np.random.randint(0, len(nodes), nrand * 2)
    for i in range(nrand):
        u = nodes[rand_idx[2 * i]]
        v = nodes[rand_idx[2 * i + 1]]
        while True:
            while u == v:
                v = nodes[np.random.randint(0, len(nodes))]
            try:
                dists.append(vertices_distance(graph, u, v))
            # if there is no path, try again with random vertices
            except nx.exception.NetworkXNoPath:
                u = nodes[np.random.randint(0, len(nodes))]
                v = nodes[np.random.randint(0, len(nodes))]
                continue
            break

    return dists
