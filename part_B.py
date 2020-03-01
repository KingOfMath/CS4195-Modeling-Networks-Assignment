# coding=utf-8

import xlsxParser
import graph_tools as gt
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import anytree as at

# g = gt.Graph(directed=True)
nxG = nx.Graph()
raws = xlsxParser.parser()

# --------------------------------------------------------
# this graph works without timestamps
# deemed as a final network on the last timestamp
for link in raws:
    node_in = int(link[0])
    node_out = int(link[1])
    if not nxG.has_edge(node_in, node_out):
        nxG.add_edge(node_in, node_out)

# --------------------------------------------------------

# ******
# Q 9: Eit, Vit(?)
# ******

# Eit = []
# Infected = []
# count = 0
# timestamp = 0
# for link in raws:
#     node_in = int(link[0])
#     node_out = int(link[1])
#     currentTime = int(link[2])
#     if currentTime == timestamp + 1:
#         if (node_in == 1) or (node_in in Infected):
#             count += 1
#             Infected.append(node_out)
#     else:
#         timestamp += 1
#         Eit.append(count/timestamp)
#         if node_in in Infected:
#             count += 1
#             Infected.append(node_out)

# ******
# Q 10: R
# ******

# d = {}
# for i in range(168):
#     d[i] = 0
# Infected = []
# R = []
# count = 0
# timestamp = 0
# for link in raws:
#     node_in = int(link[0])
#     node_out = int(link[1])
#     currentTime = int(link[2])
#     if currentTime == timestamp + 1:
#         if (node_in == 1) or (node_in in Infected):
#             d[node_in] += 1
#             Infected.append(node_out)
#             if d[node_in] > 0.8 * 167 and node_in not in R:
#                 R.append(node_in)
#     else:
#         timestamp += 1
#         if node_in in Infected:
#             d[node_in] += 1
#             Infected.append(node_out)
#             if d[node_in] > 0.8 * 167 and node_in not in R:
#                 R.append(node_in)

# ******
# Q 11
# ******



# ******
# Q 12
# ******



# ******
# Q 13: R_
# ******

Infected = []
R_ = []
count = 0
timestamp = 0
rootNode = at.Node(1, None)
nodes = [].append(rootNode)
d = {rootNode.name:0}
for link in raws:
    node_in = int(link[0])
    node_out = int(link[1])
    currentTime = int(link[2])
    if currentTime == timestamp + 1:
        if (node_in == 1) or (node_in in Infected):
            Infected.append(node_out)
            cur_node = at.Node(node_out, node_in)
            # first time infected
            if cur_node not in nodes:
                nodes.append(cur_node)
                d[node_out] = 1

            else:
                pass
    else:
        timestamp += 1
        if node_in in Infected:
            d[node_in] += 1
            Infected.append(node_out)


