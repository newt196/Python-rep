Basic info on ineffeciant algo 



Notes from bubble sort algo, and translating the algo to the leetcode problem. Sadly this can only be uised on smaller datasets.

Fails at 10-21

Will override when faster algos's are better used.


Bubble sort

def bubble_sort(arr):  
    n = len(arr)       
    for i in range(n):  
        for j in range(0, n-i-1):  
            if arr[j] > arr[j+1]:  
                arr[j], arr[j+1] = arr[j+1], arr[j]  
            print(arr)  
arr = [5, 3, 8, 1, 2]
bubble_sort(arr)

class Solution(object):
    def sortArray(self, nums):
        n = len(nums)       
        for i in range(n):  
            for j in range(0, n-i-1):  
                if nums[j] > nums[j+1]:  
                    nums[j], nums[j+1] = nums[j+1], nums[j]  # Swap if out of order
        return nums  # Return the sorted array after all passes








result 

[3, 5, 8, 1, 2]
[3, 5, 8, 1, 2]
[3, 5, 1, 8, 2]
[3, 5, 1, 2, 8]
[3, 5, 1, 2, 8]
[3, 1, 5, 2, 8]
[3, 1, 2, 5, 8]
[1, 3, 2, 5, 8]
[1, 2, 3, 5, 8]
[1, 2, 3, 5, 8]



My own interpretation on what's going on 

Bubble sort

a. def bubble_sort(arr):  
b.    n = len(arr)       
c.     for i in range(n):  
d.        for j in range(0, n-i-1): 
d.            if arr[j] > arr[j+1]:  
d.                 arr[j], arr[j+1] = arr[j+1], arr[j]  
            print(arr)  # Prints the array at each step
arr = [5, 3, 8, 1, 2]
bubble_sort(arr)

a. We need to create a def that will initzlize two things
1. bubble_sort
2. (arr) or the array that will be sorted
b. WE then need to get the len of the array with >>>> n = len(arr)
b. So instead of needing to typ out ln(arr) we can just type n
c. We have Outer loop which controls  the number of passes(just means it stops when the numbers are sorted) hence
c. we are setting the for loop to i within the range of (n)
c. More important it controls how many times we go over the list
d. Inner loop compares adjacent items with each other
d. j = 0 starts at 0 or the first ele,ents and goes until n-1i-1



Lets take more time with 

this inner loop and break it down


 for j in range(0, n-i-1):  
                if nums[j] > nums[j+1]:  
                    nums[j], nums[j+1] = nums[j+1], nums[j] 
[5, 3, 8, 1, 2]

 for j in range(0, n-i-1):  
Starts the first iteration does the following 
- starts at the first index or 0
- Stop at n-i-1 We can look at n-i-1 more in depth with the first pass
Start at 0 which means we have 5
Stop at(first pass) 5(lenn(arr)) - 0(i)  - 1


Going to use Quick Sort when trying to apply the algorithm to fix large datasets
In this case.

10-21

The data set has at least 297,000 characters. Because Bubble sort is a O(n^2) the algo was able to scape by when the sets were small to medium. The "10-21"
set was far above the limitations of bubble sort.

Going to start with the fundamental structure of quicksort. Will breakdown for memorization after the conversion has 
been done

Steps:
Pick a pivot element (commonly the last element, first element, or a random element).
Partition the array:
Move elements smaller than the pivot to the left.
Move elements greater than the pivot to the right.
Recursively apply QuickSort on the left and right subarrays.
The base case is when the array has 0 or 1 elements (already sorted).

Found in basic search, will need to convert to working order and indent within leet and nums

    def quick_sort(arr):
    	if len(arr) <= 1:
    		return arr
    	pivot = arr[len(arr) // 2]
    	left = [x for x in arr if x < pivot]
    	middle = [x for x in arr if x == pivot]
    	right = [x for x in arr if x > pivot]
    	return quick_sort(left) + middle + quick_sort(right)


As for the leetcode 1 to 1

    class Solution(object):
    	def quicksort(self, nums):
    		if len(arr) <= 1: # looks like edge case for no items in list
    			return nums
    		pivot = nums[len(nums) // 2]
    		left = [x for x in nums if x < pivot]
    		middle = [x for x in nums if x == pivot]
    		right = [x for x in nums if x > pivot]
		
		return quicksort(left) + middle + quicksort(right)

Going to implement quick sort with the following provided base.

    class Solution(object):
        def sortArray(self, nums):
            if len(nums) <= 1:
                return nums

        pivot = nums[len(nums) // 2]
        left = [x for x in nums if x < pivot]
        middle = [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]

        return self.sortArray(left) + middle + self.sortArray(right)

When running initial tests, I get a quick computation. Sadly when I 
submit the base program gets a "Memory Limit Exceeded" at 13/21. 

Looking at the array, I see even more numbers added within the array. 

Although I can see that numbers are limited to 5 spaces like "21998,13998,29874,14000,22000,14002,"
Might find a hint within the constraints and limit the code from *(anything goes on) to limit to what the program is looking for. IE the 5 numer spaced given.

        1 <= nums.length <= 5 * 104
        -5 * 104 <= nums[i] <= 5 * 104

Translation 

1 <= number of items within the array <= 50000
-50000 * <= How large or small a number in the array can be <= 50000



def sortArray(self, nums):
	if not (1 <= len(nums) <= 50000) or any(-50000 < = num <= 50000) for num in nums): # note the for loop within the nums
		return

When adding the constraints, instead of a memory issue this time around. We are getting a time limit exceeded. 


When reading the discussion, I see that quick sort was the solution for python here, but
now is unable to be passed with the current python.
Seems people are also failing on 11 or 13.

So someone noted the "constraints" at the start. With "You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible."

Its interesting to note that when looking at algorithms that do this is:

- Quicksort
- Mergesort
- HeapSort

It looks like "now" mergesort is the answer at its most basic form. For quick sort 



Insertion Sort is great for nearly sorted data and small datasets.
Bubble Sort is useful for detecting already sorted lists with minimal swaps.
Merge Sort is stable and works well for linked lists, unlike QuickSort.

