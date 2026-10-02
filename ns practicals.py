import networkx as nx
import matplotlib.pyplot as plt

#importing datasets
G_karate=nx.karate_club_graph()
G_dolphin=nx.read_gml("dolphins.gml")
G_football=nx.read_gml("football.gml")
G_polbooks=nx.read_gml("polbooks.gml")


for u, v in G_karate.edges():        #assigning weights
    G_karate[u][v]['weight']=1

for u, v in G_dolphin.edges():        #assigning weights
    G_dolphin[u][v]['weight']=1

for u, v in G_football.edges():        #assigning weights
    G_football[u][v]['weight']=1

for u, v in G_polbooks.edges():        #assigning weights
    G_polbooks[u][v]['weight']=1

def node_strength(G, node, weight='weight'):     #function to calculate strength of node
    return G.degree(node, weight=weight)   #returns weighted degree of the node

def c_index_centrality(G, node, weight='weight'):  #functn to calculate c-index centrality of a ndoe
    scores=[]     
    for n in G.neighbors(node):     #loops over every neighbor of the node 
        w=G[node][n][weight]   #edge weight bw the node and this neighbor 'n'
        s=node_strength(G, n, weight)   #node strength of the neighbor 'n'
        scores.append(w*s)  #stores (edge weight x neigbors strength)

    scores.sort(reverse=True)    #sort the scores ind escending order
    c=0         #initial c-index value
    for i, val in enumerate(scores, start=1):   #i=rank, val=actual score
        if val >= i:
            c=i
        else:
            break
    return c

c_index_values = {node: c_index_centrality(G_karate, node) for node in G_karate.nodes()}

print("c-index of karate graph nodes: ")
for node, val in sorted(c_index_values.items(), key=lambda x: -x[1]):
    print(f"Node {node}: C-index = {val}")

c_index_values2 = {node: c_index_centrality(G_dolphin, node) for node in G_dolphin.nodes()}

print("\nc-index for dolphin graph nodes: ")
for node, val in sorted(c_index_values2.items(), key=lambda x: -x[1]):
    print(f"Node {node}: C-index = {val}")

c_index_values3 = {node: c_index_centrality(G_football, node) for node in G_football.nodes()}

print("\nc-index for football graph nodes: ")
for node, val in sorted(c_index_values3.items(), key=lambda x: -x[1]):
    print(f"Node {node}: C-index = {val}")

c_index_values4 = {node: c_index_centrality(G_polbooks, node) for node in G_polbooks.nodes()}

print("\nc-index for polbooks graph nodes: ")
for node, val in sorted(c_index_values4.items(), key=lambda x: -x[1]):
    print(f"Node {node}: C-index = {val}")


degree_values = nx.degree_centrality(G_karate)
degree_values2 = nx.degree_centrality(G_dolphin)
degree_values3 = nx.degree_centrality(G_football)
degree_values4 = nx.degree_centrality(G_polbooks)

print("\nDegree centrality of karate graph nodes: ")
for node, val in sorted(degree_values.items(), key=lambda x: -x[1]):
    print(f"Node {node}: Degree centrality = {val:.4f}")

print("\nDegree centrality for dolphin graph nodes: ")
for node, val in sorted(degree_values2.items(), key=lambda x: -x[1]):
    print(f"Node {node}: Degree centrality = {val:.4f}")

print("\nDegree centrality for football graph nodes: ")
for node, val in sorted(degree_values3.items(), key=lambda x: -x[1]):
    print(f"Node {node}: Degree centrality = {val:.4f}")

print("\nDegree centrality for polbooks graph nodes: ")
for node, val in sorted(degree_values4.items(), key=lambda x: -x[1]):
    print(f"Node {node}: Degree centrality = {val:.4f}")


top5 = sorted(degree_values4.items(), key=lambda x: -x[1])[:15]
nodes = [f"Node {n}" for n, _ in top5]
values = [v for _, v in top5]

plt.figure(figsize=(16, 8))
plt.bar(nodes, values, color='orange')
plt.ylabel("Degree Centrality")
plt.xticks(rotation=45, ha='right')
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.title("Top 15 nodes by Degree Centrality — Polbook graph")
plt.show()
