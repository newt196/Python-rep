**https://leetcode.com/problems/best-time-to-buy-and-sell-stock**



Project that revisits and fixes leetcode solutions throughout. In this case we are fixing the best time to buy sell stock.

Current code is 

	class Solution:
	    def maxProfit(self, prices: List[int]) -> int:
	        min_value = min(prices)
	        min_index = prices.index(min_value)
	        remove_prices = prices[min_index:]
	        
	        max_value = max(remove_prices)
	        max_index = remove_prices.index(max_value)
	        
	        total = max_value - min_value
	        return total

Code stops at current variable
[2,4,1]

Output is 0 
Expected is 2 here

When thinking about why the solution failed, I am a sure that it has something to do with how the code and the code logic is 
dealing with a lower number  at the end. More specially with 1 at the end. 
In this case, the 4 maximum price for profit calculation occurs before the 1 minimum price in the entire list.

We need to rethink the structure of the code to account for a min value and a min value at the last index. 


Going to go through an iterable approach with a Single Linked List and if the lowestr price is found it is calctulated between the iterations and the max profit.


We start this the same way we with the wrong answer. 
Setting 

        min_price = prices[0] 
	max_profit = 0 


to keep track of the min_price and max profit if or once found. 
prices[0] just helps us start at 0 and change the number as we singly iterate.

For the logic used in the iteration, we use a for loop that starts at the second index, that being onme. 

We need to make sure that the iteration or price check starts at index 1 because it makes more sense to keep track after holding the first number or index 0.

For...Heh the for loop, we use do the following


		for price in prices[1:]:  
            		if price < min_price:
Once the following has been done, we then update the price to the minimum price. 

Else 
		elif price - min_price > max_profit:
                	max_profit = price - min_price  


we update the max price if found. 

What we have is 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:  
            return 0

        min_price = prices[0]  
        max_profit = 0  

        for price in prices[1:]:  
            if price < min_price:
                min_price = price  
            elif price - min_price > max_profit:
                max_profit = price - min_price  

        return max_profit


A little different from 


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value = min(prices)
        min_index = prices.index(min_value)
        remove_prices = prices[min_index:]
        
        max_value = max(remove_prices)
        max_index = remove_prices.index(max_value)
        
        total = max_value - min_value
        return total


Where the first question, relies on variables and if statements. Where the second question just relies on variables.










 
        max_profit = 0 

        for price in prices:
            if price < min_price:
                min_price = price  # Update the minimum price
            elif price - min_price > max_profit:
                max_profit = price - min_price  # Update the max profit

        return max_profit






Given an array of prices where prices[i] is the price of a given stock on the Ith day.

You want to maximize the profict vy choosing a single day to buy one stock and choosing a different day in the future to sell the stock.,
Return the maximum profit you can achieve from this transaction
If you cannot achieve any profit, return 0
		
		if 0 > profit
			return 0
prices = [7,1,5,3,6,4]
Output: 5
Buy on day 2 (price = 1) and sell on day 5(price = 6), profit = 6-1=5.
Need to assign the numbers in a sequence to and make the math or logic behind it to not touch other elements in the previous sequence. 

More logic for the math is as follows. 
If we buy on day 1 or price 7 > we would sell the on price 1. 
Meaning we bought at 7 and the price shifted to 6 or 7(-1)=-6. We lost 6 dollars
If we buy on day 2 or price 1 > We would sell on day 3 or price 5
Meaning we bought at 1 and the price shifted to 5 or 1(+5)=+4 We gained 4 dollars.

This is all dependent if we want to proceed in selling in a linear fashion, which as w wallstreet better we would never do....Typically.
**Important**
What if we buy at the lowest price(which in reality we wouldn't know because time is linear in this case....But in this example we dont need to proceed linearly. We want to figure out the lowest buy time which seriously helps us figure out the lowest time to buy
**Important**

Once we have the lowest price for day[i] we can now run that lowest price to the highest number on day[i] to proceed with the biggest assured bet for the day.

This could mean having math that immediately runs through the array and checks for the lowest number in a sequence(very important) and then checks for the largest number after that lowest number. 
Also a little check when looking at the example 2. Each number or price change is constantly going down. Making it impossible for said user to make any profit. 


When going through the logic sounds like we need dont need a new array we just need a straight calculation that computers the lowest buy datae and the biggest sale date.

Something like 
if i >next i 
append i

this should leave us with the lowest i in the array
(google fu "finding the lowest variable within an array")


once the lowest number or price, the day or the index needs to be indexed. So we can drop all of the previous indexes before the lowest price.
Once the index and the lowest price are found, we need to then return the highest number from the new or previously created index. (both are complicated to pull off. 

General thoughts
So for the sake of time, its probably better to use the same index say prices[] and then check if the index is less than the indexz after the calculation has been done.
(kind of dank though)
We need to remember that we could also run through the highest number and return the largest number or return from the smallest number from the previous calculation.


Now that I think of it it would be easier to as early stated, find the lowest number and its index. 
Once done > we proceed with finding the largest number  and notating its index, because it cant be less than the index of the lowest number. 

Once done > we proceed with subtracting the lowest number from the highest number and its index. 
In this example 
We know that index 1 is the lowest price which is saved. Anything after that we drop. 
We know that the index 4 has the highest price or number after index 1 meaning its highest sell price. This means 6-1 = 5 dollars is the biggest profit within that array. 

This should get us started with coding up the solution. 


Thing to remember .remove()

First issue 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        for i in range(prices):
            print(i)
TypeError: 'list' object cannot be interpreted as an integer


Sound like i need to convert the list into an array of integers. 

Tried and this seems to be better 

        for i in prices:
            print(i)

Stdout
7
1
5
3
6
4

Found out that this output is not indexable, but with enumerate() i can.

this works 

        for i in enumerate(prices):
            print(i)

(0, 7)
(1, 1)
(2, 5)
(3, 3)
(4, 6)
(5, 4)

Got stumped on the List object throwing error with everything but enumerate, Got some help to proceed. We now have

      mi_value = min(prices) 

Already locating the min prices with the min_value
Already notating the min value with the prices.index(min_value) a smart way to notate the min value and its index. 
Also because its running in a sequence it will not race loop and fill in info it doesn't have. 

      remove_price = prices[min_index:]

All in all we have 

        class Solution:
            def maxProfit(self, prices: List[int]) -> int:
                min_value = min(prices)
                min_index = prices.index(min_value)
                remove_prices = prices[min_index:]

Which returns the lowest value and its index. Which after printing the results. 
For visual basic

[1, Index: 1]
 [1, 5, 3, 6, 4]


Now that we have the first half or maybe the 1/3 we can proceed with finding the largest number and only considering remove_prices = prices[min_index:]
this is due to the new index only containing days after the "buy" date. 


So for the max value I was able to reverse the order but for the max value. I did have to note the nax value within max_index = remove_prices.index(max_value)

We now have 

    class Solution:
      def maxProfit(self, prices: List[int]) -> int:
          min_value = min(prices)
          min_index = prices.index(min_value)
          remove_prices = prices[min_index:]
          
          max_value = max(remove_prices)
          max_index = remove_prices.index(max_value)

Which returns the lowest and highest value within the array.

2/3 of the way there. We just need mat to subtract the highest number from the lowest number



done, we now have 

    class Solution:
        def maxProfit(self, prices: List[int]) -> int:
            min_value = min(prices)
            min_index = prices.index(min_value)
            remove_prices = prices[min_index:]
            
            max_value = max(remove_prices)
            max_index = remove_prices.index(max_value)
            
            total = max_value - min_value
            return total
Which does what the first part, second and third part does. 

When running the program through chat it says the code is widely inefficient for larger data sets.

Received

Final Rating of Your Solution:
Correctness: 9/10
Handles valid inputs correctly.
Efficiency: 5/10
Not optimal for large inputs due to multiple passes and extra space.
Readability: 8/10
Clear and straightforward code.


Need to do work on using variable and data structures a little better. 
Need to stop spamming simple solution, but this is good nonetheless



















