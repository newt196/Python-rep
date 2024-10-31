import numpy as np

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
