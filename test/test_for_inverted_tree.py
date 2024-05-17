import unittest
from src.invert_binary_tree import invert_binary_tree, BinaryTree


class InvertationCase(unittest.TestCase):
    def test_1(self):
        tree = BinaryTree(1)
        tree.left = BinaryTree(2)
        tree.right = BinaryTree(3)

        inverted_tree = invert_binary_tree(tree)

        self.assertEqual(inverted_tree.value, 1)
        self.assertEqual(inverted_tree.left.value, 3)
        self.assertEqual(inverted_tree.right.value, 2)


if __name__ == '__main__':
    unittest.main()
