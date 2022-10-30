import os
import networkx as nx


def read_edgelist(file_path, graph_type):
    if graph_type == 'graph':
        G = nx.Graph()
    elif graph_type == 'digraph':
        G = nx.DiGraph()
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
        for line in lines:
            line = line.strip()
            if line[0] in ['#', '%']:
                continue

            if '\t' in line:
                line = line.split('\t')
            elif ',' in line:
                line = line.split(',')
            else:
                line = line.split(' ')
            G.add_edge(line[0], line[1])
    return G


def read_gml(file_path):
    return nx.read_gml(file_path)


def read_graphml(file_path):
    return nx.read_graphml(file_path)

def read_file(filename, graph_type=None):
    file_path = os.path.join('files', filename)
    if filename.endswith('.txt') or filename.endswith('.csv'):
        return read_edgelist(file_path, graph_type)
    elif filename.endswith('.gml'):
        return read_gml(file_path)
    elif filename.endswith('.graphml'):
        return read_graphml(file_path)

    raise Exception('File extension not recognized')