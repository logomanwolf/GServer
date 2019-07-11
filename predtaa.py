import networkx as nx
import networkx.readwrite.json_graph as json_graph
import json
with open("./data/demo.json", "r") as load_f:
    data = json.load(load_f)
    G=json_graph.node_link_graph(data)
    nx.write_edgelist(G,'data/demo.edgelist')