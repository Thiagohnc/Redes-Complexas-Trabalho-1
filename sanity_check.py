import networkx as nx
import ast

G = nx.Graph()

with open(r'files\oregon1_010331.txt', 'r') as file:
    lines = file.read().splitlines()
    for line in lines:
        line = line.strip()
        if line[0] == '#':
            continue

        line = line.split('\t')
        G.add_edge(line[0], line[1])
        G.add_edge(line[1], line[0])

with open(r'files\oregon1_010331_eccentricity.txt') as file:
    lines = file.read()
    eccentricity = ast.literal_eval(lines.strip())

print('Nodes:', len(G.nodes))
print('Edges:', len(G.edges))
print('Nodes in largest CC:', max([len(i) for i in nx.connected_components(G)]))
print('Average clustering coefficient:', round(nx.average_clustering(G), 4))
print('Number of triangles:', (1/3) * sum(nx.triangles(G).values()))
print('Fraction of closed triangles:', round((1/3) * nx.transitivity(G), 4))  # Acho que não é pra dividir por 3
#print('Approximation Diameter:', nx.approximation.diameter(G))
print('Diameter:', nx.diameter(G, eccentricity))
#eccentricity = nx.eccentricity(G)
#print(nx.dijkstra_path(G, '9056', '12963'))
#print(sorted(eccentricity.values())[len(eccentricity)//10])