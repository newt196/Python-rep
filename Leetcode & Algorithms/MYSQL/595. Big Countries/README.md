https://leetcode.com/problems/big-countries/description/?envType=study-plan-v2&envId=top-sql-50

Big Countries

Table: Worldd

NAME is the primary key for this table.
Each row of this table gives information about the name of the country, the continent to which it belongs, its area, the pop, and the GDP.
(allot of variables to account for?)


Asking for: 

Return if it has size >= 3000000 

AND

has a pop of size >= 25000000

This one i just adlibbed from the earlier question but with beater comparisons.

Not much notes here

We have the setup which is 

SELECT name, population, area FROM World


and the logic for the comparison here
WHERE area >= 3000000 OR population >= 25000000;

Although I initially had an AND statement which returned nothing and a wrong answer. This was
my fault for not reading the question asks better.
The initial test passed, pending the submit. 

It does past. 










<img width="922" alt="image" src="https://github.com/user-attachments/assets/2dce2896-724b-4315-9ac8-9fb009b5f9bc" />
