
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

**Revised Part 2**


https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

Given an integer array nums sorted, remove some duplicates in place ( l = [] ) such that each unique elements appears AT MOST TWICE. The relative elements should be kept the same ( mbasic for loop, watch duplicates though)

Since it is impossible to change the lengths, you must instead have the result be placed in the first path (array created = [] ) Return k after placing the final result in the first k slots of nums

Somethings to note
- Return k after placing the final result in the first k slots of nums???

Constraints
-nums.lenthg at least 1 length. no greater length then 3*10^4 == 30000 (This does affected computation, we could have a scenario where the number of elements 
is at 30,000 at the most or the worst case scenario)
(Actually, because this is sorted already, we don't really have to worry about going through each line and sorting it ourself) 
Essentially one run through the given list.
-Larges numbers is within the range - & + 10000. (This does not affect computation)

Examples 
I nums = [1,1,1,2,2,3]
O 5, nums = [1,1,2,2,3,_]
In this example i see it as within the given array we have. 3 ones, 2 twos, and 1 three. 
Looking at the initial problem, we need to take the first two elements of the given individual number. 
In this case should do the following
1,1,1 > ( -1 happens(too many 1's ) == 2 
2,2 > (nothing happens) == 2
3 > (nothing happens) == 1 which is less than 2, but it doesn't matter

This only tests how we can slice elements that pose or hold more than 2.
So if we have 5 1's at the beginning, that is no beuno.

We need to slice out 3 1's and return that to the newly created [] 

Lets double check the solution within the second example

I = [0,0,1,1,1,1,2,3,3]
Without lookin at the output I can guess it by running it through my theory above.

We have the following
0,0 > (Thats fine) == k = 2
1,1,1,1 > (No beuno, need to slice 2 two's) 1,1 == k(now equals) = 4
2 > (nothing happens) == k = 5
3,3 (Thats fine) == k = 7

This aligns within the output for the example.

To confirm this is just a counting up to each second elements and add to k. 

Going to cover the constraints later on, not very hard to understand for now.
Refer to the constraints portion mentioned earlier.

Code


Is the first condition to proceed with the solution 

if len(nums) <= 2:
    return len(nums)



This helps us identify arrays that are less than or equal to 2. Satisfying  the first constraint. 


We now want to start placing valid items at index 2.
Peering through there discussion helped me with this one because we always have valiud numbers with this logic.

nums = [0,0] == Valid
nums = [0,1] == Valid

We want to then use rem to compare the solution to. This will be used to remove any elements within nums that is over 2. 

Hence we use 

		rem = 2 

To do so.

Interesting shortcut that helped solve the first part of the problem. 


Now that we have the first part of the setup which is 



			 


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        rem = 2  


now for the algorithm or the solution. Couldn't use an already created list from part 1. This is due to the overall complexity of "in place". Here we want the big O remaining O(1) where for larger data sets for the new list we would be running into O(n^2). 
A huge issue when first satisfying the problems constraints and the efficiencies of the problem...which are 
essentially the same thing.

Essentially the problem once a fast and efficiently solution without creating a list within the code base. 

To
satisfy this requirement we need to use pointers to go through nums

we first run a for loop that again starts at index 2 and ends at the len(nums)
We then want to run a check to see if the current element is different from the leemtns located positions behind the 2 or rem. This is done with 



if nums[i] != nums[rem - 2]:




The idea here is that no number should appear more than twice in the modified array.
By comparing the current number to nums[rem - 2], we can check if the current number is different from the number that is two positions back in the modified array.
If nums[i] != nums[rem - 2], it means that the number at nums[i] hasn’t appeared more than twice in the modified array, so we can be sure to place it at the rem position.



nums[rem] = nums[i]
rem += 1


By comparing nums[i] with nums[rem - 2], we ensure that each number appears at most twice.



<img width="848" alt="image" src="https://github.com/user-attachments/assets/924e95d0-4434-4057-9217-2fb9e79f305a" />
