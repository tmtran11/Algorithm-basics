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
        print('running..')
    print('out')
    m = 0
    m_weight = []
    for x in graph:
        for i in graph[x]:
            if graph[x][i] > m:
                m = graph[x][i]
                m_weight = [x, i]
    print(m_weight, m)
# create edge add in weight every time encounter one more?
# find the most weighted relationship