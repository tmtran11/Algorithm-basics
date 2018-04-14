# Provide two txt file of film and its relative budget and actors and their film
# Return a graph with weight of each actor to other
# with the weight calculated by the highest possible sum of the money make by the films that connect them.
# running time O(n^3)
# Using Dynamic Programming

import codecs
from itertools import combinations

def merge(g1, g2):
    return {u: max(i for i in (g1.get(u), g2.get(u)) if i) for u in g1.keys() | g2} 


film = codecs.open("/film", "r", encoding='utf-8')
lines = film.readlines()
f = {}  
# key:(film, actor), value:its money
# raw processing of the txt files
for x in lines:
    t = x[:-1].split('\t')
    f[(t[0], t[1])] = float(t[2])
actor = codecs.open("/actors", "r", encoding='utf-8')
lines = actor.readlines()

a = {}  
# key:actor value:all films that participates
for x in lines:
    t = x[:-1].split('\t')
    if t[0] not in a:
        a[t[0]] = []
    a[t[0]].append((t[1], t[2])) 
    if (t[1], t[2]) not in r:
        r[(t[1], t[2])] = {}
    r[(t[1], t[2])].update({t[0]: f[(t[1], t[2])]})  


# key:actor, value:all actor that they are connected to, map to the money value of the movie
g = {}
for this in a:
    g[this] = {}
    for film in a[this]:
        g[this] = merge(g[this], r[film])


nodes = list(a.keys())
table = []
# Using dynamic programming, with maximizing path's weight as the objective
# Initializa table, dimension of actors*actors, if actor and actor is not directly connected then let table[a1][a2]=0
for r in range(0, len(nodes)):
    table.append([])
    for c in range(0, len(nodes)):
        if nodes[r] in g[nodes[c]]:
            table[r].append(g[nodes[c]][nodes[r]])
        else:
            table[r].append(0.0000)

# Dynamics programming
count = 0
for k in range(0, len(nodes)):
    for r in range(0, len(nodes)):
        for c in range(0, len(nodes)):
            if table[r][k]+table[c][k] > table[r][c] and k != c and k != r and r != c:
                table[r][c] = table[r][k] + table[c][k]
                
weight = {}
for x in list(combinations(nodes, 2)):
    weight[x] = table[nodes.index(x[0])][nodes.index(x[1])]
# return the dictionary of pair of actor with the

