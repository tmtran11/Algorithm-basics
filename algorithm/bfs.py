# algorithm return highest possible score of any path
# return None if path not exist
# using bfs

def feel_the_love(G, i, j):
    bfs = [i]
    marked = [i]
    path = {i: [i]}
    m = 0
    edge = []
    while len(bfs)!= 0:
        current = bfs[0]
        del bfs[0]
        for neigh in G[current]:
            if G[current][neigh] > m:
                m = G[current][neigh]
                edge = [current, neigh]
            if neigh not in marked:
                path[neigh] = path[current]+[neigh]
                bfs.append(neigh)
                marked.append(neigh)
    if j not in path: return None
    return path[edge[0]]+[edge[1]]+path[edge[1]][::-1][1:]+path[j][1:]


#########
#
# Test

def score_of_path(G, path):
    max_love = -float('inf')
    for n1, n2 in zip(path[:-1], path[1:]):
        love = G[n1][n2]
        if love > max_love:
            max_love = love
    return max_love


def test():
    G = {'a': {'c': 1},
         'b': {'c': 1},
         'c': {'a': 1, 'b': 1, 'e': 1, 'd': 1},
         'e': {'c': 1, 'd': 2},
         'd': {'e': 2, 'c': 1},
         'f': {}}
    path = feel_the_love(G, 'a', 'b')
    assert score_of_path(G, path) == 2

    path = feel_the_love(G, 'a', 'f')
    assert path == None

test()


