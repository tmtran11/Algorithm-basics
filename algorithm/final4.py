def process_graph(G):
    #bfs for every node
    for node in G:
        marked = []
        bfs = [node]
        while len(bfs)!=0:
            current = bfs[0]
            marked.append(current)
            del bfs[0]
            for neigh in current:
                if neigh not in marked:
                    bfs.append(neigh)
                    G[node][neigh] = G[node][current]+1

#
# When being graded, `is_connected` will be called
# many times so this routine needs to be quick
#
def is_connected(G, i, j):
    return j in G[i]

#######
# Testing
#
def test():
    G = {'a':{'b':1},
         'b':{'a':1},
         'c':{'d':1},
         'd':{'c':1},
         'e':{}}
    process_graph(G)
    assert is_connected(G, 'a', 'b') == True
    assert is_connected(G, 'a', 'c') == False

    G = {'a':{'b':1, 'c':1},
         'b':{'a':1},
         'c':{'d':1, 'a':1},
         'd':{'c':1},
         'e':{}}
    process_graph(G)
    assert is_connected(G, 'a', 'b') == True
    assert is_connected(G, 'a', 'c') == True
    assert is_connected(G, 'a', 'e') == False

test()