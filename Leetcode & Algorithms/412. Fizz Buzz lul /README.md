**https://leetcode.com/problems/fizz-buzz/**


<img width="455" alt="image" src="https://github.com/user-attachments/assets/c23dde84-1583-446a-ae8d-d3078d74f5da">




<img width="477" alt="image" src="https://github.com/user-attachments/assets/31686f7d-3ebc-4ddb-8a8f-fffbafb66ba0">




Need a Fizz buzz rundown for logic and problem solving.

Not satisfied
*****May need to start with an if statement to check whether n is divisible by 3 or 5...or both.(need logic for that)

We need to throw an exception if the N is not divisible by any of the suggested. 
If it is we can proceed with


If N being the number provided is divisible by 3 is returned. We need to return a count where the position 2(012) or "3" returns Fizz.
EX: 3
1,2,Fizz
If 5, then return Fizz at position 2 or "3" and Buzz at position 4 or "5"

If N is divisible by both, then return fizzbuzz at position 14 or "15" besides returning Fizz and Buzz at the previously stated positions.



Initial thoughts need a way to first count N and list the items in an Array 
So 
EX: if n=3
return len(3) or something like the opposite...
Output 1,2,3
****Need logic to return the output. Going to google fu this logic here.
Used to satiate this requirement 

solution = Solution()
print(solution.fizzBuzz(15)) 

Satisfied...for now()
*****Once N prints 1,2,3 or 1,2,3,4,5 
We need logic to replace the indexed positions of 3 and 5 with Fizz or Buzz 
***Any number or instance position that is divisible by 3 or 5 needs to be replaced with Fizz or Buzz or both. 
Also position 15 needs to be replaced with fizzbuzz

started with assigning an my_array and setting the list to n+1.

Full code includes   


my_array = list(range(1, n + 1))  


Initially going to create a new def to perform the logic on the new array created listed as result.
Altghough it was seen as to tedious and uneccessary. We can create and cram the logic within the same fizzbuzz def. 

The logic goes. We first create a list with the given logic.
   
    def fizzBuzz(self, n: int) -> List[str]:
        result = [] 

Using the below to add to the array given n + 1 starting at 1. 
       
        for x in range(1, n + 1):

We now use the following if/elif statements to complete the logic for the program. 
15/5/3 using .append to add words to the positions within the loop

            if x % 15 == 0:       
                result.append("FizzBuzz")
            elif x % 3 == 0:       
                result.append("Fizz")
            elif x % 5 == 0:       
                result.append("Buzz")
 


The ending else statment is used to skip through the logic if none of the following have been made. 
           
            else:
                result.append(str(x))  






