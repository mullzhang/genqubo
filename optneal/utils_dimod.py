import json

import dimod
import networkx as nx
import matplotlib.pyplot as plt


def load_bqm(path_json):
    with open(path_json, 'r') as f:
        ser = json.load(f)
    return dimod.BinaryQuadraticModel.from_serializable(ser)


def save_bqm(path_json, bqm):
    with open(path_json, 'w') as f:
        json.dump(bqm.to_serializable(), f)


def load_sampleset(path_json):
    with open(path_json, 'r') as f:
        ser = json.load(f)
    return dimod.SampleSet.from_serializable(ser)


def save_sampleset(path_json, sampleset, aggregate=False):
    if aggregate:
        sampleset = sampleset.aggregate()

    with open(path_json, 'w') as f:
        json.dump(sampleset.to_serializable(), f)


def draw_bqm(bqm, pos_xshift_factor=0.6, pos_yshift_factor=0.6, save_path=None):
    graph = bqm.to_networkx_graph()
    positions = nx.layout.spring_layout(graph)

    nx.draw_networkx_nodes(graph, positions, node_size=500, node_color='white', edgecolors='black')

    line_styles = ['solid' if w['bias'] >= 0 else 'dashed' for i, j, w in graph.edges(data=True)]
    nx.draw_networkx_edges(graph, positions, style=line_styles)

    node_labels = {i: ('+' if w['bias'] > 0 else '') + str(w['bias'])
                   for i, w in graph.nodes(data=True) if w['bias'] != 0}
    node_positions = {k: (pos[0] * pos_xshift_factor, pos[1] * pos_yshift_factor) for k, pos in positions.items()}
    nx.draw_networkx_labels(graph, positions)
    nx.draw_networkx_labels(graph, node_positions, labels=node_labels)

    edge_labels = {(i, j): ('+' if w['bias'] > 0 else '') + str(w['bias'])
                   for i, j, w in graph.edges(data=True) if w['bias'] != 0}
    nx.draw_networkx_edge_labels(graph, positions, edge_labels=edge_labels)

    plt.axis('off')
    if save_path:
        plt.savefig(save_path)
    plt.show()
