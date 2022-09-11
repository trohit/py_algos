def insertion_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    n = len(arr)
    for i in range(n):
        temp = arr[i]
        red = i-1
        #print(f"a:{arr} i:{i} red:{red} t:{temp}")
        while red >= 0 and arr[red] > temp:
            arr[red+1] = arr[red]
            red -= 1
        #print(f"   a:{arr}")
        #print(f"arr[{red+1}]={temp}")
        arr[red+1] = temp
    return arr
