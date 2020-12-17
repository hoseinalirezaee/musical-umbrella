from unittest import TestCase

from networkx.readwrite.edgelist import read_weighted_edgelist

from vertex_cover.graph import calculate_minimum_vertex_cover


class Test(TestCase):

    def _test(self, init_node_id, expected_result):
        graph = read_weighted_edgelist('test_graph.txt')
        result = calculate_minimum_vertex_cover(graph, init_node_id)
        self.assertIsInstance(result, set)
        self.assertSetEqual(result, expected_result)

    def test_init_vertex_6(self):
        expected = {3, 5, 6, 7, 8, 9, 11, 12, 15, 16, 17, 18, 19, 20, 21, 25}
        self._test(6, expected)
