def bubble_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1, 0, -1):
            #print(f"{i} {j}")
            if arr[j] < arr[j - 1]:
                arr[j], arr[j-1] = arr[j - 1], arr[j]
    return arr
