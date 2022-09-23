from ortools.graph.python import min_cost_flow
import numpy as np
def main():

    smcf = min_cost_flow.SimpleMinCostFlow()

    start_nodes = np.array ([1,   1,   2,  3,   4,   5,  5,  6,   7,  7,   7])  
    end_nodes = np.array   ([2,   4,   3,  5,   5,   3,  6,  5,   4,  5,   6]) 
    capacities = np.array  ([100, 80,  60, 170, 170, 60, 70, 170, 80, 170, 70]) 
    unit_costs = np.array  ([30,  40,  50, 35,  30,  40, 35, 25,  50, 45,  50]) 

    supplies =[200,100,60,80,170,70,300]


    smcf.add_arcs_with_capacity_and_unit_cost(start_nodes, end_nodes, capacities, unit_costs)


    for count, supply in enumerate(supplies):
        smcf.set_node_supply(count, supply)

    status = smcf.solve()

    if status != smcf.OPTIMAL:
        print('There was an issue with the min cost flow input.')
        print(f'Status: {status}')
        exit(1)
    print('Minimum cost: ', smcf.optimal_cost())
    print('')
    print(' Arc   Flow / Capacity  Cost')
    for i in range(smcf.num_arcs()):
        cost = smcf.flow(i) * smcf.unit_cost(i)
        print(
            '%1s -> %1s    %3s   / %3s   %3s' %
            (smcf.tail(i), smcf.head(i), smcf.flow(i), smcf.capacity(i), cost))


if __name__ == '__main__':
    main()
