import random
import csv
import networkx as nx
import numpy as np
import scipy as sp

obj=csv.reader(open('data.csv','r'))
l=[] #nodelist
e=[] #edgelist
next(obj) 
G=nx.DiGraph() #directed graph
for row in obj:
    b=row[1][0:11].upper() 
    l.append(b) 
    for i in row[2:]:
        if i=='': continue
        e.append((b,i[-11:].upper())) 
G.add_nodes_from(l) #adding nodes to graph
G.add_edges_from(e) #adding edges to graph

l = list(G.nodes())
n = len(l)

adj = []
for i in range(n):
    row = []
    for j in range(n):
        if G.has_edge(l[i], l[j]):
            row.append(1)
        else:
            row.append(0)
    adj.append(row)

adj = np.array(adj)
cnt = 0
for i in range(n):
    for j in range(n):
        if adj[i][j] == 0:
            row = np.delete(adj[i], j, axis=0)
            col = np.delete(adj[:,j], i, axis=0)
            A = np.delete(np.delete(adj, i, axis=0), j, axis=1)
            X = np.linalg.lstsq(A.T, col, rcond=None)[0]
            val = np.matmul(X,col)
            if val > 0:
                G.add_edge(l[i], l[j])
                cnt+=1
                print("Missing Link:", l[i], l[j])
print(cnt)
