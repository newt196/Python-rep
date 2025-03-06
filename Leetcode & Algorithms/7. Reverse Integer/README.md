**https://leetcode.com/problems/reverse-integer/**




<img width="445" alt="image" src="https://github.com/user-attachments/assets/d0db7805-a60b-4a08-b1e2-db2e363795e1" />



https://leetcode.com/problems/reverse-integer/description/

Going to see if my initial reverse integer solution is working for all test cases.

IF: work
	then explain
else: no work
	then work it out and explain

Current solution that passes all 3 test cases.

Going to submit for wider acceptance now

class Solution:
    def reverse(self, x: int) -> int:
        r = 0
        n = abs(x)  

        while n > 0:
            r = r * 10 + n % 10
            n //= 10
        r = r if x > 0 else -r
        if r < -2**31 or r > 2**31 - 1:
            return 0  
        return r


solution = Solution()


It does pass which is nice.

r = 0
n = abs(x)

The solution needs to be in place hence we are starting out by initializing variables.

r = 0 # the typical start place for a solution that can go to - to +

n = abs(x)  # Work with the absolute value of x to simplify the reversal process.
            # Without abs(x), handling negatives would be more complex.
            # After reversing, we restore the sign based on the original x.

in all we have an example of x = -321(negative for abs(x))

we start with 
r = 0
n = abs(-321) # numbers ingested correctly to be able to manipulate later
if we return n = abs(x)
we get 321 # makes adding negative later much easier

A breakdown of the logic is a while loop that starts with n being less than 0

while n > 0: # abs(x) is plugged in in case x is a negative integer
    r = r * 10 + n % 10 # runs to reverse the number
    n //= 10


n % 10 extracts the last digit of n.
r * 10 + (n % 10) appends this digit to r (shifting previously stored digits left).
n //= 10 removes the last digit from n, also This // operator divides the first number by the second number and rounds the result down to the nearest integer 



Our 123 example:  123

r = 0, n = 123

First iteration r = 0 * 10 + 3 = 3
n = 123 // 10 = 12

Second iteration: r = 3 * 10 + 2 = 32
n = 12 // 10 = 1

Third iteration: r = 32 * 10 + 1 = 321
n = 1 // 10 = 0
Loop ends n = 0 | r = 321.
In our case we use the following to reverse 


After all of this is done, checks are done and adding the negative are added or nothing happens with 

        r = r if x > 0 else -r

r = r 	      # means what it means, most likely x was 0 or x was above that
x > 0 else -r # we go back to x and the final state of r if x is less than 0 or a negative



        if r < -2**31 or r > 2**31 - 1
		return 0
constraints here, no need to proceed more

also notate
else -r        # is used to add the negative back after the final while is done


Order of operation 
%
*
+

I want to walk through the loop one more time within a negative x
while n > 0:
r = r * 10 + n & 10
n //= 10

Lets make x = -21

So for the loop 
r = 0 * 10 + 21 % 10
21 % 10 = 1
0 * 10 = 0
0 + 1 = 1

r = 1

n //= 10
21  //= 10 = 2

1st 
r = 1
n = 2

Now we can run again 

1 * 10 + 2 % 10
2 % 10 = 2
1 * 10 = 10

10 + 2 = 12
r = 12

n 2 //= 10

0

End of loop we have 12

because the x was less than 0 we add -r
making it -12















<img width="627" alt="image" src="https://github.com/user-attachments/assets/9afcf579-8d0a-4fa9-8216-b873a3c6f9a2">



<img width="625" alt="image" src="https://github.com/user-attachments/assets/214eb7db-a44c-42c9-bfd5-6278316cbca6">



**Old notes**



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






