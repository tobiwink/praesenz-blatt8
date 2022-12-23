import unittest

import numpy as np

from quicksort import quickSort
from selectionsort import selectionSort

class TestSorting(unittest.TestCase):
    def edge_cases(self, sorting_function):
        array = []
        sorting_function(array)
        self.assertEqual(array, [])

        array = [1]
        sorting_function(array)
        self.assertEqual(array, [1])
    
    def easy_cases(self, sorting_function):
        array = [1, 2, 3, 4, 5]
        sorting_function(array)
        self.assertEqual(array, [1, 2, 3, 4, 5])

        array = [5, 4, 3, 2, 1]
        sorting_function(array)
        self.assertEqual(array, [1, 2, 3, 4, 5])

        array = [1, 3, 5, 2, 4]
        sorting_function(array)
        self.assertEqual(array, [1, 2, 3, 4, 5])

    def random_lists(self, sorting_function):
        np.random.seed(42)
        for _ in range(100):
            array = np.random.randint(low=0, high=1000000, size=np.random.randint(low=0, high=100))
            array_copy = array.copy()
            array_copy.sort()

            sorting_function(array)

            self.assertEqual(array.tolist(), array_copy.tolist())

    def big_list(self, sorting_function):
        np.random.seed(42)
        array = np.random.randint(low=0, high=1000000, size=10000)
        array_copy = array.copy()
        array_copy.sort()

        sorting_function(array)

        self.assertEqual(array.tolist(), array_copy.tolist())

    def test_selection_sort_edge_cases(self):
        self.edge_cases(selectionSort)
    
    def test_selection_sort_easy_cases(self):
        self.easy_cases(selectionSort)
    
    def test_selection_sort_random_lists(self):
        self.random_lists(selectionSort)
    
    def test_selection_sort_big_list(self):
        self.big_list(selectionSort)

    def test_quick_sort_edge_cases(self):
        self.edge_cases(quickSort)
    
    def test_quick_sort_easy_cases(self):
        self.easy_cases(quickSort)
    
    def test_quick_sort_random_lists(self):
        self.random_lists(quickSort)

    def test_quick_sort_big_list(self):
        self.big_list(quickSort)


if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)