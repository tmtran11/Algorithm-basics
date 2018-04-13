# Algorithm to make heap function for updating sorted sequences in O(log(n))

def parent(i):
    return (i-1)//2

def left_child(i):
    return 2*i+1


def right_child(i):
    return 2*i+2


def is_leaf(l, i):
    return (left_child(i) >= len(l)) and (right_child(i) >= len(l))


def one_child(l, i):
    return (left_child(i) < len(l)) and (right_child(i) >= len(l))


def up_heapify(i, l, order): #complicated shit. oh, you are so dumb.
    if parent(i) < 0:
        return
    if l[parent(i)][1] > l[i][1]:
        order[l[i][0]], order[l[parent(i)][0]] = order[l[parent(i)][0]], order[l[i][0]]
        l[i], l[parent(i)] = l[parent(i)], l[i]
    return up_heapify(parent(i), l, order)


def down_heapify(i, l, order):
    if is_leaf(l, i):
        return
    if one_child(l, i):
        comp = [left_child(i), l[left_child(i)][1]]
    else:
        if l[left_child(i)] < l[right_child(i)]:
            comp = [left_child(i), l[left_child(i)][1]]
        else:
            comp = [right_child(i), l[right_child(i)][1]]
    if l[i][1] > comp[1]:
        order[l[i][0]], order[l[comp[0]][0]] = order[l[comp[0]][0]], order[l[i][0]]
        l[i], l[comp[0]] = l[comp[0]], l[i]
    return down_heapify(comp[0], l, order)


def dijkstra(G, v):
    dist_so_far = [[v, 0]]
    final_dist = {}
    order = {}
    order[v] = 0
    while len(final_dist) < len(G):
        w = dist_so_far[0]
        order[dist_so_far[-1][0]] = 0
        dist_so_far = [dist_so_far[-1]]+dist_so_far[1:-1]
        down_heapify(0, dist_so_far, order)
        final_dist[w[0]] = w[1]
        for x in G[w[0]]:
            if x not in final_dist:
                if x not in order:
                    dist_so_far.append([x, final_dist[w[0]] + G[w[0]][x]])
                    order[x] = len(dist_so_far)-1
                    up_heapify(len(dist_so_far)-1, dist_so_far, order)
                elif final_dist[w[0]] + G[w[0]][x] < dist_so_far[order[x]][1]: 
                    dist_so_far[order[x]] = [x, final_dist[w[0]] + G[w[0]][x]]
                    up_heapify(order[x], dist_so_far, order)
    return final_dist


############
#
# Test

def make_link(G, node1, node2, w):
    if node1 not in G:
        G[node1] = {}
    if node2 not in G[node1]:
        (G[node1])[node2] = 0
    (G[node1])[node2] += w
    if node2 not in G:
        G[node2] = {}
    if node1 not in G[node2]:
        (G[node2])[node1] = 0
    (G[node2])[node1] += w
    return G


def test():
    # shortcuts
    (a, b, c, d, e, f, g) = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
    triples = ((a, c, 3), (c, b, 10), (a, b, 15), (d, b, 9), (a, d, 4), (d, f, 7), (d, e, 3),
               (e, g, 1), (e, f, 5), (f, g, 2), (b, f, 1))
    G = {}
    for (i, j, k) in triples:
        make_link(G, i, j, k)

    dist = dijkstra(G, a)
    assert dist[g] == 8  # (a -> d -> e -> g)
    assert dist[b] == 11  # (a -> d -> e -> g -> f -> b)

