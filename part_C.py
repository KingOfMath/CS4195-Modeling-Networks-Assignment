# _*_ coding:utf-8 _*_
# coding=utf-8

import xlsxParser
import graph_tools as gt
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pathpy as pp
import jgraph
from IPython.display import *
from IPython.display import HTML

# g = gt.Graph(directed=True)
# nxG = nx.Graph()
raws = xlsxParser.parser()
t = pp.TemporalNetwork()

# --------------------------------------------------------
# this graph works without timestamps
# deemed as a final network on the last timestamp
for link in raws:
    node_in = link[0]
    node_out = link[1]
    t.add_edge(source=node_in,target=node_out,ts=int(link[2]))

# --------------------------------------------------------

# work only in HTML
jgraph.draw(t)
plt.show()

# ******
# Q 14
# ******


# ******
# Q 15
# ******

