
<img width="430" alt="image" src="https://github.com/user-attachments/assets/d88025ff-79d5-426d-91e7-2506e7b66ac3" />



https://leetcode.com/problems/average-time-of-process-per-machine/description/?envType=study-plan-v2&envId=top-sql-50

2-13 0          | 0          | start         | 0.712     |
| 0          | 0          | end           | 1.520     |
| 0          | 1          | start         | 3.140     |
| 0
A bit difficult at least on the second read through. On the third read through I sort of get what is being asked here.

We are given a 

Table: Activity

We have 3 types of columns that have unique numbers given 
These are 
- Machine-id
- Process_id
- Activity-type

The item that does or could remain the same is 
- timestamp(start/end time)
^think about it...user logs in for set amount of time as the same amount of time as another user.

(unsure how to do this yet)Also  think about the average time to three decimals places

Given machine-id and preocess-id for given(per machine-id)
The start and end time are logged for both.

The ask, return the average time for....
the each machine

avg of preccessing time
The best example given.		process 1		process 2 	avg
Machine 0's average time is ((1.520 - 0.712) + (4.120 - 3.140)) / 2 = 0.894

My thoughts

What  i need to return
- machine_id
- processing_time **ref(AS processing time)

What I need to evaluate
- Machine id (once)
- Process_id(as many times as needed per the given machine_id(user could start word, timeclock, another programs)
- activity type(twice | start/stop)
- Average time of the activity type == (process_id) activity type(stop) - activity type(start) / number of process id's per machine

Started playing around with AVG.

Started with 

SELECT AVG(process_id) AS AveragePrice FROM Activity;

| AveragePrice |
| ------------ |
| 0.5          |


Now 

SELECT machine_id, AVG(process_id) AS AveragePrice FROM Activity;


| machine_id | AveragePrice |
| ---------- | ------------ |
| 0          | 0.5          |

Almsot, we are only getting one machine with an average price of process id
also hint here, only process id which should not be the case.


Forgot about the GROUP BY function and we now have some gas to cook with 

SELECT machine_id, AVG(timestamp) AS AveragePrice FROM Activity
GROUP BY machine_id;


| machine_id | AveragePrice       |
| ---------- | ------------------ |
| 0          | 2.372999995946884  |
| 1          | 0.9874999821186066 |
| 2          | 4.027999997138977  |


We could use a Select ith a direct end - start and evaluate the expression sepertyl. 
Something like


Need use Selfjoin after asking for a hint???


Currently have 
        
        SELECT a.machine_id, ROUND(AVG(b.timestamp - a.timestamp) AS processing_time FROM Activity a JOIN Activity B
        GROUP BY a.machine_id;


groups are not occurring properlyu either with a. and b. or with GROUP_BY

Coming back to this as of 2-19 will need to rereview the notes and the ask. 
I understand the ask and going to pick back up on the above provided code.

Currently running into the compile error. 

You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'FROM Activity a JOIN Activity B
GROUP BY a.machine_id' at line 1

My code 

      SELECT a.machine_id, AVG(b.timestamp - a.timestamp) AS processing_time 
      FROM Activity a JOIN Activity 
      ON process_id
      GROUP BY a.machine_id;

Fiddling around with some functions that couyld help correlate the approprioate data with each other
Like JOIN with Activity, ON with Process_ID(ON is used because we could have multiples)
GROUP BY is our return function


Sadly this returns a syntax error.

After some adjusting found a way to use a.process and b.process to structure the data provided if multiples were found.

We now have 


        SELECT a.machine_id, AVG(b.timestamp - a.timestamp) AS processing_time 
        FROM Activity a 
        JOIN Activity b 




This is awesome because we use the following to correlate each process with activity to process
***Hint provided in Discussion***
Fiddled around with JOIN and ON and documentation to find the solution with 

      ON a.process_id = b.process_id AND a.machine_id = b.machine_id
      WHERE a.activity_type = 'start' AND b.activity_type = 'end' 


Sadly this does not round properly.

Tried addingROUND() to the following 
SELECT a.machine_id, ROUND(AVG(b.timestamp - a.timestamp)) AS processing_time 

and this just rounded items to a 1 or 0.

I think we need to round the actual returned function instead of the initial numbers. 

Nope, quick search I was able to adjust the inital ROUND() with the following 

        SELECT a.machine_id, ROUND(AVG(b.timestamp - a.timestamp), 3) AS processing_time 


Once done we have the first test passed with 
        
        SELECT a.machine_id, ROUND(AVG(b.timestamp - a.timestamp), 3) AS processing_time 
        FROM Activity a 
        JOIN Activity b 
        ON a.process_id = b.process_id AND a.machine_id = b.machine_id
        WHERE a.activity_type = 'start' AND b.activity_type = 'end' 
        GROUP BY a.machine_id;




