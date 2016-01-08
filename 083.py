# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 23:27:29 EST 2016

@author: aaditya prakash
"""

from time import clock
from collections import defaultdict
from heapq import heappop, heappush
from itertools import product
from numpy import zeros

problem_number = '083'
problem_statement = """ Find the minimal path sum, in matrix.txt """

class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance


def Dijkstra(graph, start):
    A = {}
    queue = [(0, start)]
    while queue:
        path_len, v = heappop(queue)
        if A.get(v, None) is None: # v is unvisited
            A[v] = path_len
            for w in graph.edges[v]:
                edge_len = graph.distances[(v,w)]
                if A.get(w, None) is None:
                    heappush(queue, (path_len + edge_len, w))

    return A

def make_graph(m):
    g = Graph()

    nrow, ncol =  m.shape
    for r,c in product(xrange(nrow), xrange(ncol)):
        g.add_node((r,c))

    for r,c in product(xrange(nrow), xrange(ncol)):

        # Add edge for UP
        if r != 0: # no UP for top row
            g.add_edge((r,c), (r-1,c), m[r-1,c])

        # Add edge for Down
        if r != nrow -1: # no DOWN for bottom row
            g.add_edge((r,c), (r+1,c), m[r+1,c])

        # Add edge for Right
        if c != ncol -1: # no Right for last COL
            g.add_edge((r,c), (r,c+1), m[r,c+1])

        # Add edge for Left
        if c != 0: # no LEFT for first column
            g.add_edge((r,c), (r,c-1), m[r,c-1])

    return g

def solve_four_ways(m):
    g = make_graph(m)

    nrow, ncol = m.shape

    return Dijkstra(g,(0,0))[nrow-1,ncol-1] + m[0,0]



def read_data(filename):
    """ reads the matrix from a text file 'filename' and stores it into a list of lists """
    mat= []
    with open(filename) as f:
        for line in f:
            mat.append( map(int, line.strip().split(',')))
    
    # this is because numpy matrix requires predefined size
    m = zeros((len(mat),len(mat[0])))
    for i,l in enumerate(mat):
        m[i,:] = l
    return m

timeStart = clock()
print solve_four_ways(read_data('./files/p083_matrix.txt'))
print('Time (sec):' + str(clock() - timeStart))
answer = '425185'



