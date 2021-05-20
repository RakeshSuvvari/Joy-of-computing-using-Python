#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 22:42:47 2021

@author: rakesh
"""

import networkx as nx
import numpy as np

G = nx.read_edgelist("facebook_combined.txt")
N = list(G.nodes())

#shortest path length list
spll = []

for u in N:
    for v in N:
        if u!= v:
            l = nx.shortest_path_length(G,u,v)
            #print("Shortest path between",u,"and",v,"is of length",l)
            spll.append(l)
    print(u)

min_spl = min(spll)
max_spl = max(spll)
avg_spl = np.average(spll)

print("Minimum shortest path length:",min_spl)
print("Maximum shortest path length:",max_spl)
print("Average shortest path length:",avg_spl)

