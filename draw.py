import json
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

import main


def draw():
	plt.figure("Условие")
	x, y = 7, 6
	nodes = main.gen_nodes(main.gen_rawdata(x,y))

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
	fst_colors = []
	for node in G.nodes:
		if node in [(0, 0), (x - 1, y - 1)]:
			fst_colors.append("red")
		else:
			fst_colors.append("teal")
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
	weight_labels = dict(((i, j), f"{nodes[j][i].val}") for i, j in G.nodes())
	nx.draw_networkx(G, pos, with_labels=True, labels=labels, node_size=500, node_color=fst_colors, node_shape="s")
	nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)

	plt.axis('off')

	plt.figure("Решение")
	plt.axis('off')
	D = nx.grid_2d_graph(x, y)
	nx.draw_networkx_nodes(D, pos, route)
	nx.draw_networkx(D, pos, with_labels=True, labels=weight_labels, node_size=500, node_color=colors, node_shape="s")
	nx.draw_networkx_edge_labels(D, pos, edge_labels=weights)
	plt.show()


if __name__ == '__main__':
	draw()
