import main
import networkx as nx
import matplotlib.pyplot as plt


def draw():
	x, y = 7, 6
	rawdata = main.gen_rawdata(x, y)
	nodes = main.gen_nodes(rawdata)
	main.prealg(nodes)

	g_nodes = [(xx, yy) for xx in range(x) for yy in range(y)]
	g_edges = []
	for i, node in enumerate(g_nodes):
		if i + y <= len(g_nodes) - 1:
			g_edges.append((node, g_nodes[i + y]))
		if i + 1 <= len(g_nodes) - 1 and node[0] == g_nodes[i + 1][0]:
			g_edges.append((node, g_nodes[i + 1]))
	G = nx.DiGraph()
	G.add_nodes_from(g_nodes)
	G.add_edges_from(g_edges)

	pos = dict((n, n) for n in G.nodes())
	# for yy, nodes_row in enumerate(nodes):
	# 	for xx, node in enumerate(nodes_row):
	# 		if node.lb is not None:
	# 			G[xx, yy][xx - 1, yy]['weight'] = node.lb[1]
	# 		if node.db is not None:
	# 			G[xx, yy][xx, yy - 1]['weight'] = node.db[1]
	# weights = nx.get_edge_attributes(G, "weight")
	labels = dict(((i, j), f"{i},{j}") for i, j in G.nodes())

	nx.draw_networkx(G, pos, with_labels=True, labels=labels, node_size=500)
	nx.draw_networkx_edge_labels(G, pos)

	plt.axis('off')
	plt.show()


if __name__ == '__main__':
	draw()
