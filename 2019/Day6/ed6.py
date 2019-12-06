import networkx as nx

f = open("input", "r")

orbits = [x.strip('\n').split(')') for x in f.readlines()]

def part1():
    G = nx.DiGraph()

    for o in orbits:
        G.add_node(o[0])
        G.add_node(o[1])
        G.add_edge(o[1], o[0])

    total = 0
    for n in G.nodes:
        if n != 'COM':
            # There is just one path, so the shortest path to COM is fine
            total += nx.shortest_path_length(G, n, 'COM')

    print (total)

def part2():
    G = nx.Graph()
    target = None
    source = None
    for o in orbits:
        G.add_node(o[0])
        G.add_node(o[1])
        G.add_edge(o[1], o[0])
        if o[1] == 'SAN':
            target = o[0]
        if o[1] == 'YOU':
            source = o[0] 

    path_size = nx.shortest_path_length(G, source, target)
    print (path_size)

part1()
part2()
f.close()