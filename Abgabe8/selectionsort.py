def selectionSort(array, copy=False):
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
    return arr

if __name__ == '__main__':
    import random
    random.seed(0)
    array = [random.randint(0, 100) for _ in range(10)]
    print(array)
    print(selectionSort(array))