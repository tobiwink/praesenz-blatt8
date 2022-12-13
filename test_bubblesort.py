import unittest
import bubblesort

class TestBubbleSort(unittest.TestCase):
    def test_a_normal_array(self):
        input_array = [3, 2, 1]
        bubblesort.bubblesort(input_array)
        self.assertEqual([1, 2, 3], input_array)
    def test_an_empty_array(self):
        input_array = []
        bubblesort.bubblesort(input_array)
        self.assertEqual([], input_array)
    def test_array_with_1_element(self):
        input_array = [1]
        bubblesort.bubblesort(input_array)
        self.assertEqual([1], input_array)


if __name__ == '__main__':
    unittest.main()
