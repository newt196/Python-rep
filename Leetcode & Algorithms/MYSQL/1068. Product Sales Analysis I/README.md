https://leetcode.com/problems/product-sales-analysis-i/description/?envType=study-plan-v2&envId=top-sql-50

Main Table: Sales

In this problem we have the following provided.

+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| sale_id     | int   |
| product_id  | int   |
| year        | int   |
| quantity    | int   |
| price       | int   |
+-------------+-------+

With SALES_ID and YEAR being the primary key. 
Combination of columns with unique values
Product_id is a foreign key (reference column) to Product Table
Each row of this table shows a sale on the product PRODUCT_ID in a certain year.

NOTE: 
Price is per Unit

We also have 

Table: Product  

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
+--------------+---------+

Here PRODUCT_ID is the primary.
Each of the row of this table indicates the product name of each product.

The ASK:

A solution or return to report the following
(PRODUCT_NAME, YEAR, & PRICE)

FOR EACH

(SALES)

No order is necessary. 


Current example has been provided 

Example 1:

Input: 
Sales table:
+---------+------------+------+----------+-------+
| sale_id | product_id | year | quantity | price |
+---------+------------+------+----------+-------+ 
| 1       | 100        | 2008 | 10       | 5000  |
| 2       | 100        | 2009 | 12       | 5000  |
| 7       | 200        | 2011 | 15       | 9000  |
+---------+------------+------+----------+-------+
Product table:
+------------+--------------+
| product_id | product_name |
+------------+--------------+
| 100        | Nokia        |
| 200        | Apple        |
| 300        | Samsung      |
+------------+--------------+
Output: 
+--------------+-------+-------+
| product_name | year  | price |
+--------------+-------+-------+
| Nokia        | 2008  | 5000  |
| Nokia        | 2009  | 5000  |
| Apple        | 2011  | 9000  |
+--------------+-------+-------+

Explanation: 
From sale_id = 1, we can conclude that Nokia was sold for 5000 in the year 2008.
From sale_id = 2, we can conclude that Nokia was sold for 5000 in the year 2009.
From sale_id = 7, we can conclude that Apple was sold for 9000 in the year 2011.

Problem breakdown

When lookling at the output, we can see that it is just returning the price for each company provided in the prductname within Procudt.

We need to start with Sales

and then write a solution to match the primary key for sales and product id to return the price.


Started with 

SELECT product_name, year, price
FROM Sales, Product;
 

that returns all that is necessary with adding WHERE

That is returned in the below

WHERE Sales.product_id = Product.product_id;

Thought it would be harder, but this is just simply using primary keys for two tables to find corresponding info.

I will say a good google search helped me here[https://stackoverflow.com/questions/72045619/mysql-use-primary-key-values-to-get-corresponding-values-from-another-column]









<img width="916" alt="image" src="https://github.com/user-attachments/assets/33b1e661-e94f-49e6-a1fd-f9e39f9f58f2" />
