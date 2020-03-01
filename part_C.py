# _*_ coding:utf-8 _*_
# coding=utf-8

import xlsxParser
import graph_tools as gt
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pathpy as pp
import jgraph

# g = gt.Graph(directed=True)
# nxG = nx.Graph()
timestamps = xlsxParser.parser()
t = pp.TemporalNetwork()

# --------------------------------------------------------
# this graph works without timestamps
# deemed as a final network on the last timestamp
for link in timestamps:
    node_in = link[0]
    node_out = link[1]
    t.add_edge(source=node_in,target=node_out,ts=int(link[2]))

# --------------------------------------------------------

jgraph.draw(t)


