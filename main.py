from file_reader import read_file
from metrics_plot import *
from metrics_calculation import *


G = read_file('Email-EuAll.txt')

calculate_metrics(degrees(G), 'Grau')
calculate_metrics(connected_component_sizes(G), 'Tamanho das CC')
# calculate_metrics(node_clusterization(G), 'Clusterização')  # todo pegar a clusterização global pelos triângulos
# calculate_metrics(distances(G), 'Distância')
# calculate_metrics(approximate_distance(G, nrand=10000), 'Teste distância')

plot_ccdf(connected_component_sizes(G))
