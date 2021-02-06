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


def algorithm(cur_node, v, prev_node):
	if cur_node.val is None or cur_node.val > v:
		cur_node.val = v
		cur_node.opt = [prev_node]
	elif cur_node.val == v:
		cur_node.opt.append(prev_node)
	elif cur_node.val < v:
		return

	if cur_node.lb is not None:
		algorithm(cur_node.lb[0], cur_node.lb[1] + v, cur_node)
	if cur_node.db is not None:
		algorithm(cur_node.db[0], cur_node.db[1] + v, cur_node)


def gen_rawdata(y, x):
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
	for row in nodes[::-1]:
		for col in row:
			print(f"[{col.val}]", end="")
		print("")
	print("\n")


def optimal_path(cur_node, opt_indexes, nodes):
	print(cur_node)
	if cur_node is None:
		return opt_indexes
	for y, path in enumerate(cur_node.opt):
		[opt_indexes.append((noderow.index(path), y)) for noderow in nodes if path in noderow]
		optimal_path(path, opt_indexes, nodes)


def main():
	x, y = 5, 4
	rawdata = gen_rawdata(y, x)

	with open('example_data.json', 'r') as file:
		rawdata = json.load(file)
	nodes = gen_nodes(rawdata)
	nodes[y - 1][x - 1].val = 0

	print_nodes(nodes)

	algorithm(nodes[y - 1][x - 1], 0, None)

	print_nodes(nodes)

	opt_indexes = []
	optimal_path(nodes[0][0], opt_indexes, nodes)


if __name__ == '__main__':
	main()
