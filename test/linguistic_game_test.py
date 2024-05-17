import unittest
from src.linguistic_game import len_of_max_chain


class TestWordChain(unittest.TestCase):

    def setUp(self):
        self.input_file = "wchain.in"
        self.output_file = "wchain.out"

    def write_input_file(self, data: str):
        with open(self.input_file, "w") as file:
            file.write(data)

    def read_output_file(self) -> int:
        with open(self.output_file, "r") as file:
            return int(file.read().strip())

    def test_chain_1(self):
        input_data = "10\ncrates\ncar\ncats\ncrate\nrate\nat\nate\ntea\nrat\na\n"
        expected_result = 6
        self.write_input_file(input_data)
        len_of_max_chain(self.input_file, self.output_file)
        result = self.read_output_file()
        self.assertEqual(result, expected_result)

    def test_chain_2(self):
        input_data = "5\nb\nbcad\nbca\nbad\nbd\n"
        expected_result = 4
        self.write_input_file(input_data)
        len_of_max_chain(self.input_file, self.output_file)
        result = self.read_output_file()
        self.assertEqual(result, expected_result)

    def test_chain_3(self):
        input_data = "4\nword\nanotherword\nabc\nyetanotherword\n"
        expected_result = 1
        self.write_input_file(input_data)
        len_of_max_chain(self.input_file, self.output_file)
        result = self.read_output_file()
        self.assertEqual(result, expected_result)


if __name__ == "__main":
    unittest.main()
