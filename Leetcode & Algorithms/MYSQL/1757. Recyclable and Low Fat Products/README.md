
Moving to a few 
MYSQL problems that i thought were topical. 

*** This needs to go into the README.md ***

General practice coming from the SQL 50





https://leetcode.com/problems/recyclable-and-low-fat-products/description/?envType=study-plan-v2&envId=top-sql-50


The TABLE given is: Products

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| low_fats    | enum    |
| recyclable  | enum    |
+-------------+---------+

product_id is the primary key (column with unique values) for this table.
low_fats is an ENUM (category) of type ('Y''N') where 'Y' meanbs this product is low fat and the 'N' means it is not. 
Recycleable is an ENUM (catagory) of types ('Y''N'), where Y means the product is recycle;abl and N means it is not.

Going to break down after writing

Side note, Enum is a state of 0 or 1. Evaluation method

Seems like Given 
Product ID(unique)  tied to a int/number
low_fats tied to Enum(Y or N)
recyclable tied to ENUM(Y or N)

ASK
Asking to find a solution to find thes of products that are both low fat(Y) and recyclable(Y)
The order doesnt matter



CV

Example 1:

Input: 
Products table:
+-------------+----------+------------+
| product_id  | low_fats | recyclable |
+-------------+----------+------------+
| 0           | Y        | N          |
| 1           | Y        | Y          |
| 2           | N        | Y          |
| 3           | Y        | Y          |
| 4           | N        | N          |
+-------------+----------+------------+
Output: 
+-------------+
| product_id  |
+-------------+
| 1           |
| 3           |
+-------------+
Explanation: Only products 1 and 3 are both low fat and recyclable.

We are just dropping all product id's that have "N" within there description and retunring id's that
have all 'Y'



Solution walk through

SELECT product_id FROM Products

Need to select the product_id colums we want to evaluate from Products. 


We need to now write an expression to return all products that return YY on both colums

WHERE low_fats = 'Y' and recyclable = 'Y';








<img width="892" alt="image" src="https://github.com/user-attachments/assets/6581722c-e67f-42a2-98b1-427131adb060" />
