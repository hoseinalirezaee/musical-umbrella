from copy import deepcopy
from random import randint

from networkx import *
from networkx.algorithms.isolate import isolates


def calculate_minimum_vertex_cover(g: Graph, initial_node_id=None):
    """
    calculate minimum vertex cover for given graph using `Jingrong Chen * , Lei Kou, Xiaochuan Cui` algorithm
    and return a set of vertexes.
    :param g: The graph that minimum vertex cover should be calculate on
    :param initial_node_id: initial node id that algorithm should start from
    :return: an instance of set that contains all nodes id that includes in vertex cover
    """
    if not initial_node_id:
        random_number = randint(0, g.number_of_nodes() - 1)
        initial_node_id = random_number

    s = {initial_node_id}
    ordered_s = [initial_node_id]
    h = remove_node_deep(g, s)
    l = set(g.nodes) - (s.union(isolates(g)))

    if number_of_isolates(h) == h.number_of_nodes():
        return s


def remove_node_deep(g, n):
    """
    create a deepcopy from graph `g` and remove given nodes.
    """
    new_g: Graph = deepcopy(g)
    new_g.remove_nodes_from(n)
    return new_g
