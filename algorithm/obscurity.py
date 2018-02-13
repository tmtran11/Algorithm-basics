import codecs
from itertools import combinations


def merge(g1, g2):
    return {u: max(i for i in (g1.get(u), g2.get(u)) if i) for u in g1.keys() | g2} # potential problem


film = codecs.open("/Users/FPTShop/Desktop/film", "r", encoding='utf-8')
lines = film.readlines()
f = {}  # film and it money
for x in lines:
    t = x[:-1].split('\t')
    f[(t[0], t[1])] = float(t[2])
actor = codecs.open("/Users/FPTShop/Desktop/actors", "r", encoding='utf-8')
lines = actor.readlines()
# should make the graph right here
a = {}  # actor and all film
r = {}  # film and all actor, with the film
for x in lines:
    t = x[:-1].split('\t')
    if t[0] not in a:
        a[t[0]] = []
    a[t[0]].append((t[1], t[2]))  # actor and film
    if (t[1], t[2]) not in r:
        r[(t[1], t[2])] = {}
    r[(t[1], t[2])].update({t[0]: f[(t[1], t[2])]})  # film and actor,weight

# is this n4? fix
g = {}
for this in a:
    g[this] = {}
    for film in a[this]:
        print(r[film])
        g[this] = merge(g[this], r[film])
# a graph with actor and other,weight
nodes = list(a.keys())
table = []
# table element: sum max weight


for r in range(0, len(nodes)):
    table.append([])
    for c in range(0, len(nodes)):
        if nodes[r] in g[nodes[c]]:
            table[r].append(g[nodes[c]][nodes[r]])
        else:
            table[r].append(0.0000)
    print('still continue')
count = 0
for k in range(0, len(nodes)):
    for r in range(0, len(nodes)):
        for c in range(0, len(nodes)):
            if table[r][k]+table[c][k] > table[r][c] and k != c and k != r and r != c:
                table[r][c] = table[r][k] + table[c][k]
    count += 1
    print('still continue', count)
# result
weight = {}
for x in list(combinations(nodes, 2)):
    weight[x] = table[nodes.index(x[0])][nodes.index(x[1])]
    print('almost')
print(weight)


