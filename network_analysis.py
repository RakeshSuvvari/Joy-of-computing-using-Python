#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 22:11:56 2021

@author: rakesh
"""

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G = nx.gnp_random_graph(4,1)
#G = nx.barabasi_albert_graph(50,2)

nx.draw(G)
plt.show()

#nx.write_gexf(G,"nx_analysis.gexf")