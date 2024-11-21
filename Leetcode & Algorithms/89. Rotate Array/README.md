**https://leetcode.com/problems/rotate-array**

Forgot to writeup the explanation before being half done...but
Given a int array, rotate the array to the right by k steps. K is non-negative

After going through some stack overflor sites and examples. Tried (deque) but couldn't get the right syntaxt for the solution. 

Went with np.array provided within https://www.delftstack.com/howto/numpy/python-numpy-shift-array/

Was given the following 

  
            array = np.array([1, 2, 3, 4, 5])
            array_new = np.roll(array, 3)
            print(array_new)


Provided within my own code example I have the following 



                  class Solution:
                      def rotate(self, nums: List[int], k: int) -> None:
                          shift = np.array(nums)
                          array_new = np.roll(shift, k)
                          print(array_new)   





Although this returns the wrong answer. 

After looking into the output further we get 
O = [5 6 7 1 2 3 4]

but we need 

O = [5,6,7,1,2,3,4]
I hate that we need to account for the commas. Super dumb. 

Coulnt phrase or get past the expected output for the following QA. 

When lookin at some solutions, it seems the solution is a bit more technical than expected.

Going to revisit upon review. 

