# coding=utf-8

import xlsxParser
import graph_tools as gt
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import anytree as at

from treelib import Node, Tree

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

# Nodes = []
# Infected = []
# Eit = []
# Vit = []
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
#         Nodes.append(count)
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

Infected = []
R = []
timestamp = 0
t = Tree()
# root node, still pure
root = Node(1, 1, data=0)
t.add_node(root)
limit = int(167*0.8)
for link in raws:
    node_in = int(link[0])
    node_out = int(link[1])
    currentTime = int(link[2])
    if currentTime == timestamp + 1:
        if (node_in == 1) or (node_in in Infected):
            # only first time infected is used, otherwise it is repeated
            if node_out not in Infected:
                Infected.append(node_out)
                t.add_node(Node(node_out, node_out, data=1), parent=t.get_node(node_in))
                iter_num = node_out
                # update the infected chain to root
                while t.parent(iter_num) is not None:
                    t.parent(iter_num).data += 1
                    iter_num = t.parent(iter_num).tag
                    print(str(t.get_node(iter_num).tag) + "," + str(t.get_node(iter_num).data))
                    if t.get_node(iter_num).data > limit and iter_num not in R:
                        R.append(iter_num)
    else:
        timestamp += 1
        if node_in in Infected:
            if node_out not in Infected:
                Infected.append(node_out)
                t.add_node(Node(node_out, node_out, data=1), parent=t.get_node(node_in))
                iter_num = node_out
                # iter
                while t.parent(iter_num) is not None:
                    t.parent(iter_num).data += 1
                    iter_num = t.parent(iter_num).tag
                    print(str(t.get_node(iter_num).tag) + "," + str(t.get_node(iter_num).data))
                    if t.get_node(iter_num).data > limit and iter_num not in R:
                        R.append(iter_num)
print(R)

# ******
# Q 11: C,D,rRD,rRC
# ******

# D = []
# C = []
# degree_arr = sorted(nxG.degree, key=lambda item: item[1])[::-1]
# cluster_arr = sorted(nx.clustering(nxG).items(), key=lambda item: item[1])[::-1]
# for a in degree_arr:
#     D.append(a[0])
# for a in cluster_arr:
#     C.append(a[0])
#
# rRD = []
# rRC = []
# all_f = np.linspace(0.05, 0.5, 10)
# for f in all_f:
#     fN = int(f * 167)
#     RD = []
#     RC = []
#     for node in R[:fN]:
#         if node in D[:fN]:
#             RD.append(node)
#         if node in C[:fN]:
#             RC.append(node)
#     rRD.append(len(RD) / fN)
#     rRC.append(len(RC) / fN)
#
# plt.figure()
# plt.subplot(121)
# plt.plot(all_f, rRD)
# plt.subplot(122)
# plt.plot(all_f, rRC)
# plt.show()

# ******
# Q 12
# ******


# ******
# Q 13: R_(?)
# ******

# Infected = []
# R_ = []
# count = 0
# timestamp = 0
# rootNode = at.Node(1, None)
# nodes = [].append(rootNode)
# d = {rootNode.name:0}
# for link in raws:
#     node_in = int(link[0])
#     node_out = int(link[1])
#     currentTime = int(link[2])
#     if currentTime == timestamp + 1:
#         if (node_in == 1) or (node_in in Infected):
#             Infected.append(node_out)
#             cur_node = at.Node(node_out, node_in)
#             # first time infected
#             if cur_node not in nodes:
#                 nodes.append(cur_node)
#                 d[cur_node.name] = 1
#
#             else:
#                 pass
#     else:
#         timestamp += 1
#         if node_in in Infected:
#             d[node_in] += 1
#             Infected.append(node_out)

# d = {}
# for i in range(168):
#     d[i] = {}
#     for j in range(168):
#         d[i][j] = 0
# R_ = {}
# for i in range(168):
#     R_[i] = 0
# Infected = []
# count = 0
# timestamp = 0
# limit = int(0.8*167)
# for link in raws:
#     node_in = int(link[0])
#     node_out = int(link[1])
#     currentTime = int(link[2])
#     if currentTime == timestamp + 1:
#         if (node_in == 1) or (node_in in Infected):
#             if d[node_in][node_out] == 0:
#                 d[node_in][node_out] = currentTime
#                 d[node_in][0] += 1
#                 print(d[node_in][0])
#             Infected.append(node_out)
#             if d[node_in][0] > limit:
#                 R_[node_in] = np.sum(each for each in d[node_in].values())/limit
#     else:
#         timestamp += 1
#         if node_in in Infected:
#             if d[node_in][node_out] == 0:
#                 d[node_in][node_out] = currentTime
#                 d[node_in][0] += 1
#             Infected.append(node_out)
#             if d[node_in][0] > limit:
#                 R_[node_in] = np.sum(each for each in d[node_in].values())/limit
#
# print(R_)
