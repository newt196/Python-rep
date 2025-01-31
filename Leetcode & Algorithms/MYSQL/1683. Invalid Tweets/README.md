https://leetcode.com/problems/invalid-tweets/?envType=study-plan-v2&envId=top-sql-50

Current Table: Tweets

tweet_id is the primary key(column with unique values) for this table. Content consists of characters of an American keyboard, and no other special characters.
This table contains all the tweets in a social media pp.

The ask
- Find the ID;s of the invalid tweets(how is this identified) >>> The tweet 
is invalid if the number of characters in the content of the tweet is stricter greater than 15  

tweet_id(id)16+ > 15 invalid
tweet_id(id)14- < 15 valid

Return the result in any order


Example 1:

Input: 
Tweets table:
+----------+-----------------------------------+
| tweet_id | content                           |
+----------+-----------------------------------+
| 1        | Let us Code                       |
| 2        | More than fifteen chars are here! |
+----------+-----------------------------------+
Output: 
+----------+
| tweet_id |
+----------+
| 2        |
+----------+
Explanation: 
Tweet 1 has length = 11. It is a valid tweet.
Tweet 2 has length = 33. It is an invalid tweet.



My Own Breakdown

Just setting a eval that returns any id that is under 15 characters.


Inital build 

SELECT tweet_id FROM TWEETS
WHERE content < 15;


Sadly it returns both example tweets. Need a better eval
SO unsure what this is, but blank spaces are counts as blank spaces. 

As seen in 

Explanation: 
Tweet 1 has length = 11. It is a valid tweet.
Tweet 2 has length = 33. It is an invalid tweet.
WHERE content < 12;


Going to use LENGTH to find exactly what i am looking for. May need more expressions to extract info
from the blanks spaces. 


Wrote this 

SELECT tweet_id, LENGTH(content) as name_length
FROM TWEETS

returned 

| tweet_id | name_length |
| -------- | ----------- |
| 1        | 11          |
| 2        | 33          |

wth

So now unsure why the original expression is returning an item that is more that 15.

Oh wait, we need to return invalid tweets, dumb oversight.

Nope, needed help and apparently i am missing the CHAR_Length which seems to just compare string length and does not 
eval empty spaces. 















<img width="907" alt="image" src="https://github.com/user-attachments/assets/99035424-f827-4b15-9563-c3a2f7ddd76a" />
