**https://leetcode.com/problems/single-number/?envType=problem-list-v2&envId=array


**
Given an array, every element appears twice except for one. Find or return the 1

Needs and constraints

Linear runtime complexity O(n)

Use only content extra space. 

1 <= nums.length <= 30000 === [1] or [1,2,3,4,5....30000]
-30000 <= nums[i] <= 30000 === smallest [-30000] or [30000] largest


For a no go, that includes
- arrays
- lists
- hash tables
- recursion


Need a way to go through the array and computer the number or index that [i] = 1

After looking at the discussion, apparently something called a Bitwise operand needs to be used here.


Apparently a hash set blows this out of the water, due to duplicates being removed within the properties within a hash.

Sadly needs to be in-place. 
Following along within Neetcodes explanation

Need to perform the following


4 = 100 *** 100 that stands out
1 = 001   same 0
2 = 010  same  1
1 = 001	  same 0
2 = 010   same 1

If two bits are the same, the same are going to equal 0
if different than we can return 1 with XOR.
From my own interpretation if we combine all of the numbers, we can leave all of the 0's or the same and leave a 1 because it leaves
or returns what we need. 


Again, in my understanding, we are just retuning the odd man or number out when it comes to the bitwise or bit operation. 
The code goes as follows

result = 0
This is done to ensure that the XOR operation, any number with 0 will leave the number unchanged. 

We then loop through the array with 
	for n in nums:
for each number within the array, we will XOR the number with the result. Making it so that 
if the number appears twice, the two occurrences will cancel each other out as mentioned earlier.

In all the code is 

result = 0
for n in nums:
	result = n ^ result
return result













<img width="866" alt="image" src="https://github.com/user-attachments/assets/ae522202-abd9-49e0-8dc5-215113bdd94e" />
