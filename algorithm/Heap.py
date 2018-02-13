#
# write up_heapify, an algorithm that checks if
# node i and its parent satisfy the heap
# property, swapping and recursing if they don't
#
# L should be a heap when up_heapify is done


def up_heapify(l, i):
    if parent(i)<0:
        return
    if left_child(parent(i)) < len(l) and l[parent(i)] > l[left_child(parent(i))]:
        l[parent(i)], l[left_child(parent(i))] = l[left_child(parent(i))], l[parent(i)]
    if right_child(parent(i)) < len(l) and l[parent(i)] > l[right_child(parent(i))]:
        l[parent(i)], l[right_child(parent(i))] = l[right_child(parent(i))], l[parent(i)]
    return up_heapify(l, parent(i))


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


def test():
    L = [2, 4, 3, 5, 9, 7, 7]
    L.append(1)
    up_heapify(L, 7)
    print(L)
    assert 1 == L[0]
    assert 2 == L[1]

test()