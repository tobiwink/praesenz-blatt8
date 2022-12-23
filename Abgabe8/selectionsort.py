def selectionSort(array, copy=False):
    """
    Sorts the given array using the selection sort algorithm and modifies the array.

    Parameters
    ----------
    array : Sortable array
        Array to be sorted.
        copy : bool, optional
            If True, the array will be copied before sorting. The default is False.
    
    Returns
    -------
        None
    """
    if copy:
        arr = array.copy()
    
    else:
        arr = array

    for i, _ in enumerate(arr):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
