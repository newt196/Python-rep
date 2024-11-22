https://leetcode.com/problems/jump-game

You are given integer array. You are initially positioned at the arrays first index(*0) and each element in the array
represents your max jump length at the position.

Return true if you can reach the last index, or false otherwise.

Given
class Solution:
    def canJump(self, nums: List[int]) -> bool:

Note the int > bool

Example 
I. nums = [2,3,1,1,4]
O: True
EX: Jump 1 step from the index 0 to 1, then 3 steps to the last index.

Example 2
I. nums = [3,2,1,0,4]
O: False
EX: You will always arrive at the index 3 no matter what. Its max jump length is 0, which makes it impossible to reach the last
index.


I am not going to lie, this is a bit of a dank description. I dont know what the ask here is. 
Needed to go to the forums to have someone explain. From what he says is 

"The question states "each element in the array represents your maximum jump length at that position."
It means if we are at a position k and nums[k] = 4, then it means we can jump forward a maximum of 4 steps from this position. It's our choice to jump 1,2,3 or 4 positions, but not more than 4.

For example
In this test case [2,3,1,4]
nums[0] = 2
It means we can jump either 1 or 2 steps

At the end, if we reached the last index or greater than that we win!

Thanks for reading, Hope this helps :) 

Kind of makes sense, instead the rule does not apply to example 1. 

Slowly starting to get it, and will adjust as new info comes in. Seems that we use each number and move a (i) amount of times to try and reach the last index. 

In this example 1's case, we have [2,3,1,1,4] starting at index 0 and we have a max of two moves. 
After taking two moves we move to index 2 meaning we now have 1 move because we are are index 2 and number 1. 
We now have 1 move at index 2 and we move to index 3. 
We now move to index 4 because we are given 1 more move to complete the game at number 4 or index 4.

Index 4 is going to be the key here, but we need to note that in other cases this could be mutable.



**Important**
We need a function to check for cases of 0 stopping us from achieving the end of the array (which is the goal)


Thought process

We need math to add the value to the associated index(starting at 0).
Checks for if the array starts at 0, because then we wont be able to play. 

We need to have math that checks for if the "value" is not able to move the index to the end. The associated value should 
should take that number and proceed. 
We should add the logic

"if index_value == 0" 
skip value

or something of that nature

Again if the associated index lands on a 0 then we need to try and skip that 0 or the game ends.

May need to find the max number of indexes within the list first. 

started with 

        for i in nums:
            return nums
         
but this seems to be redundant, because the array has already been created.
Instead I am going to focus on keeping track of the element or value within the given array. 

Going to start with 


 element = 0

which should keep track of the elements that is further in the array. 

we then experiment with for i in range which helps us keep track of the len of the given array

this is done with 

        for i in range(len(nums)):

we then us a for loop to return false if the element cannot be reached.
This is done with the following 

        for i in range(len(nums)):
            if i > element:
                return False

our first catch for if the element jump cannot be reached.

Once we are past the 0 check we can proceed with adding and checking for if the value can reach the end of the array.

This is done with. 

      element = max(element, i + nums[i]) 

Update element to the maximum of its current value and the farthest index reachable from index i which is i + nums[i]


We then have another check for if we can reach or exceed the last index with >=. More spsifically with the following 



		if element >= len(nums) - 1:
                return True 
this checks for if the added elements is greater or equal to the len of the nums.


 










        
