import re
import networkx as nx
file = "Day7/input.txt"

line = "Step (?P<src>\w{1}) must be finished before step (?P<dst>\w{1}) can begin."
p= re.compile(line)

G=nx.DiGraph()
with open(file,'r') as f:
    for l in f:
        match = p.match(l.strip()).groupdict()
        G.add_edge(match['src'],match['dst'])

order=""
while True:
    available_tasks = [node for node in G.nodes() if G.in_degree(node)==0 ]
    if len(available_tasks)==0:
        break
    first = min(available_tasks)
    order+=first
    G.remove_node(first)

print(order)
