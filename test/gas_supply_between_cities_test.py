import unittest
from gas_supply_between_cities import gas_supply


class GasSupply(unittest.TestCase):
    def test_no_cities(self):
        cities = []
        storages = ["storage_1", "storage_2"]
        pipes = [["storage_1", "storage_2"]]
        self.assertEqual(gas_supply(cities, storages, pipes), {})

    def test_no_storages(self):
        cities = ['Lviv', 'Striy', 'Dolina', 'Kyiv', 'Mykolaiv']
        storages = []
        pipes = [['Lviv', 'Striy'], ['Lviv', 'Dolina'], ['Lviv', 'Kyiv']]
        self.assertEqual(gas_supply(cities, storages, pipes), {})


if __name__ == '__main__':
    unittest.main()
