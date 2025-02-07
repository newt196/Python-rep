
https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/description/?envType=study-plan-v2&envId=top-sql-50


We are provided tables

Table: Visits

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| visit_id    | int     |   <<<Note all int
| customer_id | int     |
+-------------+---------+

visit_id is the column with unique values for this table. This
table contains info abotuy the customers who visited the mall


Table:: Transactions
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| transaction_id | int     |
| visit_id       | int     |
| amount         | int     |
+----------------+---------+

Transaction_id is the column with unique values for this table. This
table contains info about the transactions made during the visit_id.

^^^^General info 

The ASK: 

- find the ID';s of the users who visited without making any transactions and the number of times they made these types of visits.

- Any order


Going to start without using the given example. 

Add some level of difficulty before hard questions start being added. 

Going to skip passed the setup and go straight into the logic to answer the question.


Without having the example as a shortcut to the solution we need to return the following.

Write a solution to find the IDs of the users who visited without making any transactions and the number of times they made these types of visits.


- IDs  (|customer_id | int)

- without making any transactions(| amount         | int) = assuming this is 0 | 

- number of times they made these types of visits.<<<unsure of this, maybe visit_id if repeated with customer_id


Needed to cheat a little with the example.

Looking at customer_id 54 is repeated twice


We are just returning as previously stated, how many times a user visited the mall while amount_id(for ref) remains 0


In this case we need to return and record two things.


- customer_id
- amount of times (customer_id) shows up while int=0 | count_no_trans ise used to indicate this

BTW^^^this is all under AND statement (while true if data was continuously pouring in)

Kind of tricky, i am stuck on using just Visits. Cant wrap my head around Transactions containing info that will help
solve the context problem.


I may have to set the item to null instead 0.

I have it backwards. Instead of focusing on customer_id, visit_id corresponds with both tables and is unique. 

Need to set the visit_id with the amount of time they show up as NULL

Have to be careful, though because it seems the ask is to customer_id needs to be returned, but visit_id needs to be evaluated. 

The thought process goes as follows, 

Need to select the customer_id and the cound for transaction_id when null.

This was done with 

				SELECT v.customer_id, COUNT(CASE WHEN t.transaction_id IS NULL THEN 1 END) AS count_no_trans

Which gives us the starting point for which we are to display as the problem.
also needed to lookup
"THEN 1 END"
^ this allows us to only count instances where the condition is true and returns 1


The evaluation of data goes as follows:


We are using left join again to make sure all elements are captured and using.v and .T to make sure we are capturing and 
evaluating visit_id for both tables properly.


We now have 


			FROM Visits v
			LEFT JOIN Transactions t ON v.visit_id = t.visit_id

The last little bit ensure that the customer_id count only returns id's that have 0.

Initial left this out and it returns users with 0 who have visited the store and made a purchase. 

      
      GROUP BY v.customer_id
      HAVING COUNT(CASE WHEN t.transaction_id IS NULL THEN 1 END) > 0;


In all we have the following 


      SELECT v.customer_id, COUNT(CASE WHEN t.transaction_id IS NULL THEN 1 END) AS count_no_trans
      FROM Visits v
      LEFT JOIN Transactions t ON v.visit_id = t.visit_id
      GROUP BY v.customer_id
      HAVING COUNT(CASE WHEN t.transaction_id IS NULL THEN 1 END) > 0;













<img width="919" alt="image" src="https://github.com/user-attachments/assets/382c52f0-c5d3-40d8-98d2-0a3499036fa7" />
