Initial problem:

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of them 
nodes contain a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Standout points or "ask":
-two non-empty (we don’t need to worry about creating numbers for the array, they are already given

-linked lists: It mainly allows efficient insertion and deletion operations compared to arrays. 
Like arrays, it is also used to implement other data structures like stack, queue and deque. 


-stored in reverse order

Final product 
-Add the two numbers and return the sum as a linked list.

Input: l1 = [2,4,3], l2 = [5,6,4]
l1 is set to [2,4,3]
l2 is set to [5,6,4]

We need a way to reverse the array and store them in memory for later


Output: [7,0,8]
Explanation: 
Elements are reverses and combined within a single number and then added.
342
465
*need a way to reverse the array and store as a single entity within python*


342+465 *Need a way to join or add the new entity or array for the answer*  
Answer = 807

Side note

*Seems ez to add elements together and just reverse the answer*
*checks out*

What I am currently working with after some Stack overflow research 

import numpy as np

def addTwoNumbers():
    l1 = np.array([2, 4, 3])
    l2 = np.array([5, 6, 4])
    result = int(''.join(str(i) for i in l1))
    return result

result = addTwoNumbers()
print(result)
243

Currently adds the l1 = np.array([2, 4, 3]) array into 243

*Missing*
- doing the same add with l2
- reversing the newly created elements
- adding the newly reversed elements 

So found logic to reverse numbers on stack overflow that reverses the number silly first.,
    while number > 0:  
        digit = number % 10  
        reversed_number = reversed_number * 10 + digit  
        number //= 10 
Once done I needed to store and run the entity within Sally. The definition I set for the problem within the program.
For some reason running two instances took a bit of time to set where it now runs two instances for l1 and l2 or silly and sally 


The result is import numpy as np

def addTwoNumbers():
    l1 = np.array([9,9,9,9,9,9,9])
    l2 = np.array([9,9,9,9])
    silly = int(''.join(str(i) for i in l1))
    sally = int(''.join(str(i) for i in l2))
    return silly, sally  

silly, sally = addTwoNumbers()
print(silly)
print(sally)

def reverse(number):
    original_number = number  
    reversed_number = 0  
    while number > 0:  
        digit = number % 10  
        reversed_number = reversed_number * 10 + digit  
        number //= 10   
    return original_number, reversed_number  

_, reversed_silly = reverse(silly)
_, reversed_sally = reverse(sally)



total_reversed = reversed_silly + reversed_sally
print(total_reversed)

Needed to run a decent amount of print statements to check my work and return results of what the program was doing and processing. 


