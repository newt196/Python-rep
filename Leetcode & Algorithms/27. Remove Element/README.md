**https://leetcode.com/problems/remove-element
**


Given an integer array and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. The return
the number of elements in nums which are not equal to val.

Consider the number of elements in nums, which are not equal to val b k, to get accepted. You need to do the following:

Change the array(nums) such that the first (k) elements of (nums) contain the elemnts which are not equal to (val). The remaining elements of (nums) are not important as well as the size of (nums)

Return (k)


Newt breakdown. 

The problem gives us an un ordered integer(numer) array and also a single integer that is set to val.

we need logic that consideres or outlines all of the instances within the given array(Consider the number of elements in nums which are
not equal to val be k) That value is set to k. This means [1,2.3] k would be equal to 3 since there are three values provided in the array.

It explicitly states that we need to return k(*Return k)


I get it 
In the example or first prblemt we are given nums = [3,2,2,3]  where val = 3

We need to first remove all instances of 3 within nums. So the final result, we'll say a new array should be new_array = [2,2] 
Since we have the new array, we need to find the number of given int within the new array or k.
In this case it is 2 because [2,2] two ints within the new_array

Some contraints and hints.
0 <= nums.length <= 100 I am guessing this is for defining limits or constraints for the values within nums.length. nums.length <> or equal to 0-100
0 <= nums[i] <= 50 nums[i] <> or equal to 0-50
0 <= val <= 100

Initial problem solving, need a way to iterate over the nums array from left to right. (unsure how to utilize the two pointers or why that is necessary.)
Just found this (*The second pointer (k only increments when a non-val element is found, indicating where to place the next non-val element.) 

First hint.

The problem statement clearly asks us to modify the array in-place and it also says that the element beyond the new length of the array can be anything. Given an element, we need to remove all the occurrences of it from the array. We don't technically need to remove that element per-say, right?

Some other notes is that we need to use two pointers to iterate over the array for the first part.

Currently working on iterating over the array, but before anything. Need a way to return k elements within the array for later usage.
Set

              val = k
                  for items in nums:
                      if k =='k':

after running 

    class Solution:
      def removeElement(self, nums: List[int], val: int) -> int:
          val = k
          for k in nums:
              if k =='k':
                  return k
              del k[nums.index(k)]
              print(nums)

I was all over the place with errors. 

To first address my first issue, val =  k meaning it was set to a letter or a non value.
This doesn't help us one bit. Checked my other solutions and it seems setting k = 0 starts the pointer correctly. Making it so that we can iterate
properly over the problem

After that I improved the for k in nums with 


		for i in range(len(nums)): 

This gives us a second pointer that gives us the range of the initial nums for comparison later.
The later is given in 

		if nums[i] != val: 

which gives if the current element is not equal to val we place the nums value at the now given [k] position


		if nums[i] != val:       
                nums[k] = nums[i]   
                k += 1

The logic provided helps iterate k and use that for the final value so we can return the amount of elements within the array with k. 

Something to note is that starting the pointer properly is a must here.
In this case we needed k as the final return and the comparison for the amount of values provided in the array.
in this case we needed to start with an inital pointm that being 0. we cant start at 1 or -1 because we need to count up from the given length of the array.
This has already been established, but the first pointer is k = 0 While the second pointer is started at for i in range(len(nums)):
           

		 if nums[i] != val:      
                nums[k] = nums[i]    
                k += 1 





