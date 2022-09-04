# https://leetcode.com/problems/sort-an-array/discuss/276916/Python-bubble-insertion-selection-quick-merge-heap

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # self.quickSort(nums)
        # self.mergeSort(nums)
        # self.bubbleSort(nums)
        # self.insertionSort(nums)
		# self.selectionSort(nums)
        self.heapSort(nums)
        return nums
    
	# @bubbleSort, TLE
    def bubbleSort(self, nums):
        n = len(nums)
        for i in range(n):
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    
	# @insertionSort, TLE
    def insertionSort(self, nums): 
        for i in range(1, len(nums)): 
            key = nums[i]
            j = i-1
            while j >= 0 and key < nums[j] : 
                    nums[j + 1] = nums[j] 
                    j -= 1
            nums[j + 1] = key
		
	# @selectionSort, TLE
	def selectionSort(self, nums):
		for i in range(len(nums)):
			_min = min(nums[i:])
			min_index = nums[i:].index(_min)
			nums[i + min_index] = nums[i]
			nums[i] = _min
		return nums
    
	# @quickSort
	# https://www.educative.io/answers/how-to-implement-quicksort-in-python
    def quickSort(self, a):
        n = len(a)
        if n < 2: return a
        lwi = 0 # left wall index that tracks all elm < pivot
        for i in range(1, n): # partition the arr on pivot a[0]
            if a[i] <= a[0]:  # by looking for elms < pivot
                lwi += 1      
                a[i], a[lwi] = a[lwi], a[i] # swap a[lwi] <> a[i]
        a[0], a[lwi] = a[lwi], a[0]
        l = self.quickSort(a[:lwi]) # Sorts the n to the left of pivot
        r = self.quickSort(a[lwi+1:]) # Sorts the n to the right of pivot
        a = l + [a[lwi]] + r # Merges everything together
        return a
     
	# @mergeSort
    def mergeSort(self, nums): 
        if len(nums) > 1: 
            mid = len(nums)//2
            L = nums[:mid] 
            R = nums[mid:] 

            self.mergeSort(L)
            self.mergeSort(R)

            i = j = k = 0

            while i < len(L) and j < len(R): 
                if L[i] < R[j]: 
                    nums[k] = L[i] 
                    i+=1
                else: 
                    nums[k] = R[j] 
                    j+=1
                k+=1
 
            while i < len(L): 
                nums[k] = L[i] 
                i+=1
                k+=1

            while j < len(R): 
                nums[k] = R[j] 
                j+=1
                k+=1
   
   # @heapSort
    def heapSort(self, nums):
        def heapify(nums, n, i): 
            l = 2 * i + 1
            r = 2 * i + 2
			
            largest = i
            if l < n and nums[largest] < nums[l]: 
                largest = l 

            if r < n and nums[largest] < nums[r]: 
                largest = r 

            if largest != i: 
                nums[i], nums[largest] = nums[largest], nums[i]
                
                heapify(nums, n, largest)
                
        n = len(nums) 

        for i in range(n//2+1)[::-1]: 
            heapify(nums, n, i) 

        for i in range(n)[::-1]: 
            nums[i], nums[0] = nums[0], nums[i]
            heapify(nums, i, 0) 
