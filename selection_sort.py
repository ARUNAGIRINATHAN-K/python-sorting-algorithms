def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find minimum element in the unsorted portion
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap minimum element with the first element of unsorted portion
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr