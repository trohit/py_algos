#!/usr/bin/env python
def qs(a):
    n = len(a)
    if n < 2: return a
    lwi = 0  # partition on pivot elm which is leftmost elm
    for i in range(1, n):
        if a[i] <= a[0]:
            lwi += 1
            a[lwi], a[i] = a[i], a[lwi]
    a[0], a[lwi] = a[lwi], a[0]
    l = qs(a[:lwi])
    r = qs(a[lwi + 1 :])
    a = l + [a[lwi]] + r
    return a


# main
# import random
# a = random.sample(range(100), 7)
a = [4, 3, 7, 2, 9, 1, 8]
a = qs(a)
print(f"s:{a}")
