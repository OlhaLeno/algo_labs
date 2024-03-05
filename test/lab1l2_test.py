import unittest
from lab1l2 import quick_sort  # find_largest_k_el, index_k_largest_el


class lab1l2_test(unittest.TestCase):
    def test_find_largest_k_el(self):
        array = [15, 7, 22, 9, 36, 2, 42, 18]
        k = 3
        sorted_array = quick_sort(array)
        largest_k_el = sorted_array[-k]
        self.assertEqual(largest_k_el, 22)


if __name__ == '__main__':
    unittest.main()
