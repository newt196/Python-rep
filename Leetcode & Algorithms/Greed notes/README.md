Notes on greedy algo

Starts with 
1. Start with initial state of the problem, begin making choices (optimal choices)
2. Evaluate all possible choices you can make from the current state. 
3. Choose the option that seems best, regardless of the future consideration.
4. Move to the new state, this becomes the new starting point for the iteration.
5. Repeat steps 2-4 until the goal has ended.

Not much sense when explained, but an example has been provided. 
EX:
You have a set of coins with values [1,2,5,10] and you need to give minimum number of coins for the number 39.

Logic breakdown:
1. Start with the largest coin that is less than the value or equal to the amount to be changed. 
- in this case 10 is the highest value that is close and less than 39.
2. Subtract the largest coin value from the amount to be changed, adding the coin to the solution.
- 39 - 10 = 29 || Adding one 10 coin to the solution.
^^^Now Repeat Stes 1 and 2 untiol the amount to be changed becomes 0.

Just for this case I am going to do the equations by hand.
In this case we have:
39 - 10 = 29 
29 - 10 = 19
19 - 10 = 9
9 - 5 = 4
4 - 2 = 2 
2 - 2 = 0
[10, 10, 10, 5, 5, 2]
3 10 coins used used || 2 5 coins used || 2 2 coins used
Some notes here
I thought we could only use a few coins <<< this is wrong. 
We can use as many coins to get to the solution

This is the greedy representation of the algo hence going from the highest value to the lowest.

In regards to the code representation of how to solve this we have the following. 



$$$$ Remember the goal is to figure out the minimum number of coins needed here $$$$


# Python Program to find the minimum number of coins
# to construct a given amount using greedy approach

        def minCoins(coins, amount):
            n = len(coins) # in this example the current len of coins is 4
            coins.sort() sorts the given [5, 2, 10, 1]
            res = 0
        
            # Start from the coin with highest denomination
            for i in range(n - 1, -1, -1):
                if amount >= coins[i]:
                  
                    # Find the maximum number of ith coin we can use
                    cnt = amount // coins[i]
        
                    # Add the count to result
                    res += cnt
        
                    # Subtract the corresponding amount from the total amount
                    amount -= cnt * coins[i]
        
                # Break if there is no amount left
                if amount == 0:
                    break
            return res
        
        if __name__ == "__main__":
            coins = [5, 2, 10, 1]
            amount = 39
        
            print(minCoins(coins, amount))

Not going to cover inital setup, but comments are in the ....comments

For now lets cover the notes provided.

As early mentioned we need to start from the higher value item

for i in range(n - 1 , -1, -1)

For the start, step, stop
Start
n-1 || n = 4 > 4 - 1 >> Starts at the end as we said [[0]1, [1]2, [2]5, [3]10]
^^^for more info after .sort is used, we know the last element is the highest value item

Step

-1 is used because we are going backwards

Stop

-1 > Stops when i = -1 (excluded)




Proceeding


          for i in range(n - 1 , -1, -1)
            if amount >= coins[i]:

the if statement checks if the current value, in this case 10 can be used to make change
If the value is greater, skip
if its less than we use it as many time until as possible.

thinking about this in the earlier case
if 39 >= coins[10];
39 >= 10 
proceed to

cnt = amount // coins[i]

cnt is used to get the abs number of the division 

In this case 39 // 10 
3.9 > .9 is dropped because of // 
We now have 3 
This means we can use three 10-value coins.


Adding that number to cnt with 

		res += cnt  
		amount -= cnt * coint[i]
For this case 
          
          
          
          res = 0 + 3 = 3

Now having amount with 39 - (3 * 10) = 9

Now we have 9 leftover which is still less than 39

Second iteration is 39 >= 9 

Same thing 
        
        amount = 9
        cnt = 9 // 5 = 1
        res = 3 + 1 = 4
        
        amount = 9 - (1 × 5) = 4


This is done until we have 0 hence the

        if amount == 0:
            break 

This stops the operation and moves to the return statement on res

Returning the amount of coins needed for amount. 


Huge takeaway is the way the we take the highest value item and use it to reduce until a solution is found.

Have to be careful about 

	    cnt = amount // coins[i]

            res += cnt

            amount -= cnt * coins[i]


This is where the greedy part of the algo comes into play. Keeping the remainder and using it o find what is possible within 
the problem. 
