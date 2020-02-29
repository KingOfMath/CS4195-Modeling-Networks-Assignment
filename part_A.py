# coding=utf-8

import xlsxParser
import graph_tools as gt
import numpy as np
import networkx as nx

g = gt.Graph(directed=True)
nxG = nx.Graph()
timestamps = xlsxParser.parser()

# --------------------------------------------------------
# this graph works without timestamps
# deemed as a final network on the last timestamp
for link in timestamps:
    node_in = int(link[0])
    node_out = int(link[1])
    if not g.has_edge(node_in, node_out):
        g.add_edge(node_in, node_out)
    if not nxG.has_edge(node_in, node_out):
        nxG.add_edge(node_in, node_out)

# --------------------------------------------------------

# ******
# Q 1 : N,L,p,ED,VarD
# ******
N = len(g.vertices())
L = len(g.edges())
p = nx.density(nxG)
ED = []
VarD = []

# ******
# Q 3 : pD => -0.29 ???
# ******
pD = nx.degree_assortativity_coefficient(nxG)

# ******
# Q 4 : cc
# ******
cc_dict = nx.clustering(nxG)
cc = np.sum(cc_dict[i] for i in range(1, N)) / N

# ******
# Q 5 : EH,Hmax
# comment line 585
# ******
betweenness = 0
for i in range(1, N):
    betweenness_each = g.betweenness(i)
    betweenness += betweenness_each
EH = 2 * betweenness / (N * (N - 1))

Hmax = 0
for each in nx.shortest_path_length(nxG):
    for _, v in each[1].items():
        if v > Hmax:
            Hmax = v

# ******
# Q 7 : max_adj_eigval => 0 ???
# ******
adj_matrix_eigvals = g.adjacency_matrix_eigvals()
max_adj_eigval = adj_matrix_eigvals[-1]

# ******
# Q 8 : second_min_lap_eigval
# ******
lap_matrix_eigvals = g.laplacian_matrix_eigvals()
second_min_lap_eigval = lap_matrix_eigvals[1]

# --------------------------------------------------------


