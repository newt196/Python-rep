https://leetcode.com/problems/rising-temperature/description/?envType=study-plan-v2&envId=top-sql-50

Table: Weather

Provided example given by lc

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     | >>>unique
| recordDate    | date    | >>> not unique
| temperature   | int     | >>> not unique
+---------------+---------+

The ask is as follows:

- Need to find all dates ID with higher temps compared to its pervious dates(yesterday)




Rundown/solution

**Return**

Just seems we are returning(important) the id that contains a date where the previous date was lower

**Logic**
Evaluate id 1 with recordDate and temp. Although temp is the important part

If temp for date 2 is higher than 1
	return date 2
If temp for date 3 is the == prev
	drop row



I was a bit stumped on the solution, for could not wrap my head around why if -1 was in the temperature. My solution would fail.

I did have to look at the solution for if dates was necessary and it seems so. Insteead of comparing values, the guy wrote that its more effective to compare dates with DATEDIFF. 

This ensures that (-) is compensated for.

Also found a way to find the difference within the same table.

Found that just calling two instances of Weather with small case w makes it so that we can iterate through the table
itelse



For right now we have 

			SELECT w1.id
			FROM Weather w1, Weather w2

This makes it so that in its basic form we can resolve most of the setup with proble,

We now have the selected id and two tables for comparison.

As for the logic 

As early started we use DATEDIFF to compare the dates of the two tables created.


With the following WHERE combined with DATEDIFF we can evaluate record date which if we remember holds the 
date that can help us find the idf's needed for the resolution

With that we have the first eval at 


			WHERE DATEDIFF(w1.recordDate, w2.recordDate)

The eval is set to (=1) because we want to look at the difference of the dates by exactly one day
Thank you stack

^^This solves the first part of the eval for the dates, we then want to set an eval statement for following 
		if temp 1is > temp 2
		return yay
		temp 1 < temp 2
		drop temp 1


We pair this eval with an AND statement and end the statement with the following 

		AND w1.temperature > w2.temperature




In all we have the following 


SELECT w1.id
FROM Weather w1, Weather w2
WHERE DATEDIFF(w1.recordDate, w2.recordDate) = 1 AND w1.temperature > w2.temperature;


Some side notes when testing and just general MySQL context notes


The FROM order does not matter
but
the order for recordDate does matter because it impacts how the rows are evalauted

AND 
^ this needs to be a base go to when evaluating things that remotely sound like more than 1 item.











<img width="890" alt="image" src="https://github.com/user-attachments/assets/024ee43c-f47f-4369-b35b-9abeddfbc682" />
