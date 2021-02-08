import json
import random
from time import sleep

import matplotlib.pyplot as plt
import networkx as nx
import main
import numpy as np
from itertools import count


# for x in range(x):
#   for y in range(y):
#

# G.add_node("n00", weight=9)
# G.add_node("n01", weight=3)
# G.add_node("n10", weight=4)
# G.add_node("n11", weight=0)

# G.add_edge("n11", "n01", weight=3)
# G.add_edge("n11", "n10", weight=4)
# G.add_edge("n01", "n00", weight=6)
# G.add_edge("n10", "n00", weight=7)

def draw():
	plt.figure()
	x, y = 5, 4
	with open('example_data.json', 'r') as file:
		rawdata = np.array(json.load(file))

	nodes = main.gen_nodes(rawdata)
	main.algorithm(nodes[y - 1][x - 1], 0, None)
	G = nx.grid_2d_graph(x, y)

	pos = dict((n, n) for n in G.nodes())
	for yy, nodes_row in enumerate(nodes):
		for xx, node in enumerate(nodes_row):
			if node.lb is not None:
				G[xx, yy][xx - 1, yy]['weight'] = node.lb[1]
			if node.db is not None:
				G[xx, yy][xx, yy - 1]['weight'] = node.db[1]
	route = main.optimal_path(nodes[0][0], [], nodes)
	colors = []
	for node in G.nodes:
		if node in [(0, 0), (x - 1, y - 1)]:
			colors.append("red")
		elif node in route:
			colors.append("green")
		else:
			colors.append("gray")

	weights = nx.get_edge_attributes(G, "weight")
	labels = dict(((i, j), f"{i},{j}") for i, j in G.nodes())
	# weight_labels = dict(((i, j), f"{i},{j}") for i, j in G.nodes())
	nx.draw_networkx(G, pos, with_labels=True, labels=labels, node_size=500)
	nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)

	plt.axis('off')

	anodes = [(xx, yy) for xx in range(x) for yy in range(y)]
	aedges = []
	for i, node in enumerate(anodes):
		if i + y <= len(anodes) - 1:
			aedges.append((node, anodes[i + y]))
		if i + 1 <= len(anodes) - 1 and node[0] == anodes[i + 1][0]:
			aedges.append((node, anodes[i + 1]))
	sleep(2)
	plt.figure()
	D = nx.DiGraph()
	D.add_nodes_from(G.nodes)
	D.add_edges_from(G.edges)
	D.remove_edges_from([edge for edge in D.edges if edge not in route])
	nx.draw_networkx(G, pos, with_labels=True, labels=labels, node_size=500, node_color=colors)
	nx.draw_networkx_edges(G,pos, arrows=True, arrowstyle="fancy")
	plt.show()


# x,y=7,6
# for row in range(y):
#       cur_row = []
#       for col in range(x):
#           cur_row.append([random.randint(1, 10), random.randint(1, 10)])
#       rawdata.append(cur_row)


if __name__ == '__main__':
	draw()
