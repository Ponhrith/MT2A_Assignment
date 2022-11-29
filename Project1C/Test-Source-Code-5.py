import numpy as np
import networkx as nx
import pandas as pd
from ortools.sat.python import cp_model


edgelist_df = pd.DataFrame({'From': ['VN',   'KCham', 'KThom','PP',   'PP','SR','Thai','Thai','Thai', 'VN',   'Thai'],
                            'To':   ['KCham','KThom',  'PP',  'KThom','SR','PP','SR',  'PP',  'KThom','KThom','PP'],
                        'Weight':   [[100,      80,     60,     170,   170, 60,  70,    170,    80,     170,   70]],
                     'Unit Cost':   [ 30,       50,     35,     40,    35,  25,  50,    45,     50,     40,    45]}) 
                    
g = nx.DiGraph()
for i, elrow in edgelist_df.iterrows():
    g.add_edge(elrow[0], elrow[1], weight = elrow[2], unitCost = elrow[3])
g.edges(data=True)


OutEdgeDataView = ([('s', 'u', {'weight': 20, 'cost': 3.0}), ('s', 'v', {'weight': 10, 'cost': 2.0}), ('u', 'v', {'weight': 30, 'cost': 0.7}), ('u', 't', {'weight': 10, 'cost': 1.0}), ('v', 't', {'weight': 20, 'cost': 7.0})])

max_flow_model = cp_model.CpModel()



