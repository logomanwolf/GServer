import community
import networkx as nx
import matplotlib.pyplot as plt
import time
import sys

if __name__ == "__main__":
    if sys.argv.__len__()<2:
        console.log("The Format is 'python <filename>'")
    else:
        filename=sys.argv[1]
        if filename.endswith('.edgelist'):
            G=nx.read_edgelist(filename)
        #first compute the best partition
            partition = community.best_partition(G)
            print(partition)
            