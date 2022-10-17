class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # dutch national flag 3 way partition
        # O(n)
        #       lo_end mid_end    hi_st
        # 0.......i.......j.........k.....n
        #    <mid    mid    unsorted  >mid
        a = nums # just an alias
        n = len(nums)
        i,j,k = 0,0,n-1 # before index, holds the max elm just before pivot
        while j <= k: # loop until unsorted elms exist
            print(f"{a} i:{i} j:{j} k:{k}")
            if a[j] < pivot:
                print("<lesser")
                a[j], a[i] = a[i], a[j]
                i += 1
                j += 1
            elif a[j] > pivot:
                print(">greater")
                a[j], a[k] = a[k], a[j]
                k -= 1
            else: # a[j] == pivot
                print("equal")
                j += 1 
        print(a)
        return a
        
