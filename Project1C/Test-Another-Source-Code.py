
from ortools.graph.python import pywrapgraph


def main():
    start_nodes = ([1,1,2,3,3,4,5,5,6,7,7,7])
    end_nodes =   ([2,3,3,4,4,5,5,5,5,6,6])
    capacities =  ([100,60,80,170,70])

    max_flow = pywrapgraph.SimpleMaxFlow()
    for i in range(0, len(start_nodes)):
        max_flow.AddArcWithCapacity(start_nodes[i], end_nodes[i], capacities[i])
    
    #find the optimal max flow value
    if max_flow.Solve(0, 6) == max_flow.OPTIMAL:
        print('Max flow:', max_flow.OptimalFlow())
        print('------------------------')
        print('  Arc    Flow / Capacity')
        for i in range(max_flow.NumArcs()):
            print('%1s -> %1s   %3s  / %3s' % (
            max_flow.Tail(i),
            max_flow.Head(i),
            max_flow.Flow(i),
            max_flow.Capacity(i)))
    else:
        print('There was an issue with the max flow input.')


if __name__ == '__main__':
    main()
