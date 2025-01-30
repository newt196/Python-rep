
https://leetcode.com/problems/article-views-i/?envType=study-plan-v2&envId=top-sql-50

Article Views I

TABLE: VIEWS
There is no primary key (colums with unique values) for the given tables, the table may have duplicates....(!!!!)

Each row of this table indicates thast some viewer viewed an article (written by some author) on some date.
Note that equal author_id and viewer_id indicares the same person(!!!!)

I dont like that their are duplicates and that author and viewer could be the same. 




The ASK

Find an author that has viewed his own article once

Return the table sorted by id in ascending 

Example is a bit confusing 

Example 1:

Input: 
Views table:
+------------+-----------+-----------+------------+
| article_id | author_id | viewer_id | view_date  |
+------------+-----------+-----------+------------+
| 1          | 3         | 5         | 2019-08-01 |
| 1          | 3         | 6         | 2019-08-02 |
| 2          | 7         | 7         | 2019-08-01 |
| 2          | 7         | 6         | 2019-08-02 |
| 4          | 7         | 1         | 2019-07-22 |
| 3          | 4         | 4         | 2019-07-21 |
| 3          | 4         | 4         | 2019-07-21 |
+------------+-----------+-----------+------------+
Output: 
+------+
| id   |
+------+
| 4    |
| 7    |
+------+


After some thinking, "I understand it now"

From what i get, we are just returning both the author_id and viewer_data that is == to each other.

This can be confirmed when looking at the expect output. 

4 & 7 

When looking at the table

7 in the third row is notated with viewing it own article at 2019-08-01 
In this case Author id == Viewer ID and itself 7 should be returned

Current iteration adlibbed was 

SELECT author_id FROM Views
WHERE author_id == viewer_id;
This was throwing two error

1. ID needed to be returned (in the og code, author_id is being returned) 
2. For some reason I am getting 	|
| 7  |
| 4  |
| 4  |

Where I should 

| id |
| -- |
| 4  |
| 7  |

Initially went to change the author id with RENAME, but apparently this is now allowed within leet. Plus 
I am confident this would change the name of author within the database itself and not just the result. Which wouldn't really help us here.
Found that AS can manipulate the result without changing the database itself. 


SELECT author_id AS id FROM Views

We now have the first problem eliminated. 

Quick google search allows us to eliminate the second problem.

Found DISTINCT which just prevents duplicates.

Now one third somewhat hidden problem 
We are getting 

| id |
| -- |
| 7  |
| 4  |

we need to add sorting.

Simply adding ORDER BY seems to do the trick.

We now have 

SELECT DISTINCT author_id AS id FROM Views
WHERE author_id = viewer_id
ORDER BY id;


This finished the test case and the overall submission 



 












<img width="860" alt="image" src="https://github.com/user-attachments/assets/baf7b749-8a22-4f22-a7d8-6fe1d37a2569" />
