"""
Time:O(k+n)
Space:O(k+n)
"""
def counting_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    a = arr
    # print(f"u:{a}")
    dd = {}
    n = len(a)
    for i in range(n):
        if a[i] in dd:
            dd[a[i]] += 1
        else:
            dd[a[i]] = 1
    pos = 0
    # print(f"keys:{dd.keys()}")
    for num in sorted(dd.keys()):
        for i in range(dd[num]):
            a[pos] = num
            pos += 1
    # print(f"s:{a}")
    return a
