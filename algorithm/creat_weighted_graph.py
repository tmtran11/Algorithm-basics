def create_weighted_graph(bipartiteG, characters):
    graph = {}
    for x in characters:
        if x not in graph:
            graph[x] = {}
        for y in bipartiteG[x]:
            for z in bipartiteG[y]:
                if z!=x and z in characters:
                    if z not in graph[x]: graph[x][z]=0
                    graph[x][z] = graph[x][z]+bipartiteG[y][z]
    for x in characters:
        for y in graph[x]:
            graph[x][y] = float(graph[x][y])/float(len(bipartiteG)-len(characters))
    return graph

######
#
# Test

def test():
    bipartiteG = {'charA':{'comicB':1, 'comicC':1},
                  'charB':{'comicB':1, 'comicD':1},
                  'charC':{'comicD':1},
                  'comicB':{'charA':1, 'charB':1},
                  'comicC':{'charA':1},
                  'comicD': {'charC':1, 'charB':1}}
    G = create_weighted_graph(bipartiteG, ['charA', 'charB', 'charC'])
    # three comics contain charA or charB
    # charA and charB are together in one of them
    assert G['charA']['charB'] == 1.0 / 3
    assert G['charA'].get('charA') == None
    assert G['charA'].get('charC') == None

test()
