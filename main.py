import math
import json
import numpy as np


class Node:
	def __init__(self, lb, db):
		self.val = None
		self.mb = None
		self.lb = lb  # prev left branch
		self.db = db  # prev down branch
		self.opt = []

	def calculate_mb(self):
		self.mb = math.sqrt(self.db[0] ** 2 + self.lb[0] ** 2)

	def __str__(self): return f"Нода с весом {self.val}"


def algorithm(cur_node, v, prev_node):
	if prev_node is None:
		cur_node.val = v
	elif cur_node.val is None or cur_node.val > v:
		cur_node.val = v
		cur_node.opt = [prev_node]
	elif cur_node.val == v and not cur_node.opt[0] == prev_node:
		cur_node.opt.append(prev_node)
	elif cur_node.val < v:
		return

	if cur_node.lb is not None:
		algorithm(cur_node.lb[0], cur_node.lb[1] + v, cur_node)
	if cur_node.db is not None:
		algorithm(cur_node.db[0], cur_node.db[1] + v, cur_node)


def gen_rawdata(x, y):
	return np.random.randint(1, 10, (y, x, 2), int)


def gen_nodes(rawdata):
	nodes = []
	for y, row in enumerate(rawdata):
		cur_row = []
		for x, col in enumerate(row):
			if x == 0:
				lb = None
			else:
				lb = [cur_row[x - 1], col[0]]
			if y == 0:
				db = None
			else:
				db = [nodes[y - 1][x], col[1]]
			cur_row.append(Node(lb, db))
		nodes.append(cur_row)
	return nodes


def print_nodes(nodes):
	for row in nodes:
		for col in row:
			print(f"[{col.val}]", end="")
		print("")
	print("\n")


def optimal_path(cur_node, opt_indexes, nodes):
	if cur_node.opt == [None]:
		return
	for path in cur_node.opt:
		[opt_indexes.append((node_row.index(path), y)) for y, node_row in enumerate(nodes) if path in node_row]
		optimal_path(path, opt_indexes, nodes)
	return opt_indexes


def prealg(nodes):
	nodes[len(nodes) - 1][len(nodes[0]) - 1].val = 0
	algorithm(nodes[len(nodes) - 1][len(nodes[0]) - 1], 0, None)


def main():
	x, y = 5, 4
	rawdata = gen_rawdata(x, y)

	# with open('example_data.json', 'r') as file:
	# 	rawdata = json.load(file)

	nodes = gen_nodes(rawdata)
	prealg(nodes)

	print_nodes(nodes)

	opt_indexes = optimal_path(nodes[0][0], [], nodes)
	print(len(opt_indexes), opt_indexes)


if __name__ == '__main__':
	main()
