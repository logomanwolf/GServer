import sys
import networkx as nx
import json

if __name__ == '__main__':
    if sys.argv.__len__()<2:
        print('The format is "python pageRank.py data.edgelist [{1:2}]"')
    else:
        filename = sys.argv[1]

    if filename.find('weight')==-1:
        graph = nx.read_edgelist(filename)
    else:
        graph  = nx.read_weighted_edgelist(filename)
    # p = PageRank(graph, isDirected)
    # p.rank()
    # sorted_r = sorted(p.ranks.items(), key=operator.itemgetter(1), reverse=True)
    if sys.argv.__len__()==3:
        personalization=sys.argv[2]
        vec=eval(personalization)
        pr=nx.pagerank(graph,personalization=vec)
    else:
        pr=nx.pagerank(graph)
    pagerank = sorted(pr.items(), key=lambda item: item[1], reverse=True)
    # pagerank = sorted(pr.items(), key=lambda item: '{:.3f}'.format(item[1]), reverse=True) 
    # data = [tuple((d[0], '{:.6f}'.format(d[1]))) for d in pagerank]
    # output = dict(data)
    jsonStr = json.dumps(pagerank)
    print(jsonStr)

 
