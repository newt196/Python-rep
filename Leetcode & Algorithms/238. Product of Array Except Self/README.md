**https://leetcode.com/problems/product-of-array-except-self**

Given an integer array, return an array(answer) such that (answer[i]) is equal to the product 
of all the elements of nums except nums[i]?

This explanation seems off, except for "(answer[i]) is equal to the product 
of all the elements"

This "except nums[i]?" is what throws me off.

Looking at the example it seems to clear up the ask a bit more. Probably a good idea to move away from looking at or using the examples as a base start.
Seems better to figure it out at the start. Disregard, senior programmers say the opposite.
May need a way to be more creative with more test examples.
Thinking more like a problem solver and programmer.


For right now we have 
EX: nums = [1,2,3,4]
O: [24,12,8,6]

Which doesn't make sense

EX1: nums = [-1,1,0,-3,3]
O: [0,0,9,0,0]

Almost missed the side info for the problem:
The product of any prefix9:21 AM 12/2/2024 or suffix of nums is guaranteed to fit in a 32 bit integer.
You must write and algo that runs in O(n) time and without using the division operations

Some key notes


"You must write and algo that runs in O(n)" single iterations sounds like it works here

"without using the division operations" unsure why this is important


When looking at the whole picture, I am sure how the numbers fit in the first example, but unsure how the numbers in the array fit. 


Still a bit confused, but I am this helps clarify some solution for the soon to be logic.
4*3*2*1 = 24 which is nice
3*2*1 = 6 which is nice, but doesn't really help in the index
2*1 = 2 where things break down
1 = 1  wth?

Wait
4*3 = 12
4*2 = 8 

Lets iterate again

4*3*2*1 = 24
4*3*2 = 24
4*3 = 12
4 = 4
1 = 1
1*2 = 2
1*2*3 = 6
1*2*3*4 = 24

Unsure where the 8 comes from?

Received some help, and it seems I needed to understand the prefix and suffix item. 
For prefix we need to start with i = 1, i = 2 etc.
This means that the prefex for index 1 is the first element.
For prefix 2. This is multiplications of all of the elments before index 2 meaning index 0 & 1
In the example case 
i = index btw
i = 1 | 1
i = 2 | 1 
1 = 3 | 1 * 2 = 2
i = 4 | 1 * 2 * 3 = 6

Remember this is all to calculate the prefix, which is n + 1 for the index of the array.
Meaning for the new prefix array we have
 		
		Prefix = [1,1,6,12]


Now we need to calculate the suffix for the array
Meaning the suffix just reversed. 
i = 1 | 1 
i = 2 | 4
i = 3 | 3 * 4 (note the order here)
i = 4 | 2 * 3 * 4 = 24

		Suffix = [24,12,4,1]

Was stuck on the total add for a bit, but watched [https://www.youtube.com/watch?v=RBXJvhgcWgM&ab_channel=JOYofLIFE]
to help find that the suffix and prefix are needed to calculate the total answer. 

Counter to what is said within "The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer."
that is said within the problem description.


So for the final calculation we have 
multiple the index of each suffix and prefix together to find the [ans]
The logic follows 
			   0  1 2 3 
		Suffix = [24,12,4,1]
		Prefix = [1,1,2,6]
index 0 | 24 * 1 = 24
index 1 | 12 * 1 = 12
index 2 | 4 * 2 = 8
index 3 | 6 * 1 = 6

Now that the logic has been made with the suffix and the prefix. We need to understand how to code it out...efficiently.

The visual display for the index help with understanding what needs to happen within the code block.

A couple of things need to happen.


 |   We need to or three...Apparently I am not supposed to use two arrays for the storing.   |
Need a way store or calculate the suffix and prefix together without using two arrays. 
This is tricky, because I think I see a .suff and .pref but am unsure if they are good in use? 


First used the length of the array to inialize a value called "list".
This allows us to initialize the len of nums for later use within the code logic.(Typical in most problems involving the array)
We now use a variable called "result" to finish the final result of the code logic. 1 is used used to start the logic or math 
with prefix and suffix later on. 



        list = len(nums)
        result = [1] * list 


Credit to Stack for the solution on what variables to set the initial problem to.

      prefix = 1
        for i in range(list):
            result[i] = prefix
            prefix *= nums[i]  


For Prefix, we set the variable "prefix to 1" at the start.
Remembering that the inital index does not hold value, hence the 1 and not 0. 
0 because there is an item there


now that we have the start pick with prfix, we now use a for loop to iterate over all of the array items to now find out prefx answer.

[for i in range(list)] remembering that list holds the len of the nums | index positions..
we use the result [i] also remembering that i is each element with respect to its index area.
within the do after ":".

At each index within nums, we assign and update i within the context of the prefix. 
After each loop the index is then assigned to the current prefix to result[i] due to it representing the product of all elements before [i]

			            prefix *= nums[i]  


after that we multiply the result within each [i] to get the prefix within the array to get the result


     suffix = 1
        for i in range(list - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i] 
	

For suffix, we assign the same 1 with the same logic at the start.

The for loop is a bit different though.

Credit to Stack in regards to the logic here though.

How it was explained is, although using the classic [for i in range]
We use  (list - 1, -1, -1):

this is due to the fact that we are iterating backwards
We first start at n - 1:

The loop starts at the last index of the list (n - 1), where n is the length of the list. we begin the move at the end of the array.

[stop = -1] The loop continues until it reaches an index just before -1. In practice, this means it will process index 0 (the first element in the list) as the last step, because range excludes the stop value.

[step = -1] The loop moves backward by decrementing the index by 1 after each iteration.


Since we already have the math from prefix we just need to multiply each element in result by the product of all elements after the current index.

This is done with

 		result[i] *= suffix
            	suffix *= nums[i]  ]

After completion we then return the result, asltghough print could have been used since we need to add fringe cases. 












