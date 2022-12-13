import unittest
import bubblesort

class TestBubbleSort(unittest.TestCase):
    def test1(self):
        input_array = [3, 2, 1]
        bubblesort.bubblesort(input_array)
        self.assertEqual([1, 2, 3], input_array)  # add assertion here


if __name__ == '__main__':
    unittest.main()
