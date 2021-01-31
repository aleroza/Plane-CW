import math
import random


class Node:
    def __init__(self, lb, tb):
        self.val = None
        self.mb = None
        self.lb = lb  # "next" left branch
        self.tb = tb  # "next" top branch

    def calculate_mb(self):
        self.mb = math.sqrt(self.tb[0] ** 2 + self.lb[0] ** 2)


def gen_rawdata(x, y):
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
                lb = [col[0], cur_row[x - 1]]
            if y == 0:
                tb = None
            else:
                tb = [col[1], nodes[y - 1][x]]
            cur_row.append(Node(lb, tb))
        nodes.append(cur_row)
    return nodes


def main():
    g = gen_rawdata(6, 5)
    for row in g:
        print(row)
    print("")
    nl = gen_nodes(g)
    for row in nl:
        for col in row:
            print(f"[{col.lb} {col.tb}]", end="")
        print("")


if __name__ == '__main__':
    main()
