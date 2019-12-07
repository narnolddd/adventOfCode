import networkx as nx
from collections import defaultdict

file = "Day6/inputnaomi.txt"

with open(file,'r') as f:
    data = f.readlines()
    f.close()

G = nx.Graph()

# Construct directed graph A->B if A directly orbited by B
for row in data:
    src,dst=row.strip().split(')')
    G.add_edge(src,dst)

def BFS(startnode, distance, visited_nodes,distances):
    neighbours = G.neighbors(startnode)
    distance+=1
    for n in neighbours:
        if visited_nodes[n]==True:
            continue
        visited_nodes[n]=True
        distances[n]=distance
        BFS(n,distance,visited_nodes,distances)

distances_from_origin={}

BFS("COM",0,defaultdict(lambda: False),distances_from_origin)
no_orbits=sum(distances_from_origin.values())

print("Part 1: "+str(no_orbits))

distances_from_you={}
BFS("YOU",0,defaultdict(lambda: False),distances_from_you)
print("Part 2: "+str(distances_from_you["SAN"]-2))
