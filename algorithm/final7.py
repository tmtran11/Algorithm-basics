from operator import itemgetter


def maximize_probability_of_favor(G, v1, v2):
    # if dense, use heap
    # if not dense, use list
    final_prob = dijkstra_heap(G, v1)
    path = final_prob[v2][1]+[v2]
    prob = final_prob[v2][0]
    print(path, prob)
    return path, prob


#
# version of dijkstra implemented using a heap
#
# returns a dictionary mapping a node to the distance
# to that node and the parent
#
# Do not modify this code
#
def dijkstra_heap(G, a):
    # Distance to the input node is zero, and it has
    # no parent
    first_entry = (1.000, a, [])
    heap = [first_entry]
    # location keeps track of items in the heap
    # so that we can update their value later
    location = {first_entry: 0}
    dist_so_far = {a: first_entry}
    final_dist = {}
    while len(dist_so_far) > 0:
        dist, node, path = heappopmin(heap, location)
        # lock it down!
        final_dist[node] = (dist, path)
        del dist_so_far[node]
        for x in G[node]:
            if x in final_dist:
                continue
            new_dist = G[node][x] * final_dist[node][0]
            new_path = final_dist[node][1] + [x]
            new_entry = (new_dist, x, new_path)
            if x not in dist_so_far:
                # add to the heap
                insert_heap(heap, new_entry, location)
                dist_so_far[x] = new_entry
            elif new_entry > dist_so_far[x]:
                # update heap
                decrease_val(heap, location, dist_so_far[x], new_entry)
                dist_so_far[x] = new_entry
    return final_dist
    # return (distance from a, path)


#
# version of dijkstra implemented using a list
#
# returns a dictionary mapping a node to the distance
# to that node and the parent
#
# Do not modify this code
#
def dijkstra_list(G, a):
    dist_so_far = {a: (1.000, [])}  # keep track of the parent node
    final_dist = {}
    while len(final_dist) < len(G):
        node, entry = min(dist_so_far.items(), key=itemgetter(1))
        # lock it down!
        final_dist[node] = entry
        del dist_so_far[node]
        for x in G[node]:
            if x in final_dist:
                continue
            new_dist = G[node][x] * final_dist[node][0]
            new_entry = (new_dist, entry[1]+[node])
            if x not in dist_so_far:
                dist_so_far[x] = new_entry
            elif new_entry > dist_so_far[x]:
                dist_so_far[x] = new_entry
    return final_dist
    # return (distance from a, its parent)


##########
#
# Test

def test():
    G = {'a': {'b': .9, 'e': .5},
         'b': {'c': .9},
         'c': {'d': .01},
         'd': {},
         'e': {'f': .5},
         'f': {'d': .5}}
    path, prob = maximize_probability_of_favor(G, 'a', 'd')
    assert path == ['a', 'e', 'f', 'd']
    assert abs(prob - .5 * .5 * .5) < 0.001
test()

def left(i): return i*2+1
def right(i): return i*2+2
def parent(i): return (i-1)/2
def root(i): return i==0
def leaf(L, i): return right(i) >= len(L) and left(i) >= len(L)
def one_child(L, i): return right(i) == len(L)
def val_(pair): return pair[0]

def swap(heap, old, new, location):
    location[heap[old]] = new
    location[heap[new]] = old
    (heap[old], heap[new]) = (heap[new], heap[old])

# Call this routine if the heap rooted at i satisfies the heap property
# *except* perhaps i to its children immediate children
#
#
# location is a dictionary mapping an object to its location
# in the heap
def down_heapify(heap, i, location):
    # If i is a leaf, heap property holds
    while True:
        l = left(i)
        r = right(i)

        # see if we don't have any children
        if l >= len(heap):
            break

        v = heap[i][0]
        lv = heap[l][0]

        # If i has one child...
        if r == len(heap):
            # check heap property
            if v > lv:
                # If it fails, swap, fixing i and its child (a leaf)
                swap(heap, i, l, location)
            break

        rv = heap[r][0]
        # If i has two children...
        # check heap property
        if min(lv, rv) >= v:
            break
        # If it fails, see which child is the smaller
        # and swap i's value into that child
        # Afterwards, recurse into that child, which might violate
        if lv < rv:
            # Swap into left child
            swap(heap, i, l, location)
            i = l
        else:
            # swap into right child
            swap(heap, i, r, location)
            i = r

# Call this routine if whole heap satisfies the heap property
# *except* perhaps i to its parent
def up_heapify(heap, i, location):
    # If i is root, all is well
    while i > 0:
        # check heap property
        p = (i - 1) / 2
        if heap[i][0] < heap[p][0]:
            swap(heap, i, p, location)
            i = p
        else:
            break

# put a pair in the heap
def insert_heap(heap, v, location):
    heap.append(v)
    location[v] = len(heap) - 1
    up_heapify(heap, len(heap) - 1, location)

# build_heap
def build_heap(heap):
    location = dict([(n, i) for i, n in enumerate(heap)])
    for i in range(len(heap)-1, -1, -1):
        down_heapify(heap, i, location)
    return location

# remove min
def heappopmin(heap, location):
    # small = heap[0]
    val = heap[0]
    new_top = heap.pop()
    del location[val]
    if len(heap) == 0:
        return val
    location[new_top] = 0
    heap[0] = new_top
    down_heapify(heap, 0, location)
    return val

def decrease_val(heap, location, old_val, new_val):
    i = location[old_val]
    heap[i] = new_val
    # is this the best way?
    del location[old_val]
    location[new_val] = i
    up_heapify(heap, i, location)