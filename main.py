import math
import random


class Node:
    def __init__(self, lb, tb):
        self.val = None
        self.mb = None
        self.lb = lb  # prev left branch
        self.tb = tb  # prev top branch

    def calculate_mb(self):
        self.mb = math.sqrt(self.tb[0] ** 2 + self.lb[0] ** 2)


def algorithm(cur_node, v):
    cur_node.val=v
    print(cur_node.lb[0])
    if cur_node.lb != None:
        algorithm(cur_node.lb[0], cur_node[1]+v)
        

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


def main():
    x,y=6,5;

    nodes = gen_nodes(gen_rawdata(y,x))
    print(len(nodes),len(nodes[0]))  
    nodes[y-1][x-1].val=0
    nodes = algorithm(nodes[y-1][x-1],0)
    
    
  
    # for row in nodes:
        # for col in row:
            # print(f"[{col.lb} {col.tb}]", end="")
        # print("")
        
    #g = gen_rawdata(6, 5)
    #for row in g:
    #    print(row)
    #print("")
    #nl = gen_nodes(g)



if __name__ == '__main__':
    main()
