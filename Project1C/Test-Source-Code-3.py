from ortools.graph.python import min_cost_flow


smcf = min_cost_flow.SimpleMinCostFlow()



start_nodes = [1, 1] +     [2] +    [3]   +  [4]      +   [5,5]       +   [6]     +   [7,7,7]
end_nodes =   [2, 4] +     [3] +    [5]   +  [5]      +   [3,6]       +   [5]     +   [4,5,6]
capacities =  [100,80] +   [60] +   [170] +  [170]    +   [60,70]     +   [170]   +   [80,170,70]
costs = (     [30,40]  +   [50] +   [35]  +  [30]     +   [40,35]     +   [25]    +   [50,45,50])
  

source = [1,7]
sink = [2,3,4,5,6]
tasks = 4
supplies = [tasks, 0, 0, 0, 0, 0, 0, 0, 0, -tasks]
