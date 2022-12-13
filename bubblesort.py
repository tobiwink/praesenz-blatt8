from typing import List

def bubblesort(input_array: List[int]):
    """
    Sorting an input array inplace in ascending order.

    :param input_array: an input array of integers, can be empty.
    :return: None
    """
    n = len(input_array)
    for i in range(n):
        for j in range(n - 1):
            if input_array[j] > input_array[j + 1]:
                temp = input_array[j]
                input_array[j] = input_array[j + 1]
                input_array[j + 1] = temp
