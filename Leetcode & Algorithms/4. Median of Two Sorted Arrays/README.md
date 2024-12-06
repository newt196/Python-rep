**https://leetcode.com/problems/median-of-two-sorted-arrays/**


Revisiting a hard question,

Essentially given two float arrays. We need to return the median of the two arrays in integer form.

No need to return the two examples because its pretty straightforward.

We need to first merge and then sort the [floated]arrays.

This can be done with the {sorted} function

Starting with 

		sort = sorted(nums1 + nums2)

This does the following nice things for us

:Adds the two arrays together
:After combination, they are added by degree of number


This does almost half the job for us.

We now need to do the following


:Return the length of the int | used for the middle array

:Divide the length by the addition of all entities within the new int array.

:convert the single array into


We return the length with the following

			n = len(sort)


We now want to return the median of the length with he following

		median = n // 2

this is kind of a double wammy, because we need to take into consideration if n == odd or n == even.

If odd we need to take the middle n and return the float.

    if n % 2 == 1:
                return float(sort[median])

If we are even we need to a bit more math to find the solution for the middle portion

This is done with the following



            return (sort[median - 1] + sort[median]) / 2



Which is broken down with the following

Instead of just retuning the middle element if off, we need to return the average of the median element of the two items within 
the merged array

So if [1,2,3,4] We need to find the average of [2,3]

Which in this case we need to return a float because returning 2 and 3 will not settle it.

In this case we sort the median - 1 and add the sorted medium

Returning the now average of the middle 2 and 3 if we are going odd. 

In all we have 




    class Solution:
        def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
            sort = sorted(nums1 + nums2)
            
    
            
            n = len(sort)
            median = n // 2
    
            if n % 2 == 1:
                return float(sort[median])
            else:
                return (sort[median - 1] + sort[median]) / 2




 




 

