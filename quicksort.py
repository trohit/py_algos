#!/usr/bin/env python

import random
# the simplest quicksort that one can use in interview + passes leetcode
# siplifies the partitioning and uses and O(n) extra space on avg but O(n^2) in worst case 
def q(a):
    n = len(a)
    if n <= 1: return a
    pivot = random.choice(a)
    l = [v for v in a if v <= pivot]
    m = [v for v in a if v == pivot]
    r = [v for v in a if v > pivot]
    a = q(l) + m + q(r)
    return a

# uses lomuto - more swaps than hoare
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
