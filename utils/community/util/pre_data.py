import numpy as np
import networkx as nx  
groundTruth="E:/Download/social_network/email-Eu-core-department-labels.txt/email-Eu-core-department-labels.txt"
edgeList="E:\Download\social_network\email-EuAll.txt\Email-EuAll.txt"
def preData():
    G=nx.read_edgelist(edgeList)
    size=len(nx.nodes(G))
    edges=G.edges()
    # labels=map(change,np.loadtxt(directory+edgeList))
    # for line in nx.generate_edgelist(G)
    new_array=np.zeros((size,size),dtype="int8")
    for line in edges:
        new_array[int(line[0])][int(line[1])]=1
        new_array[int(line[1])][int(line[0])]=1
    return new_array 
def preLabel():
    pass
if __name__ == "__main__":
    preData()