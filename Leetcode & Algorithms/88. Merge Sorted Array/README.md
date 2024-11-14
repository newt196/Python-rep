**https://leetcode.com/problems/merge-sorted-array**

https://leetcode.com/problems/merge-sorted-array

Given two integer arrays in non decreasing(no order?) We need to merge into a single array sorted in non-decreasing order 1123 | increasing 123

Seems like non decreasing is ordered but in relations to the same number. 


Something to note *The final sorted array should not be returned by the function, but instead be stored inside the array nums1.*
Seems like they want num2 to be merged with num1

num1 and num2 are int? No need to translate or convert. 
To clarify m for num1 is the number of elements that need to be merged.
n for num2 is (kind of confusing) if n=3 for num2 array we have [123456] we need to start at 0. Meaning we throw out 123 and merge 456.

things to remember, INT in an array are immutable. we need a 


			new_array = nums1 (method to merge | pointer) nums2

we need top evaluate each element in the array and not use the array but evaluate and place the elements within a new array. 


1. Inital ideas, can we just take nums 1 and declude the items not needed and add the items from nums2 into nums
sounds like we need to append items already had by nums2

2. Creating a new temp array from nums 1 and nums2...need to add elements within nums1.

We may need to consider that we should probably go backwards, since the nums1 is nondecreasing. 
Starting to create another array from nums1 <<<backwards
Start at the real value from nums1 for now, seems like we need to evaluate nums2 with the same logic.

The logic should follow, evaluate the largest number from nums1 and nums2 backwards and replace the element if larger?

    last_index = m + n - 1

Getting the index for nums1 as of now


Merge the result in the reverse order
		last_index = m + n - 1

		while m > 0 and n > 0:


This is the case that I have used to run until n and m hit 0.
Every instance of the while loop run will run until 0 is hit.


			if nums1[m-1] > nums2[n-1]:
				nums1[last] = nums1[m-1]
				m -= 1
			else:
				nums1[last] = nums2[n-1]
				n -= 1
			last -= 1
		




while n > 0:
			nums1[last] = nums2[n]
			n, last = n -1, last -1




































