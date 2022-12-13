def bubblesort(input_array):
    n = len(input_array)
    for i in range(n):
        for j in range(n - 1):
            if input_array[j] > input_array[j + 1]:
                temp = input_array[j]
                input_array[j] = input_array[j + 1]
                input_array[j + 1] = temp
