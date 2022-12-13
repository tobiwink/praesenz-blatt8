import unittest
import bubblesort

class TestBubbleSort(unittest.TestCase):
    def test1(self):
        input_array = [3, 2, 1]
        bubblesort.bubblesort(input_array)
        self.assertEqual([1, 2, 3], input_array)  # add assertion here
    def test2(self):
        input_array = []
        bubblesort.bubblesort(input_array)
        self.assertEqual([], input_array)  # add assertion here
    def test3(self):
        input_array = [1]
        bubblesort.bubblesort(input_array)
        self.assertEqual([1], input_array)  # add assertion here


if __name__ == '__main__':
    unittest.main()
