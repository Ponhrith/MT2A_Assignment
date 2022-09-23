"""From Taha 'Introduction to Operations Research', example 6.4-2."""
from ortools.graph.python import max_flow

import numpy as np


def main():
    """MaxFlow simple interface example."""
    # Instantiate a SimpleMaxFlow solver.
    smf = max_flow.SimpleMaxFlow()

    # Define three parallel arrays: start_nodes, end_nodes, and the capacities
    # between each pair. For instance, the arc from node 0 to node 1 has a
    # capacity of 20.
    start_nodes = np.array([1,   1,   2,  3,   4,   5,  5,  6,   7,  7,   7]) 
    end_nodes = np.array  ([2,   4,   3,  5,   5,   3,  6,  5,   4,  5,   6]) 
    capacities = np.array([100, 80,  60, 170, 170, 60, 70, 170, 80, 170, 70]) 

    # Add arcs in bulk. 
    #   note: we could have used add_arc_with_capacity(start, end, capacity)
    smf.add_arcs_with_capacity(start_nodes, end_nodes, capacities)

    # Find the maximum flow between node 0 and node 4.
    status = smf.solve(1, 7)

    if status != smf.OPTIMAL:
        print('There was an issue with the max flow input.')
        print(f'Status: {status}')
        exit(1)
    print('Max flow:', smf.optimal_flow())
    print('')
    print('  Arc    Flow / Capacity')
    for i in range(smf.num_arcs()):
        print('%1s -> %1s   %3s  / %3s' %
              (smf.tail(i), smf.head(i), smf.flow(i), smf.capacity(i)))
    print('Source side min-cut:', smf.get_source_side_min_cut())
    print('Sink side min-cut:', smf.get_sink_side_min_cut())


if __name__ == '__main__':
    main()