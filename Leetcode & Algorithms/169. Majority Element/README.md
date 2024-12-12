**https://leetcode.com/problems/majority-element**


This is the redo of the question, because i was getting a time limit exceeded. 
Failed on 25/42

When previously going over the question, because its been some time.

I realized the time complexity was O(N^20 because of the usage of count() within the max() function. 

This is perfect for short lists, but because the array that failed me had over 100 elements. Exceeded the complexity for the questions.

When going back over the solution, I think it would be better to go over the list once, and if a larger elements is found.
We replace that element with the higher element.


We use a for loop within the nums to iterate over the larger element that is caught.

This is seen with 	

	for nums in nums:

and if the count within the loop equates to 0: we set the candidate = num and count up.

Represented in

                  	if count == 0:
                  		candidate = num
                  		count = 1

Else if the num is equal to the candidate, do nothing.

Else decrement. 

Seen with 


            elif num == candidate:
                count += 1
            else:
                count -= 1


This should tackle only one iteration through the array. 

We now go from, a complexity of O(N^2) > O(N) 

The end product is 


            class Solution:
                def majorityElement(self, nums: List[int]) -> int:
                    candidate = None
                    count = 0
                    
                    for num in nums:
                        if count == 0:
                            candidate = num
                            count = 1
                        elif num == candidate:
                            count += 1
                        else:
                            count -= 1
                    
                    return candidate



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
 
