#!/usr/bin/env python
import random
def mergesort(a):
    n = len(a)
    if n <= 1: return

    i = j = k = 0
    m = n // 2
    l = a[:m]
    r = a[m:]
    mergesort(l)
    mergesort(r)
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            print(f"a[{k}] = l[{i}] => {l[i]}")
            a[k] = l[i]
            i += 1
        else:
            a[k] = r[j]
            j += 1
        k += 1
    while i < len(l):
        a[k] = l[i]
        i += 1
        k += 1
    while j < len(r):
        a[k] = r[j]
        j += 1
        k += 1
         
# main
# a = [20, 40, 10, 30]
# a = random.sample(range(100), 10)
a = [4,3,7,2,9,1,8]

mergesort(a)
print(f"{a}")
