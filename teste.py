import networkx as nx
import matplotlib.pyplot as plt


def save_graph(graph, file_name):
    # initialze Figure
    plt.figure(num=None, figsize=(20, 20), dpi=80)
    plt.axis('off')
    fig = plt.figure(1)
    pos = nx.kamada_kawai_layout(graph)
    #nx.draw_networkx_nodes(graph, pos)
    #nx.draw_networkx_edges(graph, pos)
    #nx.draw_networkx_labels(graph, pos)
    nx.draw_kamada_kawai(graph)

    cut = 1.1
    xmin = cut * min(xx for xx, yy in pos.values())
    ymin = cut * min(yy for xx, yy in pos.values())
    xmax = cut * max(xx for xx, yy in pos.values())
    ymax = cut * max(yy for xx, yy in pos.values())
    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)

    plt.savefig(file_name, bbox_inches="tight")
    plt.close()
    del fig

#G = nx.petersen_graph()
G = nx.read_graphml(r'files\mixed.species_brain_1.graphml')

save_graph(G, 'test_kamada_kawai.pdf')
#subax1 = plt.subplot(121)
#nx.draw(G, with_labels=True, font_weight='bold')
#subax2 = plt.subplot(122)
#nx.draw_shell(G, with_labels=True, font_weight='bold')

#plt.show()

#

#G