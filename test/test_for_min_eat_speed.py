import unittest
from lab2v3l2 import min_eat_speed


class lab2v3l2_test(unittest.TestCase):
    def test_eat_all_bananas(self):
        piles = [3, 6, 7, 11]
        h = 8
        expected_res = 4
        self.assertEqual(min_eat_speed(piles, h), expected_res)


if __name__ == '__main__':
    unittest.main()
