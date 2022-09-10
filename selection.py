def selection_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    n = len(arr)
    for i in range(n - 1):
        mini = i
        minv = arr[i]
        print(f"{arr}")
        for j in range(i+1, n):
            print(f"{i}:{j}")
            if arr[j] < minv:
                print(f"{mini} <>{j}=> {arr[mini]}<>{arr[j]}")
                mini = j
                minv = arr[j]
        # swap min numbers with elm at pos i
		if arr[i] != arr[mini]:
			print(f"swapping {mini}=>{minv} with {i}=>{arr[i]}")
			arr[i], arr[mini] = arr[mini], arr[i]
    print(arr)
    return arr
