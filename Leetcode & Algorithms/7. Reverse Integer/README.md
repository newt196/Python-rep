**https://leetcode.com/problems/reverse-integer/**

Given a signed integer, just meaning -1,0,1 backwards and forwards.


Initial thought process

We could use a reverse function with a if statement to check for (-) to keep it the same when reversing the number
EX  x--123
O--321

Also if 0 is added we need to disclude that from the final X.
EX for this x--120
O--21

For 0 we can run an if statement after the reverse function is implemented to disclude any instance of 0 within the final X. 

Jumping off point:https://stackoverflow.com/questions/24953303/how-to-reverse-an-int-in-python

Used the initial

def reverse_number(n):
              
                r = 0
                while n > 0:
                    r *= 10
                    r += n % 10
                    n /= 10
                return r

print(reverse_number(123))

to start my journey in figuring the problem out. This answered the question on how to reverse a given INT/x
We started in our own code with  



      class Solution:
          def reverse(self, x: int) -> int:
              r = 0
              n = abs(x)  



Setting R = 0
and implementing abs(x) or absolute value to account for positive, negative and 0's within possible X's. 
ref: https://www.w3schools.com/python/ref_func_abs.asp
This satiates the negative and 0 possibility that could be found within X.

We now have to variables we need to work with. That being 
R & N

Wanted to go with a route that builds the reversed int brick by brick. We can do this by taking the last int within 
            
          r = r * 10 + n % 10





appending the last digit to n.
Doing this until there are no more digits left.
This actually satiated two EX. Being 1 and 3. Although we didn't have a case to account for negative numbers yet or numbers outside of  -2**31, 2**31.

Created an if statement that if/else statement when x is less than 0 than we append the - sign to it. Easy enough.

    
        
        r = r if x > 0 else -r

We now can use another if statement that checks if x is out of bounds within -2**31, 2**31.

        if r < -2**31 or r > 2**31 - 1:
            return 0 

We return 0 as the questions stated. 






