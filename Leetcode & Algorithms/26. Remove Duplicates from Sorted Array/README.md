**https://leetcode.com/problems/remove-duplicates-from-sorted-array**


Given an integer array (an array filled with numbers) sorted in increasing order(1234). Remove the duplicates (in place?(no new array, I think) such that each unique elemtns appears only once. The relative order of elements should be kept the same. Return the number of unique elements of nums.

Things to consider
The number of unique elements of nums to be k, to get accepted, we need the following.
Change the array such that the first (k) elements of nums contain the unique elements in the order that were present in nums initially. The remining of nums are not important as wall as the size of nums

Return (k)

Example
Input 
nums = [1,2,2]
Output
k = 2
nums = [1,2,_]
Your function should return k = 2, with the first two elements of the nums being 1 and 2. It does not matter what you leave beyond the returned k.

Constraints to consider
nums is sorts in increasing(important because we don't need to sort)

MY own explanation for the problem

We are given an array of numbers in increasing order. 
We need to do the following with logic
-Remove the duplicates plus(0)
-Sort the new array 
-return k, k meaning the unique elements given in an array. 

For right now I have created an array_length as a sudo k.
This may not work, because we need to run this function after seperating the duplicates into the new array.
This may work. 

Found https://www.geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/

        a = list(set(nums))

This seems to remove all duplicates without any fuss to my knowledge.

Just found out after a day break that (set) cannot be used because it creates a new array which violates the in-place requirement. 
Although set is nice, it could be seen as efficient but is not within the solution. Need pointers that go through the array and not create a new one.
Hence. In-Place

After some research, I found this code snippet within the site. "https://www.geeksforgeeks.org/how-to-remove-duplicate-elements-from-numpy-array/"


					
		
		
          import numpy as np
           
          #declaring original array
          org = np.array([1, 2, 3, 4, 5, 1, 2, 3, 1, 2 , 9])
           
          #displaying the original array
          print("Original Array : ")
          print(org,"\n")
           
          l = []
          for i in org:
              if i not in l:
                  l.append(i)
           
          new = np.array(l) 
           
          #displaying the new array with updated/unique elements
          print("New Array : ")
          print(new)



More specifically this part. 


      l = []
      for i in org:
          if i not in l:
              l.append(i)



Seemed like a good way to point through the array and removing any element "manually" meaning without using [set]
Found my way with the following code to do what [set] did, but manually. 




    class Solution:
        def removeDuplicates(self, nums: list[int]) -> int:
            l = []
            for i in nums:
                if i not in l:
                    l.append(i)
            return len(l)


The only thing is that it failed to copy the unique elements back into nums. The main idea here is that the amount of unique elements 
needs to be put back into the nums with logic. found the following to possibly to such 

			nums[:len(l)] = l

Using (nums[:len(l)]) allows you to replace only the beginning portion of nums with the unique elements collected in l. 
With this now implemented before the return function, we can sort the proper array and return the answer. 




