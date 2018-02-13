from itertools import combinations

print((0.000000000+float(6/9)) > (0.0000000000+float(5/9)))

with open("/Users/FPTShop/Desktop/centrality", "r") as myfile:
    lines = myfile.readlines()
    data = []
    for x in lines:
        data.append(x[:-1].split('\t'))
    graph = {}
    # what is centrality?
    # go through all key in graph[node]: check if keys are connect, count++
    # make another graph of node and it centrality
    for x in data:
        if x[0] not in graph:
            graph[x[0]] = []
        graph[x[0]] = graph[x[0]] + [i[0] for i in data if i[1] == x[1] and i[0] != x[0]]
        print('running..')
    m = 0.000000000000000000
    central = []
    for x in graph:
        graph[x] = list(set(graph[x]))
        print(graph[x])
        comb = list(combinations(graph[x], 2))
        count = 0
        for c in comb:
            if c[1] in graph[c[0]]:
                count += 1
        if float(2*count/(len(graph[x])*(len(graph[x])-1))) > m:
            central = [x]
            m = float(2*count/(len(graph[x])*(len(graph[x])-1)))
    print(central,m)