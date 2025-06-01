def counting_sort(arr):
    # Assumes non-negative integers
    max_val = max(arr)
    count = [0] * (max_val + 1)
    output = [0] * len(arr)
    
    # Count occurrences
    for num in arr:
        count[num] += 1
    
    # Cumulative count
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # Place elements in sorted order
    for num in arr[::-1]:
        output[count[num] - 1] = num
        count[num] -= 1
    
    return output