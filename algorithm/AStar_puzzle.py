import copy
import time

# implement a speacial linked list to store O(n^n) space into O(n^2)
class LinkedList():
  def __init__(self,index=0):
    self.index = index
    self.n = [None]*9
    if index+1==9:
      self.link = None
    else:
      self.link = LinkedList(index+1)
      
  def find(self,seq):
    if self.n[seq[0]]==None:
      return False
    if self.link==None:
      return True
    return self.link.find(seq[1:])
    
  def add(self,seq):
    self.n[seq[0]] = 0
    if self.link==None:
      return
    self.link.add(seq[1:])

# Node store all necessary infomation
class Node:
  def __init__(self,index,d,board,parent,depth):
    self.index = index
    self.distance = d
    self.board = board.copy()
    self.parent = parent
    self.depth = depth

# Using heap algorithm to lower down search for minimal node from O(n) to O(log n)
class heap():
  def __init__(self):
    self.h = []
    
  def leftChild(self,index):
    return index*2+1
  def rightChild(self,index):
    return index*2+2
    
  def hasLeftChild(self,index):
    return self.leftChild(index)<len(self.h) and self.leftChild(index)>-1
  def hasRightChild(self,index):
    return self.rightChild(index)<len(self.h) and self.rightChild(index)>-1
    
  def isLeaf(self,index):
    return not self.hasRightChild(index) and not self.hasLeftChild(index)
  def parent(self,index):
    return (index-1)//2
    
  def remove_head(self):
    head = copy.copy(self.h[0])
    self.h[0] = self.h[-1]
    self.h = self.h[:-1]
    self.down_heapify(0)
    return head
    
  def down_heapify(self,index):
    if self.isLeaf(index):
      return
    if self.hasLeftChild(index) and self.h[self.leftChild(index)].distance<self.h[index].distance:
      if (self.hasRightChild(index) and self.h[self.leftChild(index)].distance<self.h[self.rightChild(index)].distance) or not self.hasRightChild(index):
          self.h[index], self.h[self.leftChild(index)] = self.h[self.leftChild(index)], self.h[index]
          self.down_heapify(self.leftChild(index))
    if self.hasRightChild(index) and self.h[self.rightChild(index)].distance<self.h[index].distance:
      if (self.hasLeftChild(index) and self.h[self.rightChild(index)].distance<self.h[self.leftChild(index)].distance) or not self.hasLeftChild(index):
        self.h[index], self.h[self.rightChild(index)] = self.h[self.rightChild(index)], self.h[index]
        self.down_heapify(self.rightChild(index))
    return
  
  def add(self,node):
    self.h.append(node)
    self.up_heapify(len(self.h)-1)
    # print([x.distance for x in self.h])
    
  def up_heapify(self,index):
    if index==0:
      return
    if self.h[index].distance<self.h[self.parent(index)].distance:
      self.h[index], self.h[self.parent(index)] = self.h[self.parent(index)], self.h[index]
      self.up_heapify(self.parent(index))
    return

# find all distance in board
# is initialize once
def distance(board):
  d = 0
  for n,x in enumerate(board):
    diff = abs(x-n)
    if x//3==n//3:
      d += diff
    else:
      d += diff//3 + abs(diff//3*3-diff)
  return d

# find distance in new position
def dist(x,n):
  d = 0
  diff = abs(x-n)
  if x//3==n//3:
    d += diff
  else:
    d += diff//3 + abs(diff//3*3-diff)
  return d

# change in overall distance
# Manhattan heuristic
def delta_d(board, a, b):
  return dist(board[b],a)-dist(board[b],b)
  
# test heap structure
def test_heap():
  h = heap()
  h.add(Node(0,10,[],None,1))
  h.add(Node(0,12,[],None,1))
  h.add(Node(0,1,[],None,1))
  h.add(Node(0,9,[],None,1))
  h.add(Node(0,0,[],None,1))
  print(h.remove_head().distance)
  print(h.remove_head().distance)
  print(h.remove_head().distance)
  print(h.remove_head().distance)

  
# trace back through a chain of linked node
def trace(node):
  d = {-3:"Up",3:"Down",-1:"Left",1:"Right"}
  path_to_goal = []
  cost_of_path = 0
  while node.parent!=None:
    path_to_goal.append(d[node.index-node.parent.index])
    cost_of_path += 1
    node = node.parent
  return path_to_goal[::-1], cost_of_path
  
# print board for testing
def printf(board):
  print(str(board[0])+" "+str(board[1])+" "+str(board[2])+'\n')
  print(str(board[3])+" "+str(board[4])+" "+str(board[5])+'\n')
  print(str(board[6])+" "+str(board[7])+" "+str(board[8])+'\n')

# A-star algorithm
def ast(board):
  start_time = time.time()
  
  # A specilized linked list store visited state, seaching time O(1)
  searched = LinkedList()
  # A frontier with O(log(n)) search pace
  frontier = heap()
  # initilize distance of all node to its expected positions
  d = distance(board)
  # first node, which represents all stat of the initial state
  node = Node(board.index(0),d,board,None,1)
  
  searched.add(board)
  frontier.add(node)
  result = None
  
  nodes_expanded = 1
  max_search_depth = 1
  while 1:
    node = frontier.remove_head()
    index = node.index
    board = node.board.copy()
    depth = node.depth
    d = node.distance
    
    if(node.parent!=None):
      indexP = node.parent.index
    else:
      indexP=-1
    prev_board = board.copy()
    
    if index-3>0 and not index-3==indexP:
      td = d+delta_d(board,index,index-3)
      board[index],board[index-3] = board[index-3],board[index]
      if not searched.find(board):
        if board==[0,1,2,3,4,5,6,7,8]:
          result = Node(index-3,td,board,node,depth+1)
          break
        searched.add(board)
        frontier.add(Node(index-3,td,board,node,depth+1))
        nodes_expanded+=1
      board = prev_board.copy()
      
    if index+3<9 and not index+3==indexP:
      td = d+delta_d(board,index,index+3)
      board[index],board[index+3] = board[index+3],board[index]
      if not searched.find(board):
        if board==[0,1,2,3,4,5,6,7,8]:
          result = Node(index+3,td,board,node,depth+1)
          break
        searched.add(board)
        frontier.add(Node(index+3,td,board,node,depth+1))
        nodes_expanded+=1
      board = prev_board.copy()
      
    if index//3==(index-1)//3 and not index-1==indexP:
      td = d+delta_d(board, index, index-1)
      board[index],board[index-1] = board[index-1],board[index]
      if not searched.find(board):
        if board==[0,1,2,3,4,5,6,7,8]:
          result = Node(index-1,td,board,node,depth+1)
          break
        searched.add(board)
        frontier.add(Node(index-1,td,board,node,depth+1))
        nodes_expanded+=1
      board = prev_board.copy()
      
    if index//3==(index+1)//3 and not index+1==indexP:
      td = d+delta_d(board, index, index+1)
      board[index],board[index+1] = board[index+1],board[index]
      if not searched.find(board):
        if board==[0,1,2,3,4,5,6,7,8]:
          result = Node(index+1,td,board,node,depth+1)
          break
        searched.add(board)
        frontier.add(Node(index+1,td,board,node,depth+1))
        nodes_expanded+=1
      board = prev_board.copy()
      
    if depth+1>max_search_depth:
      max_search_depth = depth+1
  
  if depth+1>max_search_depth:
      max_search_depth = depth+1
  path_to_goal,cost_of_path = trace(result)
  search_depth = result.depth
  
  print("path_to_goal: ",path_to_goal)
  print("cost_of_path: ",cost_of_path)
  print("nodes_expanded: ",nodes_expanded)
  print("search_depth: ", search_depth)
  print("max_search_depth: ", max_search_depth)
  print("running_time: ",time.time()-start_time)

test = [1,4,2,3,5,8,6,7,0]
ast(test)1
