# Algorithm to find shortest distance from all nodes to all other node
# in running time of O(n^2)
# Using Dynamic Programming

import math
def create_labels(binarytreeG, root):
    labels = {root: {}}
    bfs = [[root, None]]
    marked = {}
    while len(bfs) != 0:
        current = bfs[0][0]
        p = bfs[0][1]
        del bfs[0]
        marked[current] = p
        for neigh in binarytreeG[current]:
            if neigh not in labels:
                labels[neigh] = {}
            if neigh in marked:
                labels[current][neigh] = binarytreeG[current][neigh]
                for parent in labels[neigh]:
                    if parent != current:
                        if parent in marked and marked[current] != marked[parent]:
                            labels[current][parent] = labels[neigh][parent] + labels[current][neigh]
            else:
                labels[current][neigh] = binarytreeG[current][neigh]
                bfs.append([neigh, current])
    return labels

#######
# Testing
#

def get_distances(G, labels):
    # labels = {a:{b: distance from a to b,
    #              c: distance from a to c}}
    # create a mapping of all distances for
    # all nodes
    distances = {}
    for start in G:
        # get all the labels for my starting node
        label_node = labels[start]
        s_distances = {}
        for destination in G:
            shortest = float('inf')
            # get all the labels for the destination node
            label_dest = labels[destination]
            # and then merge them together, saving the
            # shortest distance
            for intermediate_node, dist in label_node.items():
                # see if intermediate_node is our destination
                # if it is we can stop - we know that is
                # the shortest path
                if intermediate_node == destination:
                    shortest = dist
                    break
                other_dist = label_dest.get(intermediate_node)
                if other_dist is None:
                    continue
                if other_dist + dist < shortest:
                    shortest = other_dist + dist
            s_distances[destination] = shortest
        distances[start] = s_distances
    return distances

def make_link(G, node1, node2, weight=1):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = weight
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = weight
    return G

def test():
    edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7),
             (4, 8), (4, 9), (5, 10), (5, 11), (6, 12), (6, 13)]
    tree = {}
    for n1, n2 in edges:
        make_link(tree, n1, n2)
    labels = create_labels(tree, 1)
    print(labels)
    distances = get_distances(tree, labels)
    assert distances[1][2] == 1
    assert distances[1][4] == 2

test()
