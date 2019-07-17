import numpy as np
import networkx as nx 
import sys
import json

def getShortestPath(res, des, filename):
    if filename.find('weight')==-1:
        G = nx.read_edgelist(filename)
    else:
        G=nx.read_weighted_edgelist(filename)
    return nx.all_shortest_paths(G,res,des)

if __name__ == "__main__":
    if sys.argv.__len__()<4:
        print("The format should be 'python shortestPath.py data.edgelist 1 2'")
    else:
        start=sys.argv[2]
        end=sys.argv[3]
        filename=sys.argv[1]
        shortest_paths=getShortestPath(start,end,filename)
        data=[p for p in shortest_paths]
        jsonStr = json.dumps(data)
        print(jsonStr)  