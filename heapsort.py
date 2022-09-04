# doesnt work!
import random

def heapify(a, n, i):
  l = 2*i+1
  r = 2*i+2
  maxi = i
  if l<n and a[l] > a[maxi]: maxi = l
  if r<n and a[r] > a[maxi]: maxi = r
  if i != maxi: 
    a[i], a[maxi] = a[maxi], a[i]
    heapify(a, n, maxi)
    
def heapsort(a):
  n = len(a)
  for i in range(n//2 -1) [::-1]:
    heapify(a, n, i)
  for i in range(n)[::-1]:
    a[0], a[i] = a[i], a[0]
    heapify(a, n, 0)
   
# main
# a = random.sample(range(100), 10)
a = [4, 3, 7, 2, 9, 1, 8]
print(f"u:{a}")
heapsort(a)
print(f"s:{a}")
