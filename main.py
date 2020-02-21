# coding=utf-8

import xlsxParser
import graph_tools as gt
import numpy as np

g = gt.Graph(directed=True)
timestamps = xlsxParser.parser()

# --------------------------------------------------------
# this graph works without timestamps
# deemed as a final network on the last timestamp
for link in timestamps:
    node_in = int(link[0])
    node_out = int(link[1])
    if not g.has_edge(node_in, node_out):
        g.add_edge(node_in, node_out)

# --------------------------------------------------------

# ******
# Q 1
# ******
N = len(g.vertices())
L = len(g.edges())

# ******
# Q 5
# comment line 585
# ******
betweenness = 0
for i in range(1, N):
    betweenness_each = g.betweenness(i)
    betweenness += betweenness_each
EH = 2 * betweenness / (N * (N - 1))


# ******
# Q 7  ??? => 0
# ******
adj_matrix_eigvals = g.adjacency_matrix_eigvals()
max_adj_eigval = adj_matrix_eigvals[-1]

# ******
# Q 8
# ******
lap_matrix_eigvals = g.laplacian_matrix_eigvals()
second_min_lap_eigval = lap_matrix_eigvals[1]
