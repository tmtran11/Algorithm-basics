# Processing a txt file of data from Marvels. Each line include the character and one of the book in they appear in. Estimated 50000 line
# Using dynamic programming to find the most relevant character

with open("/Users/FPTShop/Desktop/weight", "r") as myfile:
    lines = myfile.readlines()
    data = []
    for x in lines:
        data.append(x[:-1].split('\t'))
    graph = {}
    for x in data:
        if x[0] not in graph:
            graph[x[0]] = {}
        all = [i[0] for i in data if i[1] == x[1] and i[0] != x[0]]
        for i in all:
            if i not in graph[x[0]]:
                graph[x[0]][i] = 1
            else:
                graph[x[0]][i] += 1
    # graph with weight
    nodes = list(graph.keys())
    table = []
    # problem
    for r in range(0, len(nodes)):
        table.append([])
        for c in range(0, len(nodes)):
            if nodes[r] in graph[nodes[c]]:
                table[r].append([float(1.00000/float(graph[nodes[c]][nodes[r]])), 2])
            elif r == c:
                table[r].append([0.000, 1])
            else:
                table[r].append([1000000.00000, 2])
    for k in range(0, len(nodes)):
        for r in range(0, len(nodes)):
            for c in range(0, len(nodes)):
                if table[r][k][0]+table[c][k][0] < table[r][c][0]:
                    table[r][c][0] = table[r][k][0] + table[c][k][0]
                    table[r][c][1] = table[r][k][1] + table[c][k][1] - 1

    s = 0
    for r in range(0, len(nodes)):
        for c in range(0, len(nodes)):
            s += table[r][c][1]
    print((s-len(table[0]))/2)
