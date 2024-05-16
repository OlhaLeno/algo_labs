import unittest
from collections import defaultdict
from flowers_delivery import max_flow, dfs


class TestOneMoreTime(unittest.TestCase):
    def test_dfs(self):
        graph = {'A': ['B', 'C'], 'B': ['C'], 'C': ['D'], 'D': []}
        visited = set()
        start = 'A'
        end = 'D'
        self.assertEqual(dfs(graph, visited, start, end), [['A', 'C', 'D']])

    def test_max_flow(self):
        graph = defaultdict(dict)
        graph['SOURCE'] = {'A': 5}
        graph['A'] = {'B': 3, 'C': 2}
        graph['B'] = {'SINK': 2}
        graph['C'] = {'SINK': 3}
        max_flow_val = max_flow(graph)
        self.assertIsInstance(max_flow_val, int)


if __name__ == '__main__':
    unittest.main()
