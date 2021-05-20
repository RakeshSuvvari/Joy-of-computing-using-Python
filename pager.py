#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 20 13:00:28 2021

@author: rakesh
"""

import networkx as nx
import matplotlib.pyplot as plt
import operator

G=nx.read_edgelist('pagerank.txt', create_using=nx.DiGraph(), nodetype=int)
nx.draw(G,with_labels=True)
plt.show()
p=nx.pagerank(G)
sorted_p=sorted(p.items(),key=operator.itemgetter(1),reverse=True)
print(sorted_p)