# coding=utf-8

import xlsxParser
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from treelib import Node, Tree

nxG = nx.Graph()
raws = xlsxParser.parser()
samples = 167


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

# Eit = []
# Vit = []
# Nodes = []
# Infected = []
# Eit_seed = []
# Vit_seed = []
# total = 0
# timestamp = 0
# for link in raws:
#     node_in = int(link[0])
#     node_out = int(link[1])
#     currentTime = int(link[2])
#     if currentTime == timestamp + 1:
#         if (node_in == 1) or (node_in in Infected):
#             if node_out not in Infected:
#                 total += 1
#                 Infected.append(node_out)
#     else:
#         timestamp += 1
#         if (node_in == 1) or (node_in in Infected):
#             if node_out not in Infected:
#                 total += 1
#                 Infected.append(node_out)
#         Nodes.append(total)
#         Eit_seed.append(total/167)
#         # Vit_seed.append(np.std(Nodes))
# print(len(Eit_seed))
# plt.figure()
# # plt.subplot(121)
# plt.xlabel('time stamp')
# plt.ylabel('standard varience of infected nodes')
# plt.plot(range(57790), Vit_seed)
# # plt.subplot(122)
# # plt.plot(range(57790), Vit)
# plt.show()

# ******
# Q 10: R
# ******

d = {}
for i in range(samples):
    d[i] = 0
first_time = []
R = []
notUsed = []
limit = int(167 * 0.8)
for seed in range(1, samples):
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
                if currentTime == 57791 and flag:
                    notUsed.append((seed, count))
        else:
            timestamp += 1
            if (node_in == seed) or (node_in in Infected):
                if node_out not in Infected:
                    Infected.append(node_out)
                    count += 1
                if count > limit and flag:
                    flag = False
                    first_time.append((seed, currentTime))
                if currentTime == 57791 and flag:
                    notUsed.append((seed, count))

for i, j in sorted(first_time, key=lambda item: item[1]):
    R.append(i)
for i, j in sorted(notUsed, key=lambda item: item[1])[::-1]:
    R.append(i)


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
# plt.xlabel('f')
# plt.ylabel('rRD')
# plt.plot(all_f, rRD)
# plt.subplot(122)
# plt.xlabel('f')
# plt.ylabel('rRC')
# plt.plot(all_f, rRC)
# plt.show()

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
# # jsonObj = t.to_json()
# # print(jsonObj)
#
# temp = []
# for i in range(1, 168):
#     tag = t.get_node(i).tag
#     data = t.get_node(i).data
#     temp.append((tag, data))
# for i,j in sorted(temp,key=lambda item:item[1])[::-1]:
#     treeRank.append(i)
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
#     fNR = int(f * len(treeRank))
#     RD = []
#     RC = []
#     for node in treeRank[:fNR]:
#         if node in D[:fN]:
#             RD.append(node)
#         if node in C[:fN]:
#             RC.append(node)
#     rRD.append(len(RD) / fNR)
#     rRC.append(len(RC) / fNR)
#
# plt.figure()
# plt.subplot(121)
# plt.xlabel('f')
# plt.ylabel('rTD')
# plt.plot(all_f, rRD)
# plt.subplot(122)
# plt.xlabel('f')
# plt.ylabel('rTC')
# plt.plot(all_f, rRC)
# plt.show()

# ******
# Q 13: R_
# ******

d = {}
for i in range(1, samples):
    d[i] = {}
    for j in range(2):
        d[i][j] = 0
avg_time = {}
for i in range(1, samples):
    avg_time[i] = 0
limit = int(0.8 * 167)

for seed in range(1, samples):
    Infected = []
    timestamp = 0
    for link in raws:
        node_in = int(link[0])
        node_out = int(link[1])
        currentTime = int(link[2])
        if currentTime == timestamp + 1:
            if (node_in == seed) or (node_in in Infected):
                if node_out not in Infected:
                    Infected.append(node_out)
                    d[seed][0] += 1
                    d[seed][1] += currentTime
                if d[seed][0] > limit and avg_time[seed] == 0:
                    avg_time[seed] = d[seed][1] / limit
                if currentTime == 57791 and avg_time[seed] == 0:
                    avg_time[seed] = d[seed][1] / d[seed][0]
        else:
            timestamp += 1
            if (node_in == seed) or (node_in in Infected):
                if node_out not in Infected:
                    Infected.append(node_out)
                    d[seed][0] += 1
                    d[seed][1] += currentTime
                if d[seed][0] > limit and avg_time[seed] == 0:
                    avg_time[seed] = d[seed][1] / limit
                if currentTime == 57791 and avg_time[seed] == 0:
                    avg_time[seed] = d[seed][1] / d[seed][0]

R_ = []
avg_time = {k: int(v) for k, v in avg_time.items() if v != 0}
for i, j in sorted(dict2list(avg_time), key=lambda item: item[1]):
    R_.append(i)
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
#     fNR = int(f * len(R_))
#     RD = []
#     RC = []
#     for node in R_[:fNR]:
#         if node in D[:fN]:
#             RD.append(node)
#         if node in C[:fN]:
#             RC.append(node)
#     rRD.append(len(RD) / fNR)
#     rRC.append(len(RC) / fNR)
#
# plt.figure()
# plt.subplot(121)
# plt.xlabel('f')
# plt.ylabel('rR\'D')
# plt.plot(all_f, rRD)
# plt.subplot(122)
# plt.xlabel('f')
# plt.ylabel('rR\'C')
# plt.plot(all_f, rRC)
# plt.show()

rRR = []
all_f = np.linspace(0.05, 0.5, 10)
for f in all_f:
    fN = int(f * 167)
    fNR = int(f * len(R_))
    RCC = []
    for node in R_[:fNR]:
        if node in R[:fN]:
            RCC.append(node)
    rRR.append(len(RCC) / fNR)

plt.figure()
plt.xlabel('f')
plt.ylabel('rR\'R')
plt.plot(all_f, rRR)
# plt.subplot(122)
# plt.xlabel('f')
# plt.ylabel('rR\'C')
# plt.plot(all_f, rRC)
plt.show()