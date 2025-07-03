import networkx as nx
import matplotlib.pyplot as plt
import csv
import numpy as np

# Read the data from the CSV file and create a directed graph
obj = csv.reader(open('data.csv', 'r'))
l = []  # nodelist
e = []  # edgelist
next(obj)
G = nx.DiGraph()
for row in obj:
    b = row[1][0:11].upper()
    l.append(b)
    for i in row[2:]:
        if i == '':
            continue
        e.append((b, i[-11:].upper()))
G.add_nodes_from(l)
G.add_edges_from(e)

# Store the number of inlinks for each node
inlinks = {}
for i in l:
    inlinks[i] = len(list(G.in_edges(i)))

# Make a graph of indegrees on x axis and percentage of nodes with that indegree on y axis
indegree_counts = {}
for i in inlinks.values():
    if i in indegree_counts:
        indegree_counts[i] += 1
    else:
        indegree_counts[i] = 1

x = list(indegree_counts.keys())
y = [i for i in indegree_counts.values()]

# Fit a polynomial curve to the data points
degree = 3  # Choose the degree of the polynomial curve
p = np.polyfit(x, y, degree)
f = np.poly1d(p)

# Generate values for the curve
x_fit = np.linspace(min(x), max(x), 100)
y_fit = f(x_fit)

# Plot the scatter plot and the curve of best fit
plt.scatter(x, y, label='Data')
plt.plot(x_fit, y_fit, color='red', label='Curve of Best Fit')
plt.xlabel('Indegree')
plt.ylabel('Number of Nodes')
plt.title('Indegree Distribution with Curve of Best Fit')
plt.legend()
plt.show()