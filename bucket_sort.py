def bucket_sort(arr):
    # Assumes input in range [0, 1) for simplicity
    n = len(arr)
    buckets = [[] for _ in range(n)]
    
    # Place elements in buckets
    for num in arr:
        index = int(num * n)
        buckets[index].append(num)
    
    # Sort individual buckets (using insertion sort)
    for bucket in buckets:
        bucket.sort()
    
    # Concatenate buckets
    result = []
    for bucket in buckets:
        result.extend(bucket)
    
    return result