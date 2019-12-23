import re
from collections import defaultdict
import networkx as nx

file='Day20/testnaomi.txt'

with open(file,'r') as f:
    grid = f.readlines()
    f.close()

# make easier to get door names
grid_transposed=[]
for i in range(len(grid[0])):
    new_string = ''.join([row[i] for row in grid])
    grid_transposed.append(new_string)

portal_list = {}
portals = {}

m1, m2 = '\.(?P<door>[A-Z]{2})', '(?P<door>[A-Z]{2})\.'
p1 = re.compile(m1)
p2 = re.compile(m2)

for i in range(len(grid)):
    for m in p1.finditer(grid[i]):
        portal_list[(i,m.start())]= m.group().strip('.')
    for m in p2.finditer(grid[i]):
        portal_list[(i,m.end()-1)]= m.group().strip('.')

for i in range(len(grid_transposed)):
    for m in p1.finditer(grid_transposed[i]):
        portal_list[(m.start(),i)]= m.group().strip('.')
    for m in p2.finditer(grid_transposed[i]):
        portal_list[(m.end()-1,i)]= m.group().strip('.')

print(portal_list)
start = [k for k in portal_list.keys() if portal_list[k]=='AA'][0]

visited = defaultdict(lambda : False)

def possible_directions(x,y):
    possibles = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
    real_possibles = [p for p in possibles if grid[p[0]][p[1]]!='#' and not grid[p[0]][p[1]].isalpha() and visited[p]==False]
    return real_possibles

G=nx.Graph()
weights={}

def traverse_maze(pos,weight,node):
    current_weight=weight
    current_node=node
    while True:
        visited[pos]=True
        dirs = possible_directions(pos[0],pos[1])
        if len(dirs)==0:
            if pos in portal_list.keys() and current_weight>0:
                G.add_edge(current_node,portal_list[pos])
                if (current_node,portal_list[pos]) in weights.keys():
                    if weights[(current_node,portal_list[pos])] > current_weight:
                            weights[(current_node,portal_list[pos])]=current_weight
                            weights[(portal_list[pos],current_node)]=current_weight
                else:
                    weights[(current_node,portal_list[pos])]=current_weight
                    weights[(portal_list[pos],current_node)]=current_weight
                current_node = portal_list[pos]
                current_weight=0
            return
        if len(dirs)>1:
            break
        d = dirs[0]
        current_weight+=1
        if grid[d[0]][d[1]]!='.':
            G.add_edge(current_node,portal_list[pos])
            weights[(current_node,grid[d[0]][d[1]])]=current_weight
            weights[(grid[d[0]][d[1]],current_node)]=current_weight
            current_node = grid[d[0]][d[1]]
            current_weight=0
            return
        pos=d
    for dir in dirs:
        traverse_maze(dir,current_weight+1,current_node)

for pos in portal_list.keys():
    traverse_maze(pos,0,portal_list[pos])

print(weights)

visited=defaultdict(lambda : False)
distances = defaultdict(lambda : -1)
distances['AA']=0
def do_dijkstra(node):
    visited[node]=True
    for n in G.neighbors(node):
        if distances[n]>=0 and distances[node]+weights[(n,node)]>distances[n]:
            continue
        distances[n]=distances[node]+weights[(n,node)]
        if visited[n]==False:
            do_dijkstra(n)

do_dijkstra('AA')
print(distances)
