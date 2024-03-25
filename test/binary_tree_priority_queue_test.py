import unittest
from binary_tree_priority_queue import PriorityQueue


class TestPriorityQueue(unittest.TestCase):

    def setUp(self):
        self.queue = PriorityQueue()

    def test_find_highest_priority(self):
        self.queue.insert(5, 2)
        self.queue.insert(10, 1)
        self.queue.insert(15, 3)
        self.assertEqual(self.queue.find_highest_priority(), 15)


if __name__ == '__main__':
    unittest.main()
