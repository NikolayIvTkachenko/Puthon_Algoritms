import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node("Mike")
G.add_nodes_from(["Amine", "Wassim", "Nick"])

G.add_edge("Mike", "Amine")
G.add_edge("Amine", "Imran")

print(list(G.nodes))
print(list(G.edges))

#================

vertices = range(1, 10)
edges = [(7, 2), (2, 3), (7, 4), (4, 5), (7, 3), (7, 5), (1, 6), (1, 7), (2, 8), (2, 9)]
G2 = nx.Graph()
G2.add_nodes_from(vertices)
G2.add_edges_from(edges)
print(G2)
print(list(G2.nodes))
print(list(G2.edges))

nx.draw(G2, with_labels=True, node_color='y', node_size=800)
#https://habr.com/ru/companies/skillfactory/articles/721838/

import networkx as nx
import matplotlib.pyplot as plt

vertices = range(1, 10)
edges = [(7, 2), (2, 3), (7, 4), (4, 5), (7, 3), (7, 5), (1, 6), (1, 7), (2, 8), (2, 9)]
G2 = nx.Graph()
G2.add_nodes_from(vertices)
G2.add_edges_from(edges)
print(G2)
print(list(G2.nodes))
print(list(G2.edges))

nx.draw(G2, with_labels=True, node_color='y', node_size=800)

nx.degree_centrality(G2)
nx.betweenness_centrality(G2)
nx.closeness_centrality(G2)
centrality = nx.eigenvector_centrality(G2)
sorted((v, '{:0.2f}'.format(c)) for v, c in centrality.items())

graph={'Amin' : {'Wasim', 'Nick', 'Mike'},
       'Wasim': {'Imran', 'Amin'},
       'Imran': {'Wasim', 'Faras'},
       'Faras': {'Imran'},
       'Mike': {'Amin'},
       'Nick': {'Amin'}}


def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbours = graph[node]
            for neighbour in neighbours:
                queue.append(neighbour)

    return visited

bfs(graph, 'Amin')
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

dfs(graph, 'Amin')

import networkx as nx
import matplotlib.pyplot as plt

vertices = range(1, 10)
edges = [(7, 2), (2, 3), (7, 4), (4, 5), (7, 3), (7, 5), (1, 6), (1, 7), (2, 8), (2, 9)]

G3 = nx.Graph()
G3.add_nodes_from(vertices)
G3.add_edges_from(edges)
pos=nx.spring_layout(G3)

nx.draw_networkx_nodes(G3, pos, nodelist=[1, 4, 3, 8, 9], label=True, node_color='r', node_size=1300)

nx.draw_networkx_nodes(G3, pos, nodelist=[2, 5, 6, 7], label=True, node_color='r', node_size=1300)

nx.draw_networkx_edges(G3, pos, edges, width=3, alpha=0.5, edge_color='b')
labels={}
labels[1]=r'1 NF'
labels[2]=r'2 F'
labels[3]=r'3 NF'
labels[4]=r'4 NF'
labels[5]=r'5 F'
labels[6]=r'6 6F'
labels[7]=r'7 F'
labels[8]=r'8 NF'
labels[9]=r'9 NF'
nx.draw_networkx_labels(G3, pos, labels, font_size=16)


#k means
from sklearn import cluster
import pandas as pd
import numpy as np

dataset = pd.DataFrame({
'x':[11, 21, 28, 17, 29, 33, 24, 45, 45,52, 51, 52, 55, 53, 55, 61, 62, 70, 72, 10],
'y':[39, 36, 30, 52, 53, 46, 55, 59, 63, 70, 66, 63, 58, 23, 14, 8, 18, 7, 24, 10]
})

mKmeans = cluster.KMeans(n_clusters=2)
mKmeans.fit(dataset)

centroids = mKmeans.cluster_centers_
labels=mKmeans.labels_

print(labels)
print(centroids)

import matplotlib.pyplot as plt
plt.scatter(dataset['x'], dataset['y'], s=10)
plt.scatter(centroids[0], centroids[1], s=100)
plt.show()