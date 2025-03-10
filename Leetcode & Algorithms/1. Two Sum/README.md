https://leetcode.com/problems/two-sum/?envType=problem-list-v2&envId=array

look into hash map for second solution.

1. Two Sum 


Given an array of integer[nums] and integer[target], return the indices of the two numbers such that they addd up to the target

Something to consider:
- assume each input would have exactly one solution
- cant use the same element twice

2 <= nums.length <= 10000
-1000000000  <= nums[i] <= 1000000000
-1000000000 <= target <= 1000000000

Can you come up with an algorithm that is less than O(n2) time complexity?


Notes and considerations
We need to return the index and not the numbers that add to the target.





<img width="880" alt="image" src="https://github.com/user-attachments/assets/4f6a0a2b-0f15-4c89-9f75-052711ac9834" />


Two pointer direction

first pass
	for i in range(len(nums)): # first loop 

this iterates over each element starting at index 0 up to the last element
Visual representation 

nums = [2, 7, 11, 15]

# whats called a outer loop 
for i in range(len(nums)):
    print(f"Outer loop -> i: {i}, nums[i]: {nums[i]}")


Outer loop -> i: 0, nums[i]: 2
Outer loop -> i: 1, nums[i]: 7
Outer loop -> i: 2, nums[i]: 11
Outer loop -> i: 3, nums[i]: 15

the inner loop goes as the following 

		for j in range(i + 1, len(nums)):  
starts at 1 to avoid duplicates and pair checks

When combined the visual rep

nums = [2, 7, 11, 15]

for i in range(len(nums)):         # outer loop
    for j in range(i + 1, len(nums)):  # inner loop
        print(f"Checking pair: nums[{i}] = {nums[i]} + nums[{j}] = {nums[j]}")


Checking pair: nums[0] = 2 + nums[1] = 7
Checking pair: nums[0] = 2 + nums[2] = 11
Checking pair: nums[0] = 2 + nums[3] = 15
Checking pair: nums[1] = 7 + nums[2] = 11
Checking pair: nums[1] = 7 + nums[3] = 15
Checking pair: nums[2] = 11 + nums[3] = 15

for the math, logic or pair check wee have 

            if nums[i] + nums[j] == target:
essentially meaning that upon each iteration and loop we are checking whether nums for i and j add to the target.



class Solution(object):
  def twoSum(self, nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)): # if this was the same, we would possibly run into duplicates
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

The sad thing about this s the O(n^2) because for every loop with i we have to loop through j. Super
inefficient, but LC does take the slow implementation. 

Hash implementation 


Possibly using a for n in index and if number at index = target. return

Avoiding hash map, though about using two loops to first sort the original array and then run another 
loop to find pairs that add to the target.
Greatfully, I have used this solution before and can see that is widely inefficient with a O(n^2) even
implementing the solution. Best to avoid nested loops for larger inputs when checking the contraints. A max of 10000 
elemtns provided within an array.

Going to try to run through a one pass solution for a O(n) because it only allows one pass.
First creating a dictionary with the following 
		map = {}

This will also use to store the numbers or index used to find throughout the solution. This can be done 
with enumerate and the following.
- https://www.geeksforgeeks.org/enumerate-in-python/

		for i, num in enumerate(nums): #enumerate provides both the index and the number at the index.
 		  element = targert - num	


using the following to check if the element is already provided within map.
This is done with 
	if element in map:
	  return [map[element], i]

after finding the pair we add the current number to {}




<img width="878" alt="image" src="https://github.com/user-attachments/assets/5383693b-fa0e-437b-b136-a92907e0438e" />



		



  

