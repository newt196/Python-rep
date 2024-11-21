
**https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii**


Given an integer array sorted in increasing order, remove some duplicates IN-PLACE since in each unique element appears at most twice. The 
relative order of the elements should be kept the same.

You must have the result be placed in the first part of the array NUMS. More formally, if there a K elements after removing the duplicates, then the first K elements of NUMS should hold the final result. 

EXample
nums = [1,1,1,2,2,3]  111=3  22=2 3=1
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

New notes and explanation.

From my understanding, this is very important. """The relative order of the elements should be kept the same."""
Like Remove Duplicates from Sorted Array we need to return the new array, but with at least 2 duplicates. 
In the first example we have [1,1,1,2,2,3] we need to return [1,1,2,2,3] hence the 5 elements.
This is because we need to return two 1's instead of 1 1 or 3 1's. For two we need to return two 2's and not 1 2. For three we are good here because there is just one 3 within the array. To reiterate that length of the new array is 5.

Keeping the old solution from the previous question

      class Solution:
          def removeDuplicates(self, nums: list[int]) -> int:
              l = []
              for i in nums:
                  if i not in l:
                      l.append(i)
              nums[:len(l)] = l 
              return len(l)  

But we need to account for the length of an array requiring more than 1 element within the new or I think old array. 
Unsure if we should start from the first pointer in 


        for i in nums:

or use logic right after  


        nums[:len(l)] = l 

Actually, we need to remove         

	nums[:len(l)] = l 
Adjusted the code around the main logic which just counted the elements with 


		 if l.count(i)

and it the occurrences over 2 which is the constraint they are thrown out if the element is over 2. This is done with 

		 if l.count(i) < 2:

We then return 

		 nums[:len(l)] = l  

to modify the elements within the new array letting us return the answer. All in all we return the following


      
      class Solution:
          def removeDuplicates(self, nums: list[int]) -> int:
              l = []
              for i in nums:
                  if l.count(i) < 2:
                      l.append(i)
              nums[:len(l)] = l 
              return len(l)  


The only thing adjusted was the l.count within the (i) < 2 which helps maintain the amount of elements that are
returned within the new (in-place) array.


