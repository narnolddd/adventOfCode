import networkx as nx
from collections import defaultdict

file = "Day18/inputnaomi.txt"

with open(file,'r') as f:
    grid = f.readlines()
    f.close()

# Look for start point
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j]=="@":
            start = [i,j]
            break

# Get graph representation of maze
weights={}
visited=defaultdict(lambda : False)
pos=start

def possible_directions(x,y):
    possibles = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
    real_possibles = [p for p in possibles if grid[p[0]][p[1]]!='#' and visited[p]==False]
    return real_possibles

G=nx.Graph()

def traverse_maze(pos,weight,node):
    current_weight=weight
    current_node=node
    while True:
        visited[pos]=True
        dirs = possible_directions(pos[0],pos[1])
        if len(dirs)==0:
            return
        if len(dirs)>1:
            break
        d = dirs[0]
        current_weight+=1
        if grid[d[0]][d[1]]!='.':
            G.add_edge(current_node,grid[d[0]][d[1]])
            weights[(current_node,grid[d[0]][d[1]])]=current_weight
            weights[(grid[d[0]][d[1]],current_node)]=current_weight
            current_node = grid[d[0]][d[1]]
            current_weight=0
        pos=d
    for dir in dirs:
        traverse_maze(dir,current_weight+1,current_node)

traverse_maze((start[0],start[1]),0,'@')
print(G.edges())
print(weights)
