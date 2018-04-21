"""
An instance of the N-puzzle game consists of a board holding N = m^2 − 1 (m = 3, 4, 5, ...) distinct movable tiles, plus an empty space. 
The tiles are numbers from the set {1, …, m^2 − 1}. For any such board, the empty space may be legally swapped with any tile horizontally or vertically adjacent to it. 
In this assignment, we will represent the blank space with the number 0 and focus on the m = 3 case (8-puzzle).
"""

"""
breath-first-search implement linkedList to remove_head at O(1) time
This is a merge data structure, as each node is connected in a single-chained LinkedList,
while many node share same parent, which create a tree straucture
Do not store sequence of move from start to one node,instead use def trace() to find solution.
"""

import copy
import time

class Node:
  def __init__(self,board, nodeP, index):
    self.next = None
    self.parent = nodeP
    self.index = index
    self.board = board.copy()

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    
  def remove_head(self):
    if self.head == None:
      return None
    node = copy.copy(self.head)
    if self.tail == None:
      self.head = self.tail
      self.tail = None
    else:
      self.head = self.head.next
    return node
    
  def add(self, node):
    if self.head == None:
      self.head = node
      return
    if self.tail == None:
      self.tail = node
      return
    self.tail.next = node
    self.tail = node

def trace(node):
  d = {-3:"Up",3:"Down",-1:"Left",1:"Right"}
  path_to_goal = []
  cost_of_path = 0
  while node.parent!=None:
    path_to_goal.append(d[node.index-node.parent.index])
    cost_of_path += 1
    node = node.parent
  return path_to_goal[::-1], cost_of_path
  
def swap(b, index1, index2):
  board = b.copy()
  board[index1], board[index2] = board[index2], board[index1]
  return board

def printf(board):
  print(str(board[0])+" "+str(board[1])+" "+str(board[2])+'\n')
  print(str(board[3])+" "+str(board[4])+" "+str(board[5])+'\n')
  print(str(board[6])+" "+str(board[7])+" "+str(board[8])+'\n')
  print('\n')

def bfs(board):
  path_to_goal = []
  cost_of_path = 0
  nodes_expanded = 0
  search_depth = 0
  max_search_depth = 0
  start_time = time.time()
  max_search_depth = 0
  
  result = None
  
  queue = LinkedList()
  index = board.index(0)
  node = Node(board.copy(),None,index)
  queue.add(node)
  depth1 = 1
  depth2 = 0
  max_search_depth = 0
  
  while 1:
    node = queue.remove_head()
    index = node.index
    if(node.parent==None):
      indexP = -1
    else:
      indexP = node.parent.index
    board = node.board
    #printf(board)
  
    if(index-3>0 and index-3!=indexP):
      b = swap(board,index,index-3)
      if(b==[0,1,2,3,4,5,6,7,8]):
        result = Node(b,index,index-3)
        break;
      queue.add(Node(b,node,index-3))
      nodes_expanded+=1
      depth2 += 1
      
    if(index+3<9 and index+3!=indexP):
      b = swap(board,index,index+3)
      if(b==[0,1,2,3,4,5,6,7,8]):
        result = Node(b,node,index+3)
        break;
      queue.add(Node(b,node,index+3))
      nodes_expanded+=1
      depth2 += 1
      
    if((index-1)//3==index//3 and index-1!=indexP):
      b = swap(board,index,index-1)
      if(b==[0,1,2,3,4,5,6,7,8]):
        result = Node(b,node,index-1)
        break;
      queue.add(Node(b,node,index-1))
      nodes_expanded+=1
      depth2 += 1
      
    if((index+1)//3==index//3 and index+1!=indexP):
      b = swap(board,index,index+1)
      if(b==[0,1,2,3,4,5,6,7,8]):
        result = Node(b,node,index+1)
        break;
      queue.add(Node(b,node,index+1))
      nodes_expanded+=1
      depth2 += 1
    
    depth1 -= 1
    if depth1 == 0:
      max_search_depth += 1
      depth1 = depth2
      depth2 = 0
  
  path_to_goal,cost_of_path = trace(result)
  search_depth = cost_of_path
  
  print("path_to_goal: ",path_to_goal)
  print("cost_of_path: ",cost_of_path)
  print("nodes_expanded: ",nodes_expanded)
  print("search_depth: ", search_depth)
  print("max_search_depth: ", max_search_depth)
  print("running_time: ",time.time()-start_time)
  
test = [6,1,8,4,0,2,7,3,5]
bfs(test)
