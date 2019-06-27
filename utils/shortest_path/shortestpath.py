import numpy as np
import networkx as nx 
import sys
# 最短路径长度
shortest_path=float("inf")
# 一共的节点数
n=3
# 目的地
des=1
# 用来存储是否遍历过
book=np.zeros((1,n),dtype=int)[0]
# 距离表
e=[[0,2,1],[2,0,1],[1,1,0]]
# 当前队列里存储的路径回溯
currQue=[]
# 最短路径的回溯表
shortestQue=[]
#  cur-当前所在城市编号，dis-当前已走过的路径
def init(nodes_num,destination,distance,start):
    global n,des,e,book
    n=nodes_num
    des=destination
    e=distance
    book=np.zeros((1,n),dtype=int)[0]
    book[start]=1

def dfs(cur, dis):
    global shortest_path,shortestQue,currQue
    global book
    # 若当前路径已比之前找到的最短路大，没必要继续尝试（一个小优化，可以不写）
    if dis > shortest_path:
        return;
    # 当前已到达目的城市，更新shortest_path
    if(cur == des):
        if dis < shortest_path:
            shortest_path = dis;
            shortestQue=[]
            shortestQue.append(currQue.copy())
        elif dis == shortest_path:
            shortestQue.append(currQue.copy())
        return;
    
    # 对1~n号城市依次尝试
    for i in range(0,n,1):
        # 若cur与i可达，且i没有在已走过的路径中
        if e[cur][i] != float("inf") and book[i] == 0: 
            # 标记i为已在路径中
            book[i] = 1;
            currQue.append(i) 
            # 继续搜索
            dfs(i, dis+e[cur][i]);
            # 对从i出发的路径探索完毕，取消标记
            book[i] = 0; 
            currQue.remove(i)
            print(i)
def preData():
    G=nx.read_edgelist("E:/Download/social_network/email-Eu-core.txt/email-Eu-core.txt")
    size=len(nx.nodes(G))
    edges=G.edges()
    # labels=map(change,np.loadtxt(directory+edgeList))
    # for line in nx.generate_edgelist(G)
    # new_array=np.zeros((size,size),dtype=int)
    new_array=[]
    for i in range(size):
        new_array.append([float("inf")]*size)
    for line in edges:
        new_array[int(line[0])][int(line[1])]=1
        new_array[int(line[1])][int(line[0])]=1
    return new_array
if __name__ == "__main__":
    sys.setrecursionlimit(2000)
    adj_array=preData()
    init(len(adj_array),290,adj_array,12)
    dfs(12,0)
    print(shortest_path)
    print(shortestQue)