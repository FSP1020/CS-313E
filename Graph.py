#  File: Graph.py

#  Description: Given an input file, print the cities by depth first search,
#  breadth first frist, print after deleting an edge and then a vetex.

#  Date Created: 11/23/2020

#  Date Last Modified: 11/23/2020

import sys

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append (item)

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check the item on the top of the stack
  def peek (self):
    return self.stack[-1]

  # check if the stack if empty
  def is_empty (self):
    return (len (self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len (self.stack))


class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue is empty
  def is_empty (self):
    return (len (self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len (self.queue))


class Vertex (object):
  def __init__ (self, label):
    self.label = label
    self.visited = False

  # determine if a vertex was visited
  def was_visited (self):
    return self.visited

  # determine the label of the vertex
  def get_label (self):
    return self.label

  # string representation of the vertex
  def __str__ (self):
    return str (self.label)


class Edge (object):
  def __init__ (self, fromVertex, toVertex, weight = 1):
    self.u = fromVertex
    self.v = toVertex
    self.weight = weight

  # comparison operators
  def __lt__ (self, other):
    return self.weight < other.weight

  def __le__ (self, other):
    return self.weight <= other.weight

  def __gt__ (self, other):
    return self.weight > other.weight

  def __ge__ (self, other):
    return self.weight >= other.weight

  def __eq__ (self, other):
    return self.weight == other.weight

  def __ne__ (self, other):
    return self.weight != other.weight


class Graph (object):
  def __init__ (self):
    self.Vertices = []
    self.adjMat = []

  # check if a vertex is already in the graph
  def has_vertex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).get_label()):
        return True
    return False

  # given the label get the index of a vertex
  def get_index (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).get_label()):
        return i
    return -1

  # add a Vertex with a given label to the graph
  def add_vertex (self, label):
    if (self.has_vertex (label)):
      return

    # add vertex to the list of vertices
    self.Vertices.append (Vertex (label))

    # add a new column in the adjacency matrix
    nVert = len (self.Vertices)
    for i in range (nVert - 1):
      (self.adjMat[i]).append (0)

    # add a new row for the new vertex
    new_row = []
    for i in range (nVert):
      new_row.append (0)
    self.adjMat.append (new_row)

  # add weighted directed edge to graph
  def add_directed_edge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight

  # add weighted undirected edge to graph
  def add_undirected_edge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight

  # return an unvisited vertex adjacent to vertex v (index)
  def get_adj_unvisited_vertex (self, v):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
        return i
    return -1

  # do a depth first search in a graph
  def dfs (self, v):
    # create the Stack
    theStack = Stack ()

    # mark the vertex v as visited and push it on the Stack
    (self.Vertices[v]).visited = True
    print (self.Vertices[v])
    theStack.push (v)

    # visit all the other vertices according to depth
    while (not theStack.is_empty()):
      # get an adjacent unvisited vertex
      u = self.get_adj_unvisited_vertex (theStack.peek())
      if (u == -1):
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        print (self.Vertices[u])
        theStack.push (u)

    # the stack is empty, let us reset the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

  # do the breadth first search in a graph
  def bfs (self, v):
     # create the Queue
    theQueue = Queue ()

    # mark the vertex v as visited and enqueue
    (self.Vertices[v]).visited = True
    print (self.Vertices[v])
    theQueue.enqueue (v)

    while (not theQueue.is_empty()):
      v1 = theQueue.dequeue()
      # get an adjacent unvisited vertex
      v2 = self.get_adj_unvisited_vertex (v1)
      while (v2 != -1):
        (self.Vertices[v2]).visited = True
        print (self.Vertices[v2])
        theQueue.enqueue (v2)
        v2 = self.get_adj_unvisited_vertex (v1)

    # the queue is empty, let us reset the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

  # get edge weight between two vertices
  # return -1 if edge does not exist
  def get_edge_weight (self, fromVertexLabel, toVertexLabel):
    weight = self.adjMat[self.get_index(fromVertexLabel)]\
    [self.get_index(toVertexLabel)]
    if weight == 0:
        return -1
    else:
        return weight

  # get a list of immediate neighbors that you can go to from a vertex
  # return a list of indices or an empty list if there are none
  def get_neighbors (self, vertexLabel):
    neighbors = []
    v = self.get_index(vertexLabel)
    for i in range (len(self.Vertices)):
      if (self.adjMat[v][i] > 0):
        neighbors.append(self.Vertices[i])
    return neighbors

  # get a copy of the list of Vertex objects
  def get_vertices (self):
    copy = []
    for v in self.Vertices:
      copy.append(v)
    return copy

  # delete an edge from the adjacency matrix
  # delete a single edge if the graph is directed
  # delete two edges if the graph is undirected
  def delete_edge (self, fromVertexLabel, toVertexLabel):
    start = self.get_index(fromVertexLabel)
    finish = self.get_index(toVertexLabel)
    self.adjMat[start][finish] = 0
    self.adjMat[finish][start] = 0

  # delete a vertex from the vertex list and all edges from and
  # to it in the adjacency matrix
  def delete_vertex (self, vertexLabel):
    v = self.get_index(vertexLabel)
    nVert = len(self.Vertices)
    
    # Delete the column
    for i in range(nVert):
      for j in range(v, nVert - 1):
        self.adjMat[i][j] = self.adjMat[i][j+1]
      self.adjMat[i].pop()
    
    # Delete the row
    self.adjMat.pop(v)
    
    for vertex in self.Vertices:
      if vertex.label == vertexLabel:
        self.Vertices.remove(vertex)


def main():
  # create the Graph object
  cities = Graph()

  # read the number of vertices
  line = sys.stdin.readline()
  line = line.strip()
  num_vertices = int (line)

  # read the vertices to the list of Vertices
  for i in range (num_vertices):
    line = sys.stdin.readline()
    city = line.strip()
    #print (city)
    cities.add_vertex (city)

  # read the number of edges
  line = sys.stdin.readline()
  line = line.strip()
  num_edges = int (line)
  #print (num_edges)

  # read each edge and place it in the adjacency matrix
  for i in range (num_edges):
    line = sys.stdin.readline()
    edge = line.strip()
    #print (edge)
    edge = edge.split()
    start = int (edge[0])
    finish = int (edge[1])
    weight = int (edge[2])

    cities.add_directed_edge (start, finish, weight)

  # read the starting vertex for dfs and bfs
  line = sys.stdin.readline()
  start_vertex = line.strip()
  #print (start_vertex)

  # get the index of the starting vertex
  start_index = cities.get_index (start_vertex)
  #print (start_index)

  line = sys.stdin.readline()
  delete_edge = line.strip().split()
  city1 = delete_edge[0]
  city2 = delete_edge[1]

  line = sys.stdin.readline()
  city3 = line.strip()

  # do the depth first search
  print ("Depth First Search")
  cities.dfs (start_index)
  print ()

  # test breadth first search
  print ("Breadth First Search")
  cities.bfs (start_index)
  print()

  print('Deletion of an edge')
  cities.delete_edge(city1, city2)
  # print(city1)
  # print(city2)
  print()

  # print the adjacency matrix
  print ("Adjacency Matrix")
  for i in range (num_vertices):
    for j in range (num_vertices):
      print (cities.adjMat[i][j], end = " ")
    print ()
  print ()

  print('Deletion of a vertex')
  cities.delete_vertex(city3)
  print()


  print('List of Vertices')
  for city in cities.Vertices:
  	print(city)
  print()

  # print the adjacency matrix
  print ("Adjacency Matrix")
  for i in range (len(cities.Vertices)):
    for j in range (len(cities.Vertices)):
      print (cities.adjMat[i][j], end = " ")
    print ()


if __name__ == "__main__":
  main()
