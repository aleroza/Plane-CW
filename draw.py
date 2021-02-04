import matplotlib.pyplot as plt
import networkx as nx


def main():
  G = nx.grid_2d_graph(7,6)
  # G.add_node("n00", weight=9)
  # G.add_node("n01", weight=3)
  # G.add_node("n10", weight=4)
  # G.add_node("n11", weight=0)

  # G.add_edge("n11", "n01", weight=3)
  # G.add_edge("n11", "n10", weight=4)
  # G.add_edge("n01", "n00", weight=6)
  # G.add_edge("n10", "n00", weight=7)

  # labels = {
  #   n: str(n) + '   ' + str(G.nodes[n]['weight']) 
  #   for n in G.nodes
  # }

  pos = dict( (n, n) for n in G.nodes() )
  labels = dict(((i, j), i + (1-1-j) * 1) for i, j in G.nodes())
  print(pos)
  print("\n")
  print(labels)
  weights = nx.get_edge_attributes(G, "weight")
  #nx.draw(G, with_labels=True, labels=labels)
  ebunch=["(0,0)","(0,1)"]
  G.remove_edges_from(ebunch)
  nx.draw_networkx(G, pos, with_labels=True, labels=labels)
  nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
  
  plt.axis('off')
  plt.show()

  # x,y=7,6
  # for row in range(y):
  #       cur_row = []
  #       for col in range(x):
  #           cur_row.append([random.randint(1, 10), random.randint(1, 10)])
  #       rawdata.append(cur_row)


if __name__ == '__main__':
    main()
