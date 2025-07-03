import random
import csv
import networkx as nx

obj=csv.reader(open('data.csv','r'))
l=[] #nodelist
e=[] #edgelist
next(obj) 
G=nx.DiGraph() #directed graph
for row in obj:
    b=row[1][0:11].upper() 
    l.append(b) 
    for i in row[2:]:
        e.append((b,i[-11:].upper())) 
G.add_nodes_from(l) #adding nodes to graph
G.add_edges_from(e) #adding edges to graph

def random_walk(G):
    node=G.nodes() 
    coins={} 
    for i in node:
        coins[i]=0 
    n=random.choice(list(node)) 
    coins[n]+=1
    x=G.out_edges(n) 
    c=0
    while c<300000:
        if len(x)==0:
            m=random.choice(list(node))
        else:
            n1=random.choice(list(x))
            m=n1[1] 
        coins[m]+=1   
        x=G.out_edges(m) 
        c+=1 
    return coins 
sorted_by_values = sorted(random_walk(G).items(), key=lambda item: item[1]) 
sorted_dict = {key: value for key, value in sorted_by_values} 


# function to print top 10 students according to pagerank
def top_ten(sorted_dict): 
    f=list(sorted_dict.keys())
    g=list(sorted_dict.values())
    for i in range(-1,-12,-1):
        if f[i]!='':
            print(f[i],g[i])

top_ten(sorted_dict)