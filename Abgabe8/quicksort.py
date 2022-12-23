def quick_sort_builder(array):
    if len(array) < 2:
        return array
    
    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    
    return quick_sort_builder(less) + [pivot] + quick_sort_builder(greater)


def quickSort(array):
    array[:] = quick_sort_builder(array)


if __name__ == '__main__':
    import random
    random.seed(0)
    array = [random.randint(0, 1000000) for _ in range(1000000)]
    # print(array)
    print(quickSort(array))