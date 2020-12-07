import networkx as nx

def create_graph(fname):
	file = open(fname, 'r')
	graph = nx.DiGraph()
	for line in file.readlines():
		parts = line.split()
		external_color = " ".join(parts[:2])
		if external_color not in graph:
			graph.add_node(external_color) 

		for i in range(4, len(parts), 4):
			num = int(parts[i]) if parts[i] != 'no' else 0
			color = " ".join(parts[i+1: i+3])
			if color not in graph:
				graph.add_node(color)

			graph.add_edge(external_color, color, weight=int(num))
	file.close()
	return graph

g = create_graph("edinput.txt")

dest = "shiny gold"
total = 0
for node in g.nodes:
	if node == dest:
		continue
	try:
		path = nx.shortest_path(g, node, dest)
		total += 1
	except nx.exception.NetworkXNoPath as e:
		continue

print (total)

nodes = [(dest, 1)]
total = 0
while len(nodes):
	node = nodes.pop()
	neighbors = nx.neighbors(g, node[0])
	for neigh in neighbors:
		weight = g[node[0]][neigh]['weight'] * node[1]
		total += weight
		nodes.append((neigh, weight))
		
print(total)
