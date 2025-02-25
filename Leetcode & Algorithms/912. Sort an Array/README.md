Basic info on ineffeciant algo 



Notes from bubble sort algo, and translating the algo to the leetcode problem. Sadly this can only be uised on smaller datasets.

Fails at 10-21

Will override when faster algos's are better used.


Bubble sort

def bubble_sort(arr):  # Function to sort an array
    n = len(arr)       # Get the length of the array
    for i in range(n):  # Outer loop (controls number of passes)
        for j in range(0, n-i-1):  # Inner loop (compares adjacent elements)  # main engine
            if arr[j] > arr[j+1]:  # Swap if the left element is greater
                arr[j], arr[j+1] = arr[j+1], arr[j]  
            print(arr)  # Prints the array at each step
arr = [5, 3, 8, 1, 2]
bubble_sort(arr)

class Solution(object):
    def sortArray(self, nums):
        n = len(nums)       
        for i in range(n):  # Outer loop to control passes
            for j in range(0, n-i-1):  # Inner loop to compare adjacent elements
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

a. def bubble_sort(arr):  # its looking for an array/arr which we initialize with   arr = [1,2,3]
b.    n = len(arr)       # Get the length of the array
c.     for i in range(n):  # Outer loop (controls number of passes)
d.        for j in range(0, n-i-1):  # Inner loop (compares adjacent elements)  
d.            if arr[j] > arr[j+1]:  # Swap if the left element is greater
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

