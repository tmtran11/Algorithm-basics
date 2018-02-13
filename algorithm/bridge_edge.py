# Bridge Edges v4
#
# Find the bridge edges in a graph given the
# algorithm in lecture.
# Complete the intermediate steps
#  - create_rooted_spanning_tree
#  - post_order
#  - number_of_descendants
#  - lowest_post_order
#  - highest_post_order
#
# And then combine them together in
# `bridge_edges`

import itertools
import collections


def make_link(g, node1, node2, r_or_g):
    if node1 not in g:
        g[node1] = {}
    (g[node1])[node2] = r_or_g
    if node2 not in g:
        g[node2] = {}
    (g[node2])[node1] = r_or_g
    return g


def create_rooted_spanning_tree(g, root):
    s = {}
    s[root] = {}
    open_list = [root]
    while len(open_list) > 0:
        current = open_list[0]
        del open_list[0]
        for x in g[current]:
            if x not in s:
                make_link(s, x, current, 'green')
                open_list.append(x)
            else:
                if current not in s[x]:
                    make_link(s, x, current, 'red')
    return s


def find_all_children(s, parent, current):
    green, red = [], []
    for child in s[current]:
        if child != parent:
            if s[current][child] == 'green':
                green.append(child)
            else:
                red.append(child)
    return green, red


def test_create_rooted_spanning_tree():
    g = {'a': {'c': 1, 'b': 1},
         'b': {'a': 1, 'd': 1},
         'c': {'a': 1, 'd': 1},
         'd': {'c': 1, 'b': 1, 'e': 1},
         'e': {'d': 1, 'g': 1, 'f': 1},
         'f': {'e': 1, 'g': 1},
         'g': {'e': 1, 'f': 1}
         }
    s = create_rooted_spanning_tree(g, "a")
    assert s == {'a': {'c': 'green', 'b': 'green'},
                 'b': {'a': 'green', 'd': 'red'},
                 'c': {'a': 'green', 'd': 'green'},
                 'd': {'c': 'green', 'b': 'red', 'e': 'green'},
                 'e': {'d': 'green', 'g': 'green', 'f': 'green'},
                 'f': {'e': 'green', 'g': 'red'},
                 'g': {'e': 'green', 'f': 'red'}
                 }
# test_create_rooted_spanning_tree()
###########


def post_order(s, root):
    p_order = dict((key, 0) for key in s)
    next_post_order(s, None, root, 1, p_order)
    return p_order


def next_post_order(s, parent, current, po, p_order):
    children, red = find_all_children(s, parent, current)
    for child in children[::-1]:
        po = next_post_order(s, current, child, po, p_order)
    p_order[current] = po
    return po+1


# This is just one possible solution
# There are other ways to create a
# spanning tree, and the grader will
# accept any valid result.
# feel free to edit the test to
# match the solution your program produces
# the test was right, check order
def test_post_order():
    s = { 'a': {'c': 'green', 'b': 'green'},
          'b': {'a': 'green', 'd': 'red'},
          'c': {'a': 'green', 'd': 'green'},
          'd': {'c': 'green', 'b': 'red', 'e': 'green'},
          'e': {'d': 'green', 'g': 'green', 'f': 'green'},
          'f': {'e': 'green', 'g': 'red'},
          'g': {'e': 'green', 'f': 'red'}
          }
    po = post_order(s, 'a')
    print(po)
    assert po == {'a': 7, 'b': 1, 'c': 6, 'd': 5, 'e': 4, 'f': 2, 'g': 3}

# test_post_order()
##############


def number_of_descendants(s, root):
    nd = {}
    number_of_descendants_next(s, None, root, nd)
    return nd


def number_of_descendants_next(s, parent, current, nd):
    n = 1
    for child in s[current]:
        if child != parent and s[current][child] == 'green':
            n += number_of_descendants_next(s, current, child, nd)
    nd[current] = n
    return n


def test_number_of_descendants():
    s = {'a': {'c': 'green', 'b': 'green'},
         'b': {'a': 'green', 'd': 'red'},
         'c': {'a': 'green', 'd': 'green'},
         'd': {'c': 'green', 'b': 'red', 'e': 'green'},
         'e': {'d': 'green', 'g': 'green', 'f': 'green'},
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'}
         }
    nd = number_of_descendants(s, 'a')
    assert nd == {'a': 7, 'b': 1, 'c': 5, 'd': 4, 'e': 3, 'f': 1, 'g': 1}


# test_number_of_descendants()

###############


def next_general_post_order(s, parent, current, po, comp, order):
    # return whatever, but have to change the general order {})
    green, red = find_all_children(s, parent, current)
    check = po[current]
    for child in green:
        val = next_general_post_order(s, current, child, po, comp, order)
        if comp(val, check):
            check = val
    for child in red:
        val = po[child]
        if comp(val, po[current]):
            check = val
    order[current] = check
    return order[current]


def general_post_order(s, root, po, comp):
    order = {}
    next_general_post_order(s, None, root, po, comp, order)
    return order


def lowest_post_order(s, root, po):
    lowest = general_post_order(s, root, po, lambda x, y: x < y) # how dis this thing work?
    return lowest


def test_lowest_post_order():
    s = {'a': {'c': 'green', 'b': 'green'},
         'b': {'a': 'green', 'd': 'red'},
         'c': {'a': 'green', 'd': 'green'},
         'd': {'c': 'green', 'b': 'red', 'e': 'green'},
         'e': {'d': 'green', 'g': 'green', 'f': 'green'},
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'}
         }
    po = post_order(s, 'a')
    l = lowest_post_order(s, 'a', po)
    assert l == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 2, 'f': 2, 'g': 2}

# test_lowest_post_order()
################


def highest_post_order(s, root, po):
    highest = general_post_order(s, root, po, lambda x, y: x > y)  # how dis this thing work?
    return highest


def test_highest_post_order():
    s = {'a': {'c': 'green', 'b': 'green'},
         'b': {'a': 'green', 'd': 'red'},
         'c': {'a': 'green', 'd': 'green'},
         'd': {'c': 'green', 'b': 'red', 'e': 'green'},
         'e': {'d': 'green', 'g': 'green', 'f': 'green'},
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'}
         }
    po = post_order(s, 'a')
    h = highest_post_order(s, 'a', po)
    assert h == {'a': 7, 'b': 5, 'c': 6, 'd': 5, 'e': 4, 'f': 3, 'g': 3}

# test_highest_post_order()
#################


def bridge_edges(g, root):
    s = create_rooted_spanning_tree(g, root)
    po = post_order(s, root)
    all = []
    b_edges = []
    for node in s:
        lowest = lowest_post_order(s, root, po)[node]
        highest = highest_post_order(s, root, po)[node]
        descendant = number_of_descendants(s, root)[node]
        print(node, po[node], descendant, lowest, highest)
        if highest <= po[node] and lowest > (po[node]-descendant):
            all.append(node)
    for x in all:
        if x != 'a':
            green, red = find_all_children(s, None, root)
            parent = [p for p in s[x] if p not in green and p not in red][0]
            b_edges.append((parent, x))
    print(b_edges)
    return b_edges


def test_bridge_edges():
    g = {'a': {'c': 1, 'b': 1},
         'b': {'a': 1, 'd': 1},
         'c': {'a': 1, 'd': 1},
         'd': {'c': 1, 'b': 1, 'e': 1},
         'e': {'d': 1, 'g': 1, 'f': 1},
         'f': {'e': 1, 'g': 1},
         'g': {'e': 1, 'f': 1}
         }
    bridges = bridge_edges(g, 'a')
    assert bridges == [('d', 'e')]

test_bridge_edges()
