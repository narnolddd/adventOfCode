import networkx as nx
file = "./2020/Day07/mattinput.txt"

bag_contain_bag = {}
with open(file, 'r') as f:
    for row in f:
        k, v = row.strip().split('contain')
        k = k.replace('bags', '').strip()
        v = [i.strip()
             for i in list(filter(None, v.rstrip(v[-1]).replace(',', '').replace('bags', 'bag').replace('bag', 'bags').split('bags')))]
        w = {}
        for i in v:
            if 'no' in i:
                w['other'] = 0
            else:
                a, b = i.split(' ', 1)
                w[b] = int(a)

        bag_contain_bag[k] = w

G = nx.DiGraph()

for bag, contain in bag_contain_bag.items():
    G.add_node(bag)
for bag, contain in bag_contain_bag.items():
    for bag_in, n in contain.items():
        G.add_edge(bag, bag_in, weight=n)

# 1
my_bag = "shiny gold"
bag_n = 0
for bag in G.nodes:
    if bag == my_bag:
        continue
    if nx.has_path(G, bag, my_bag):
        bag_n += 1

print(bag_n)

# 2
bags_needed_n = 0


def compute_needed_bags(bags):
    global bags_needed_n
    for bag, opt in bags.items():
        bag_neighbours = nx.neighbors(G, bag)
        for neighbour in bag_neighbours:
            weight = G[bag][neighbour]['weight'] * opt['weight']
            bags_needed_n += weight
            compute_needed_bags({neighbour: {'weight': weight}})

    return bags_needed_n


print(compute_needed_bags({my_bag: {'weight': 1}}))
