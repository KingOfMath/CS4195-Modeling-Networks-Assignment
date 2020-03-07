# coding=utf-8

import xlsxParser
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from treelib import Node, Tree

nxG = nx.Graph()
raws = xlsxParser.parser()


# --------------------------------------------------------

def dict2list(dic: dict):
    keys = dic.keys()
    vals = dic.values()
    lst = [(key, val) for key, val in zip(keys, vals)]
    return lst


# this graph works without timestamps
# deemed as a final network on the last timestamp
for link in raws:
    node_in = int(link[0])
    node_out = int(link[1])
    if not nxG.has_edge(node_in, node_out):
        nxG.add_edge(node_in, node_out)

# --------------------------------------------------------

# ******
# Q 9: Eit, Vit
# ******
#
# Eit = []
# Vit = []
# for seed in range(1, 30):
#     Nodes = []
#     Infected = []
#     Eit_seed = []
#     Vit_seed = []
#     count = 0
#     total = 0
#     timestamp = 0
#     print("seed:" + str(seed))
#     for link in raws:
#         node_in = int(link[0])
#         node_out = int(link[1])
#         currentTime = int(link[2])
#         if currentTime == timestamp + 1:
#             if (node_in == seed) or (node_in in Infected):
#                 if node_out not in Infected:
#                     count += 1
#                     total += 1
#                     Infected.append(node_out)
#         else:
#             timestamp += 1
#             if (node_in == seed) or (node_in in Infected):
#                 if node_out not in Infected:
#                     count += 1
#                     total += 1
#                     Infected.append(node_out)
#             Nodes.append(count)
#             Eit_seed.append(total / timestamp)
#             # Vit_seed.append(np.std(Nodes))
#             count = 0
#     Eit.append((seed, Eit_seed))
#     # Vit.append((seed,Vit_seed))

#
# plt.figure()
# plt.subplot(121)
# plt.plot(range(57790), Eit)
# plt.subplot(122)
# plt.plot(range(57790), Vit)
# plt.show()

# ******
# Q 10: R
# ******

d = {}
for i in range(30):
    d[i] = 0
first_time = []
R = []
limit = int(167 * 0.8)
for seed in range(1, 30):
    Infected = []
    timestamp = 0
    count = 0
    flag = True
    print("seed:" + str(seed))
    for link in raws:
        node_in = int(link[0])
        node_out = int(link[1])
        currentTime = int(link[2])
        if currentTime == timestamp + 1:
            if (node_in == seed) or (node_in in Infected):
                if node_out not in Infected:
                    Infected.append(node_out)
                    count += 1
                if count > limit and flag:
                    flag = False
                    first_time.append((seed, currentTime))
        else:
            timestamp += 1
            if (node_in == seed) or (node_in in Infected):
                if node_out not in Infected:
                    Infected.append(node_out)
                    count += 1
                if count > limit and flag:
                    flag = False
                    first_time.append((seed, currentTime))

for i, j in sorted(first_time, key=lambda item: item[1]):
    R.append(i)
print(R)

# ******
# Q 11: C,D,rRD,rRC
# ******

D = []
C = []
degree_arr = sorted(nxG.degree, key=lambda item: item[1])[::-1]
cluster_arr = sorted(nx.clustering(nxG).items(), key=lambda item: item[1])[::-1]
for a in degree_arr:
    D.append(a[0])
for a in cluster_arr:
    C.append(a[0])

rRD = []
rRC = []
all_f = np.linspace(0.05, 0.5, 10)
for f in all_f:
    fN = int(f * 167)
    RD = []
    RC = []
    for node in R[:fN]:
        if node in D[:fN]:
            RD.append(node)
        if node in C[:fN]:
            RC.append(node)
    rRD.append(len(RD) / fN)
    rRC.append(len(RC) / fN)

plt.figure()
plt.subplot(121)
plt.xlabel('f')
plt.ylabel('rRD')
plt.plot(all_f, rRD)
plt.subplot(122)
plt.xlabel('f')
plt.ylabel('rRC')
plt.plot(all_f, rRC)
plt.show()

# ******
# Q 12 : P1 => treeRank; P2 => ?
# ******

# Infected = []
# treeRank = []
# timestamp = 0
# t = Tree()
# root = Node(1, 1, data=0)
# t.add_node(root)
# limit = int(167 * 0.8)
# for link in raws:
#     node_in = int(link[0])
#     node_out = int(link[1])
#     currentTime = int(link[2])
#     if currentTime == timestamp + 1:
#         if (node_in == 1) or (node_in in Infected):
#             # only first time infected is used, otherwise it is repeated
#             if node_out not in Infected:
#                 Infected.append(node_out)
#                 t.add_node(Node(node_out, node_out, data=1), parent=t.get_node(node_in))
#                 iter_num = node_out
#                 # update the infected chain to root
#                 while t.parent(iter_num) is not None:
#                     t.parent(iter_num).data += 1
#                     iter_num = t.parent(iter_num).tag
#     else:
#         timestamp += 1
#         if node_in in Infected:
#             if node_out not in Infected:
#                 Infected.append(node_out)
#                 t.add_node(Node(node_out, node_out, data=1), parent=t.get_node(node_in))
#                 iter_num = node_out
#                 # iter
#                 while t.parent(iter_num) is not None:
#                     t.parent(iter_num).data += 1
#                     iter_num = t.parent(iter_num).tag
#
# temp = []
# for i in range(1, 168):
#     tag = t.get_node(i).tag
#     data = t.get_node(i).data
#     temp.append((tag, data))
# for i,j in sorted(temp,key=lambda item:item[1])[::-1]:
#     treeRank.append(i)
#
# print(treeRank[:5])

# ******
# Q 13: R_
# ******

# d = {}
# for i in range(168):
#     d[i] = {}
#     for j in range(2):
#         d[i][j] = 0
# avg_time = {}
# for i in range(168):
#     avg_time[i] = 0
# limit = int(0.8 * 167)
#
# for seed in range(1,167):
#     Infected = []
#     timestamp = 0
#     print("seed:"+str(seed))
#     for link in raws:
#         node_in = int(link[0])
#         node_out = int(link[1])
#         currentTime = int(link[2])
#         if currentTime == timestamp + 1:
#             if (node_in == seed) or (node_in in Infected):
#                 if node_out not in Infected:
#                     Infected.append(node_out)
#                     d[seed][0] += 1
#                     d[seed][1] += currentTime
#                 if d[seed][0] > limit and avg_time[seed] == 0:
#                     avg_time[seed] = d[seed][1] / limit
#         else:
#             timestamp += 1
#             if (node_in == seed) or (node_in in Infected):
#                 if node_out not in Infected:
#                     Infected.append(node_out)
#                     d[seed][0] += 1
#                     d[seed][1] += currentTime
#                 if d[seed][0] > limit and avg_time[seed] == 0:
#                     avg_time[seed] = d[seed][1] / limit
#
# R_ = []
# avg_time = {k: int(v) for k, v in avg_time.items() if v != 0}
# for i, j in sorted(dict2list(avg_time), key=lambda item: item[1]):
#     R_.append(i)
# print(R_)

#
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
#     for node in R_[:fN]:
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
