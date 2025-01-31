https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/?envType=study-plan-v2&envId=top-sql-50

Table: Employees


id >> int
name >> varchar

id is the primary key for this table. 

Each row of this table contains the id and there name of an employee in a company

Table: EmployeeUNI

id >> int
unique id >> int


id, unique_id is the primary key with for this table. Each row of this table contains the id and the corresponding unique
id of an employee in the company.

Something off the bat, we now have two tables with one containing and int and a var char with the other containing two ints.



The ask

- A solution to show the unique of each user
	if 
		unique id not find
			print "null"

any order is fine


Input: 
Employees table:
+----+----------+
| id | name     |
+----+----------+
| 1  | Alice    |
| 7  | Bob      |
| 11 | Meir     |
| 90 | Winston  |
| 3  | Jonathan |
+----+----------+
EmployeeUNI table:
+----+-----------+
| id | unique_id |
+----+-----------+
| 3  | 1         |
| 11 | 2         |
| 90 | 3         |
+----+-----------+
Output: 
+-----------+----------+
| unique_id | name     |
+-----------+----------+
| null      | Alice    |
| null      | Bob      |
| 2         | Meir     |
| 3         | Winston  |
| 1         | Jonathan |
+-----------+----------+
Explanation: 
Alice and Bob do not have a unique ID, We will show null instead.
The unique ID of Meir is 2.
The unique ID of Winston is 3.
The unique ID of Jonathan is 1.


The rundown:

Off the bat, need to reference the uniqu_id which was a bit tricky to get my head around. 
Now, we are just referencing the unique id to the user and if not found then print null

A better explanation, if the id of employee tables == return the unique id


A couple of things that need to happen to fulfill this.

1. if id(Employees) = id(EmployeeUNI) 
return unique id(EmployeeUNI)

Because id is being used for both copamirson, I needed to create a unique identify for both tables
This was done with e.id and u.uniqe_id

With JOIN we are able to create a table that compares the equal numbers and return he values.

After some tinkering and stack

Returned this 

SELECT u.unique_id, e.name 
FROM Employees e
JOIN EmployeeUNI u ON e.id = u.id;


Some notes, the order for unique id and name(this is for leetcode)

The join condition that is used to compare the tables if true.


2. If no unique id is found we need to return null

Asked for help here, but the solution was found in a thing called LEFT JOIN
Which when explained makes sure that all items appear even if the operand does  not state equal.

Current solution for test is here

SELECT u.unique_id, e.name  
FROM Employees e
LEFT JOIN EmployeeUNI u ON e.id = u.id;


Interesting to note, that when trying to optimize the solution. Coalesce was used by chat and some users and after some time, significanmyl
sped up computation. 

Will need to look into this more when speeding up irl prod code. 



Without COALESCE 



<img width="900" alt="image" src="https://github.com/user-attachments/assets/1469ec49-2d4f-4401-99fe-174c72f1f8d2" />




With COALESCE 


<img width="447" alt="image" src="https://github.com/user-attachments/assets/4b1df9ec-2b44-4fd3-b784-bdf48499b16f" />
