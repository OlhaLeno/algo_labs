import unittest
from src.find_largesr_k_el import quick_sort


class TestQuickSort(unittest.TestCase):
    def test_quick_sort(self):
        arr = [15, 7, 22, 9, 36, 2, 42, 18]
        expected_arr = [2, 7, 9, 15, 18, 22, 36, 42]
        sorted_arr = quick_sort(arr)
        self.assertEqual(sorted_arr, expected_arr)


class TestFindLafgestKel(unittest.TestCase):
    def test_find_largest_k_el(self):
        arr = [15, 7, 22, 9, 36, 2, 42, 18]
        k = 3
        sorted_arr = quick_sort(arr)
        largest_k_el = sorted_arr[-k]
        self.assertEqual(largest_k_el, 22)


class TestIndexKlargestel(unittest.TestCase):
    def test_index_k_largest_el(self):
        arr = [15, 7, 22, 9, 36, 2, 42, 18]
        k = 3
        expected_index = 2
        sorted_arr = quick_sort(arr)
        largest_k_el = sorted_arr[-k]
        index = arr.index(largest_k_el)
        self.assertEqual(index, expected_index)


if __name__ == '__main__':
    unittest.main()
