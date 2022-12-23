
def quick_sort_builder(array):
    """
    Sorts the given array using the quick sort algorithm.

    NOTE: This function is not meant to be called directly. Use quickSort instead.

    Parameters
    ----------
    array : Sortable array
        Array to be sorted.
    
    Returns
    -------
    sorted array

    """
    if len(array) < 2:
        return array
    
    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    
    return quick_sort_builder(less) + [pivot] + quick_sort_builder(greater)


def quickSort(array):
    """
    Sorts the given array using the quick sort algorithm and modifies the array.

    Parameters
    ----------
    array : Sortable array
        Array to be sorted.
    
    Returns
    -------
        None
    """
    array[:] = quick_sort_builder(array)