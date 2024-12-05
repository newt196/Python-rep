https://leetcode.com/problems/trapping-rain-water
 
 
 
 **Trapping Rain water**


First hard problem to note.

Extra emphasis on what is being asked here. 

Goes as follows, given {n} non-negative numbers (need checks for numbers less than 0) representing an elevation map where each bar is 1.
Compute how much water it can trap after raining

???

EX1: 
I: [0,1,0,2,1,0,3,2,1,2,1]
	3							-
	
	2				-			-				

	1		-	/	-	/	/	-	-	/	-

	0	0	-	/	-	-	/	-	-	-	-
Unsure how the 0 part is used, may need to thing of the graph instead of the given example within the text. 

O: 6

EXP: Essentially we are counting the blue section 

I get it, we are trying to return the blue or in the let is the blue section but here is the {/} section.

So I super understand it now

Logic goes as such, initially without the graph it seems that blue is returned randomely given a set of numbers.
Although you have to look at the question scenario and the graph that has been given 

Thinking about how the graph and a given bar can hold water we have to think about in the example.
Lets look at the array and its parts that we can count water to fill in.

Within [0,1,0,2,1,0,3,2,1,2,1]

The logic goes as 0 represents open air and 1 represents a bar which means we can potentially hold water following not the next number but the bnuymber after that.

This is not represented within the first 3 numbers.

Looking at [0,1,0] meaning the current array snippet is unable to hold water meaning

0 no bar | 1 a bar | 0 meaning no water can be filled within the gap.

Lets look at another snippet of the array where the water would fill in this case.

Using[2,1,0,2]
This is a perfect scenario where we have a two walls that is two high and a well that is 0 deep.

In this case we start with 2 and end with 2.(Meaning we need to have checks for numbers that are greater than 0 and greater than 0 at the end and count the negative space filled. (Will explain further in the future)

Another space that holds water is [2,1,2]
Because the wall starts at 2 and ends with 2, but the well is only 1 deep.

So the initial logic sounds like we need to check for numbers that are greater than 0 and access the numbers not only right after, but the numbers within that right after. Unsure on the logic yet.

Constraints: 
-check for if List is mute or None 
-check if the height is 0 or less than 0
-Check if any number is higher than 2*10^4 but we can say 1000 for now
Standouts for constraints here[height, number value in array, and height length[i]]


When looking further at the array, a possible solution is starting the pointer after any 0
Lets say 1 in this case within the Example. Moving right of the aray to the next number, if 0 do nothing, move the array agaian to 2. 
2-0-1 = 1 for the blue space. (For a bonus we can probably due this math for the whole function,
can check later)

2+1+0+1=4 for the blue space.
Oh also, if the following number is the same then we need to skip that number. The number following the numer needs to be higher or less than preceding number, but it cant be the same.

Initial logic check.
- Right pointer that first checks if the n=0 if so then skip.
- IF N > 0 then save the number
 
proceed
 
        {
         If {next N} == {past N} throw out. 
         If {next N} < {past N} throw out past N [2,3]throw out 2 because next wall is higher 
         If {next N} > {past N} add difference of the two numbers [2,1] 1 blue space for rain
        
        End of array does not count towards the rain [2-1] no return because the rain falls off
        
        } 



return Result

Good starting point to figuring out the code logic for the solution. 

I just realized there is space above the numbers that I missed when doing a real world run through of the problem.

Need to walk through the code logic again.

Second logic run through
- Right pointer that first checks if the n=0 if so then skip.
- IF N > 0 then save the number

Here is where we need to focus up, we need a way for if lets say N == 2 and down the line another number higher is within say N == 3

Then we need to assess that block of numbers and the space that water could be held within

Because 2 does to equal 3 but there is wall that will still hold water but not fill in because 3 is higher than 2.
But within that array numbers are lower than 2 and 3 to fill in the gaps. 
Unsure on the math and the logic to fill in this code block.

I think i get it.

      {
       If {next N} == {past N} throw out. 
       If {current N} > {next N} Current - Next
      }
      {
       If {current N} < {next N} throw out {current N} hold {next N}
      }
      }

The logic checks out when running an irl example.

Current contraints

			if not height:

				return 0 


Going to throw out any elements within the array start with 0 
Going to do this with the following

Kind of confused with the code, I thought List was the array where height is actually the array :)

Should have payed attention in 

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]

Need to first go about checking and removing if the first array is 0 
this is done  with 


			 if len(height) > 0 and height[0] == 0:
            			height = height[1:]

This successfully removes the first index if it contains a 0. Which now that I think about it doesn't 
really make sense for real world.

But in this case it doesn't count with this example. 
Proceeding as such
**
For the future, will need to process that empty space left by a number higher than the end as [mute]
**

^^^This was done automatically with he removal of 0, although we need to rethink this approach
Instead of removing 0 what is the second index is lower than the first index.

[1,2]
In this case index 0 and 1. Index 0 does not count towards the math.

Need to start the math instead of directly removing the first and last index or maybe that is the approach...confusoing here

I dont like this approach with 


        if len(height) > 0 and height[-1] == 0:
            height = height[:-1]  
            print(height)

This just makes it so that we still have to worry about the end first and last index and its return later on

Dropping this approach for now.

Received some help with this approach which just iterates the array in a singular fasion

First in the example will adjust the def to just represent the height

As usual we set 

		n = len(height)

This is done to avoid the null that was given when just using the height directly with itself.
Also for simplicity sake we can just type n for the array instead of array of len of the height.


So misinterpreted the minimum with 0, should be 3 because we cannot trap water if N is fewer than 3.

The initial check has been moved to



		        if n < 3:  
           		 return 0

We currently have the following that starts the solution out 



      class Solution:
          def trap(self, height: List[int]) -> int:
              n = len(height)
              if n < 3:  
                  return 0

We now need a way to calculate the max height between the height of the bars from start to end.

Mentioned earlier in the .txt

We first iterate over the list with the following 

To reiterative if not already said, we will be using two pointers to calculate the number of spaces needed for blue

		

This is done with starting at index 1 with 



		results = 0
		for i in range(1, n-1):


We then calculate the max height left of the index with 


            l_max = max(height[:i])

and the right index witrh 




            r_max = max(height[i + 1:])



Once the left and right max is calculates w then run those within the height until the result is returned

The math to calculate the difference is as follows 

			        results += max(0, min(l_max, r_max) - height[i])


In all we have 

from typing import List

    class Solution:
        def trap(self, height: List[int]) -> int:
            n = len(height)
            if n < 3:  
                return 0
        results = 0
        for i in range(1, n - 1):
            l_max = max(height[:i])

            r_max = max(height[i + 1:])

            results += max(0, min(l_max, r_max) - height[i])

        return results















