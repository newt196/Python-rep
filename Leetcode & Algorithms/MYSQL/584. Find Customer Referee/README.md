
https://leetcode.com/problems/find-customer-referee/description/?envType=study-plan-v2&envId=top-sql-50

Find Customer Referee

In SQL, id is the primary key column for the this table(Customer)
Each row of this table indicates the id of a customer, their name, and the if of the customer who referred the,.

The ask:
Find customers who were not referred by the customer with "id = 2"
Return the result in any order

The example from CV goes as follows

Example 1:

Input: 
Customer table:
+----+------+------------+
| id | name | referee_id |
+----+------+------------+
| 1  | Will | null       |
| 2  | Jane | null       |
| 3  | Alex | 2          |
| 4  | Bill | null       |
| 5  | Zack | 1          |
| 6  | Mark | 2          |
+----+------+------------+
Output: 
+------+
| name |
+------+
| Will |
| Jane |
| Bill |
| Zack |
+------+


My own breakdown

Anything with a referee_id = 2 should be dropped
The name that does not have 2 should be returned.

Behind in notes, but started with the id

Select id FROM Customer

I don't think this is a good solution, especially when looking at the expected output. We are looking for names, not id's.

Switched over to the following 


Select name FROM Customer


Choose to exclude the value 2, with the following 

WHERE referee_id NOT IN (2);


Sadly this only return Zack which tells me the condition for "NULL" is not being determined.

Implemented the following "IS NULL" to account for this discrepancy. After some trial and syntax error and fixes we have.
SELECT name FROM Customer
WHERE referee_id NOT IN (2) OR referee_id IS NULL;

This at least passes our first test case. 


This passes the problems 19/19 which is nice. 










<img width="925" alt="image" src="https://github.com/user-attachments/assets/1659644f-6046-49ef-b0a8-bf4af50841e9" />
