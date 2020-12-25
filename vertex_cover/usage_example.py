from networkx import Graph
from networkx.readwrite.edgelist import read_weighted_edgelist

from graph import MinimumVertexCoverSolver

if __name__ == '__main__':
    graph = read_weighted_edgelist('test_graph.txt', nodetype=int)
    solver = MinimumVertexCoverSolver()
    for i in range(1, 25):
        result = solver(graph, i)
        t: Graph = graph.subgraph(set(graph.nodes) - result)
        is_min = t.number_of_edges() == 0
        print('%s - %s: %s' % (is_min, list(result), len(result)))
