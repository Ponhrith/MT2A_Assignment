import numpy as np
import networkx as nx
import pandas as pd
from ortools.sat.python import cp_model


edgelist_df = pd.DataFrame({'From': ['VN',   'KCham', 'KThom','PP',   'PP','SR','Thai','Thai','Thai', 'VN',   'Thai'],
                            'To':   ['KCham','KThom',  'PP',  'KThom','SR','PP','SR',  'PP',  'KThom','KThom','PP'],
                     'Unit Cost':   [ 30,       50,     35,     40,    35,  25,  50,    45,     50,     40,    45]}) 
                    





max_flow_model = cp_model.CpModel()




