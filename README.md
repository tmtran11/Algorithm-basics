# Algorthms for data-mining using graphs.
# Self-study
# Under instruction of Michael Littman, https://classroom.udacity.com/courses/cs215
"""
Using estimated 50000 lines worth of data from Marvel, constructed high-density graphs and use different searching algorithm to to explore special characteristics of this databases.

*Explore centrality:
https://github.com/tmtran11/Graph_algorithms/blob/master/algorithm/centrality.py
- Centrality of vertex v is defined in this algorithm as the ratio of pairs of v’s adjacent vertices that is directly connect to each other over all possible pair
- Central vertex is vertex with highest ratio.
- Formula: 2*(count of pair of adjacent vertices that is directly connected)/(number of v’s adjacent vertices*(number of v’s adjacent vertices-1))

*Find shortest path from one vertex(v) to all the other:
https://github.com/tmtran11/Graph_algorithms/blob/master/algorithm/dp_shortest_path_all.py
- Initialize a graph whose purpose is to store the temporary shortest distance from v to others
- Build heap structure for this graph. Using up and down heapify to keep the graph sorted in log(n) time
- Using Dijkstra algorithm to find shortest path. Dijkstra is the combination between heapifying and dynamic programming.
- Search start from v
- For each search, find the vertex which currently has the shortest distance to v and finalize its shortest distance to s. The search is in O(1), because the heap is constantly sorted in O(log(n)) everytime a value is remove or add.
- From that vertex, find it neighbor whose the possible shortest path to v is update by dynamic programming in next searches

*Find bridge edges
https://github.com/tmtran11/Graph_algorithms/blob/master/algorithm/bridge_edge.py
- Create a rooted spanning tree, with green edges for tree’s edges and red edge for other edge in the graph that’s not suitable for the tree structure.
- Compute post order, consider only the green edges.
- Find lowest and highest post order of each vertex, can include one adjacency vertex of red edge.
- Compute number of decensant, only consider the green edges
- An edge is a bridge edge if: *An edge is a green edge: because if that edge is a red edge, there is a green edge elsewhere that remain the connectivity of the graph
- The post order of the vertex on that edge must be bigger or equals than the highest post order on that edge, to ensure that there is no other edge connect it with the parental vertices
- The lowest post order of the vertex must be bigger than the number of descendant minus the post order of that vertex to make sure that there is no other edge connect the descendents vertices

"""

