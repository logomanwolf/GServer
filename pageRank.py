import sys
import networkx as nx

if __name__ == '__main__':
    if sys.argv.__len__()<2:
        print('The format is "python pageRank.py data.edgelist [{1:2}]"')
    else:
        filename = sys.argv[1]

    graph = nx.read_edgelist(filename)
    # p = PageRank(graph, isDirected)
    # p.rank()
    # sorted_r = sorted(p.ranks.items(), key=operator.itemgetter(1), reverse=True)
    if sys.argv.__len__()==3:
        personalization=sys.argv[2]
        vec=eval(personalization)
        pr=nx.pagerank(graph,personalization=vec)
    else:
        pr=nx.pagerank(graph)
    pagerank=sorted(pr.items(),key=lambda item:item[1],reverse=True)
    print(pagerank)

 
