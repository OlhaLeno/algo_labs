import unittest
from src.trie import Trie


class TrieTest(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_find_prefix(self):
        self.trie.insert('banana')
        self.trie.insert('baobab')
        self.assertEqual(self.trie.find_prefix('ba'), True)
        self.assertEqual(self.trie.find_prefix('ba'), True)

    def test_insert_and_find_prefix(self):
        self.trie.insert('banana')
        self.trie.find_prefix('ba')
        self.assertEqual(self.trie.find_prefix('na'), False)

    def test_nothing(self):
        self.trie.insert('')
        self.assertEqual(self.trie.insert(''), None)


if __name__ == '__main__':
    unittest.main()
