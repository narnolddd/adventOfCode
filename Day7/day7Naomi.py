import re
import networkx as nx
from collections import defaultdict
file = "Day7/input.txt"

line = "Step (?P<src>\w{1}) must be finished before step (?P<dst>\w{1}) can begin."
p= re.compile(line)

# Make a dependency graph of the tasks A -> B if B dependent on A
H=nx.DiGraph()
with open(file,'r') as f:
    for l in f:
        match = p.match(l.strip()).groupdict()
        H.add_edge(match['src'],match['dst'])

workers = ["." for i in range(5)]

# Returns a string of letter repeated 60+number of letter times
def letter2time(letter):
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(0,26):
        if alphabet[i]==letter:
            return letter*(61+i)+"."

# Part 1 & 2 in one go
second=0
order=""
while True:
    for w in workers:
        if second > 0 and w[second]== ".":
            if w[second-1]!=".":
                H.remove_node(w[second-1])
    if second>0 and all([w[second]=="." and w[second-1]=="." for w in workers]):
        break
    # if task has no indegree then it is available
    available_tasks = [node for node in H.nodes() if H.in_degree(node)==0 and all([w[second]!= node for w in workers])]
    if len(available_tasks)!=0:
        sortedtasks=sorted(available_tasks)
        for w in range(len(workers)):
            if len(sortedtasks)==0:
                if workers[w][second]==".":
                    workers[w]+="."
            else:
                if workers[w][second]==".":
                    workers[w]=workers[w][:-1]
                    workers[w]+=letter2time(sortedtasks[0])
                    order+=sortedtasks[0]
                    sortedtasks.pop(0)
    else:
        for w in range(len(workers)):
            if workers[w][second]==".":
                workers[w]+="."
    second+=1

print(second-1,order)
