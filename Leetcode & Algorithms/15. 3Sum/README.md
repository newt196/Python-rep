
Sorting problems 

**https://leetcode.com/problems/3sum**

This one was close, the answer code is 

	class Solution:
	    def threeSum(self, nums: List[int]) -> List[List[int]]:
	        if not (3 <= len(nums) <= 3000):
	            return None  

        for i in nums:
            if not (-100000 <= i <= 100000):
                return None
        nums.sort()  
        triplet_count = 0
        final_temp_list = []
        
        k = 0  
        
        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            s = set()
            temp_list = []
            
            temp_list.append(nums[i])
            
            curr_k = k - nums[i]
            
            for j in range(i + 1, len(nums)):
                if (curr_k - nums[j]) in s:
                    triplet_count += 1
                    
                    temp_list.append(nums[j])
                    temp_list.append(curr_k - nums[j])
                    
                    triplet = sorted(temp_list)
                    if triplet not in final_temp_list:
                        final_temp_list.append(triplet)
                    
                    temp_list.pop(2)
                    temp_list.pop(1)
                
                s.add(nums[j])
        
        return final_temp_list
        
       

I am getting a time limit exceeded on the  311 / 313. I cant put the variables, because the input is too long.


So the chat analysis(needed for CS optimization) of the breakdown is that the i am repeating the triplet validation and unoptimized nested loops. This was the scope 
of my usage of chat without giving away the answer.

Needed a way to limit the usage of loops and better handle the triplet validation.

From my understanding this could be done by using multiple pointers or better defined "def". This is due to  my current O being O(n^2) to O(n).

This is where my lack of algo practice shows, because for lower inputs i am able to case by. Altghough sadly as inputs grow my approach breaks down.
This is sadly new, because I as a rookie thought the inputs would stay low.

I have to now think about the big O when given very large inputs.

In this case, we need to remove the {if not} statement because its redundant and just adds to the complexity. 



So in this case, we needed to keep the restraint checker.

With 


        if not (3 <= len(nums) <= 3000):
            return None  

        for i in nums:
            if not (-100000 <= i <= 100000):
                return None

We removed the triplet_count, because this we needed to check for if triplet was found. This was previously needed to iterate over every triplet found. Again adding to the overall complexity of the code base.


As for the loop, we readjust the ending position of the the for loop with the following 

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

We don’t want to consider the same number as the first element of the triplet if it has already been processed which would generate duplicate triplets. If the current number is the same as the previous one, we are allowed to skip it.

We are now tasked with finding the target and the prefix for the next loop with the following.



            target = -nums[i]
            left, right = i + 1, len(nums) - 1


As said before, we need two pointers to iterate through the previously stated for loop with the len(nums)


while left < right:
                current_sum = nums[left] + nums[right]
                
                if current_sum == target:
                    result.append([nums[i], nums[left], nums[right]])

Finish writeup.


        
        





Given an integer array nums, return all the triples?  
Still in the problem we have nums[a], nums[b], and nums[c] such that the following occurs
i != b, i != c, and b != c and nums[a] + nums[b] + nums[c]

This part is confusing and am unsure what this is asking for {i != b, i != c, and b != c}

Lets look at the example

Remember we are trying to sort a given item to another solution here

I = [-1,0,1,2,-1,-4]
O = [[-1,-1,2],[-1,0,1]]????
Explneations
nums[0] + nums[1] + nums[2] = -1 + 0 + 1 = 0
nums[1] + nums[2] + nums[3] = 0 + 1 + -1 = 0
nums[0] + nums[3] + nums[4] = -1 + 2 + -1 = 0

Further explenations? The distinct triplets are [-1,0,1] and [-1,-1,2]. 
Notice that the order of the ourput and the order of the triplets do not matter
???
More questions than answers.


Example 2 gives some insight
I = [0,1,1]
O = []
Explanation: The only possible triples does not sup up to 0


So its seems a give array we three numbers need to add up to 0 to be considered a triplet

nums[i] is the index's that return a 0, answers the question to start figering out the logic.


Things to consider:

Constraints V

return none if the array is {empty} (this is important because[0,0,0] is not empty and equals to a triplet)

Easy constraints caught with the following 

	if not (3 <= len(nums) <= 3000):
            return None  

        for i in nums:
            if not (-100000 <= i <= 100000):
                return None
if not 

Something I have missed that may have been not as efficient or ewffective is just setting the i or the len.nums to the contraints.
^this note is after the rough draft. I didn't think about using len(nums) to catch the out of bounds error.
The same can be seen for the i in nums
n cannot be higher or lesser than 100000


Implementation

iterate over the array index and return if the addition = 0
unsure on how to wrap my head around implementation of the for loop that will return the triplets.

Will try to save each google search and return here.


Not going to directly save, but install searched for finding elements that equaled to 0.

Didn't really help much for vales over 0 or even solving the problem at all.

Was able top find a tutorial for finding triples if they are equal to a given k here:

'https://www.geeksforgeeks.org/python-find-all-triplets-in-a-list-with-given-sum/'


Questions to ask, why is for i in range(0, len(lst)-1): 
# Starts at 0 and stops at the len(lst)-1 in my case its
# (0, len(nums)-1):

We start at 0 and stop at 

Chat says 

len(lst)-1?
This loop ***excludes the last index (len(lst)-1) from the iteration.*** 
This is often done when:

You are comparing elements in pairs (e.g., lst[i] and lst[i+1]).
You want to avoid accessing out-of-range indices.


Currently we have 

 	triplet = 0
        result = []
        
	for i in range(0, len(nums-1)):
            s = set()
            tempt_list = []
Which after checking for the constraints above, we set the triplet value to 0 and we create an array {result}
This will be used to pass the question for later. 

For now we are using a for loop to iterate through the array and eventually math and create sets. <--not in that order.

Current 

draft 

    class Solution:
        def threeSum(self, nums: List[int]) -> List[List[int]]:
            if not (3 <= len(nums) <= 3000):
                return None  
    
            for i in nums:
                if not (-100000 <= i <= 100000):
                    return None
            
            
            triplet = 0
            result = []
            for i in range(0, len(nums-1)):
                s = set()
                temp_list = []
                temp_list.append(nums[i])
    
                current_k = k - nums[i]
                for j in range(i + 1, len(nums))
                    if(current_k - nums[j]) in s:
                        triplet += 1
    
                        temp_list.append(nums[j])
    
                        temp_list.append(current_k - nums[j])
                        result.append(tuple(temp_list))
                        temp_list.pop(2)
                        temp_list.pop(1)
                    s.add(nums[j])
                return result

ran into a slew of errors currently. will adjust and explain if it completes and answeres properly 

Adjusted the k to 0
Missing indent at some lines
missing ":" at the second for loop.

IT now runs but it returns the wrong answer.

Going line by line and fixing any logic errors.

Remembering this was the template

https://www.geeksforgeeks.org/python-find-all-triplets-in-a-list-with-given-sum/

This does not make sense for i in range(0, len(nums-1)): because subtracting 1 from a list doesn't make sense


We need to change to for loop logic to  
for i in range((start)0, (stop)len(nums) - 1):

This fixes the logic issue for substring 1 from the length of the list and not the list itself...which doesn't help us much.

This was found with a print statement and returning the result. 

We are also missing the logic to see if duplicates are found, we don't handle duplicates at all. 

We do this be adjusting if (current_k - nums[j]) in s:
with a return result outside of the loop to make sure the iterations are all processed. 

We now have the following to complete the question 

    class Solution:
        def threeSum(self, nums: List[int]) -> List[List[int]]:
            if not (3 <= len(nums) <= 3000):
                return None  
    
            for i in nums:
                if not (-100000 <= i <= 100000):
                    return None
            
    	nums.sort()  
            triplet_count = 0
            final_temp_list = []
            
            k = 0  
            
            for i in range(len(nums) - 1):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                
                s = set()
                temp_list = []
                
                temp_list.append(nums[i])
                
                current_k = k - nums[i]
                
                for j in range(i + 1, len(nums)):
                    if (current_k - nums[j]) in s:
                        triplet_count += 1
                        
                        temp_list.append(nums[j])
                        temp_list.append(current_k - nums[j])
                        
                        triplet = sorted(temp_list)
                        if triplet not in final_temp_list:
                            final_temp_list.append(triplet)
                        
                        temp_list.pop(2)
                        temp_list.pop(1)
                    
                    s.add(nums[j])
            
            return final_temp_list

this can be skipped as a editors note.

Theres like 92 steps I initially see, most likely looping through each instance of the given arra. 

I just found a tool that should help vislauze and display the steos the computer is taking to solve the problem

Provided: https://pythontutor.com/render.html#mode=display

In this case we dont have the  Class solution so I adjusted the code tro accomadte for single process. 

For this I set the nums to     [-1,0,1,2,-1,-4]
More precisely 
       

nums = [-1, 0, 1, 2, -1, -4]
result = threeSum(nums)

def is read and the program accesses threeSum

In this case nums is se to the provided array  [-1, 0, 1, 2, -1, -4] for usage.

threeSum(nums) is a function within the Global frame threeSum
technically just the def as early stated.

All preamble for the beginning item.

After all definitions have been saved.
Exceptions are ran through and checked as stated way earlier. 
Because the array...no the elements in the array do not match the condition it is skipped over.

Interesting to note that it does this for every element instead of all at once.

This is the opposite for len(nums) because the length all at once is given which is 6 which the program can automatically tell 
is between the conditions.

We now run into nums.sort which just sorts the array into -4 -1 -1 0 1 2

Side note now with [i] its now -4. Which I guess is represented in the first indes within the array.


We now have a sorted array called nums.sort and an empty array final_temp_list = []

This is interesting because we are adjusting an already created array with () more spcicfically with nums.sort()
also a new array is called with = []














