import unittest
from src.is_have_graph_cycle import have_cycle


class TestGraphCycle(unittest.TestCase):
    def test_no_cycle(self):
        graph = {
            1: [2],
            2: [3],
            3: []
        }
        self.assertFalse(have_cycle(graph))

    def test_empty_graph(self):
        graph = {}
        self.assertFalse(have_cycle(graph))

    def test_single_vertex(self):
        graph = {
            1: []
        }
        self.assertFalse(have_cycle(graph))


if __name__ == '__main__':
    unittest.main()
