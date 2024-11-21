**https://leetcode.com/problems/majority-element**



Given an array of size N, return the majority elements.
The majority elements is the element that appears more then ⌊n / 2⌋ times.(I dont know what this means(⌊n / 2⌋))
You may assume that the majority of elemetns always exists in the array. 

Example
nums = [3,2,3]
Output = 3

Example 2
nums  = [2,2,1,1,1,2,2]
Output = 2

My explanation
Seems like they want the element that shows up the most amount of time to be returned. 
For example 1, 3 shows up 1 more time then 2. 
For example 1, 2 shows up 1 more time than 1. 

Found (max) that may be the key to returning the highest element within an array. This was found within 

https://stackoverflow.com/questions/6987285/find-the-item-with-maximum-occurrences-in-a-list

Has some issues with the return, but in all the answer code checks out.

      class Solution:
          def majorityElement(self, nums: List[int]) -> int:
              l = max(nums,key=nums.count)
              return l

My only item with this, is that when plugging into chatgpt to analyze the code. It returns that the code is widely inefficient. 
Due to the fact that it is inefficient with larger data sets. Although until they add larger arrays. We are fine here.

Will optimize later when i come back to the question. 
 
