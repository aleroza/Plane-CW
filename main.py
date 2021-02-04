import math
import random
import json


class Node:
    def __init__(self, lb, tb):
        self.val = None
        self.mb = None
        self.lb = lb  # prev left branch
        self.tb = tb  # prev top branch
        self.opt = None

    def calculate_mb(self):
        self.mb = math.sqrt(self.tb[0] ** 2 + self.lb[0] ** 2)


def algorithm(cur_node, v, prev_node):
    if cur_node.val == None or cur_node.val>v:
        cur_node.val=v
        cur_node.opt=prev_node
    elif cur_node.val<v:
        return

    if cur_node.lb != None:
        algorithm(cur_node.lb[0], cur_node.lb[1]+v, cur_node)
    if cur_node.tb != None:
        algorithm(cur_node.tb[0], cur_node.tb[1]+v, cur_node)
    


def gen_rawdata(y, x):
    rawdata = []
    for row in range(y):
        cur_row = []
        for col in range(x):
            cur_row.append([random.randint(1, 10), random.randint(1, 10)])
        rawdata.append(cur_row)
    return rawdata


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
                tb = None
            else:
                tb = [nodes[y - 1][x], col[1]]
            cur_row.append(Node(lb, tb))
        nodes.append(cur_row)
    return nodes

def print_nodes(nodes):
    for row in nodes:
        for col in row:
            print(f"[{col.val}]", end="")
        print("")
    print("\n")

def optimal_path(cur_node):
    if cur_node.opt == None:
        return
    print(cur_node.val)
    optimal_path(cur_node.opt)

def main():
    x,y=7,6;

    rawdata=gen_rawdata(y,x)

    with open('example_data.json', 'r') as file:
        rawdata=json.load(file)

    nodes = gen_nodes(rawdata)
    nodes[y-1][x-1].val=0

    print_nodes(nodes)

    algorithm(nodes[y-1][x-1],0, None)

    print_nodes(nodes)

    optimal_path(nodes[0][0])



if __name__ == '__main__':
    main()
