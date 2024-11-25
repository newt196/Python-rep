**https://leetcode.com/problems/h-index**

Given an array of integers [citations] where [citations[i]] is the number of citations a researcher received for their [i]th paper, return the researchers h-index.

-Initial explanation is kind of confusing, but it sounds like using the value and area of the index to find this h. 

According to the definition of h-index on Wikipedia: the h-index is defined as the max value of h such that the given researcher has published at least h papers that have each been cited at least h times.

-Still doesn't help with the definition of h

Example does help here
EX: citations = [3,0,6,1,5]
O: 3
Explanation: [3,0,6,1,5] means the researchers has 5 papers or [4]indexes of papers in total. Each of the them had 
received 3, 0, 6, 1, 5, citations respectively. Since the researcher has 3 papers with at least 3 citations and the remining two with no more than 3 citations each, their index is 3.

-Explains the first part, but not the second part. The logic is not logging. 

EX = [1,3,1]
O: 1
EX: N/A

Going to go through the hint first.

H1: An easy approach is to sort the array first(ascending pls)
H2: What are the possible values of h-index
H3: A faster approach is to use extra space(this doesn't make sense)


Discussion notes
- sort()
-decent understanding of h-index. PHD type issue that just determines a scholars success with at least 3 or more citatiosn based on what they have published.

So in the first EX [3,0,6,1,5] we sort the array ascending to [0,1,3,5,6]
Which means the current scholar has at least 3 publications with at least 3 or more citations. 
Making 3 this current 
After doing some digging, it sounds like we need to do descending order and compare the value to the index value.
Remember we need to add +1 to the index to make it human and logic safe.

I now get it, so the index is more important or at least a starting point vs the value.
So a general understanding is that if we have [10,8,5,4,3]
The first index is 0 | 10 which is the first item meaning 10 is greater than 1 h=index
The second index is 1 | 8 is stil greater than 2 which is the h = index
The thirs index is 2 | 5 is still greater than 3 which is the current h = index
The fourth index is 3 | 4 is the same as the h which is the current h = index
The fith index is 3 (we start to have issues) | 3 is less than the current h = index which is 4
h=4


Logic 

Kind of hard to put the human logic into computer/python logic.

Will break the part down for now
1. We need to sort the array(descending)
2. We need ne newarray and make sure its indexes are being +1 
3. we need to compare the new array with the in relation to its index. 

Return we need to return the final product of the h logic.
After some digging with the first requruirment, was able to find the first part with the following

        class Solution:
            def hIndex(self, citations: List[int]) -> int:
                citations.sort(reverse=True)   
                return(citations)

Notes: Used Sort initially, but it does it in ascending order by default, used reverse=true first but it needs to be cap to be used properly. 
Notes: Used return to save the results for the next part of the solution. 


Just learned I cant use return if I want to keep resuming in the def.
I am now using enumerate to get the value and the index without having to manually search and get both. 

We now have 


      class Solution:
          def hIndex(self, citations: List[int]) -> int:
              citations.sort(reverse=True)   
              print(citations)
              for index, value in enumerate(citations):
                  print(index + 1,value)

This returns 

[6, 5, 3, 1, 0]
1 6
2 5
3 3
4 1
5 0

This helps us with the second part of the solution
Even note that our indexes represent the real world publishing of scholar publishing.
Don't know if this has to be said, but the publishing's do not start at 0 :)


We now need logic for the following

3. we need to compare the new array with the in relation to its index. 

sounds like an if/else statement to meet the requirements and dont forget
fringe cases with 0

some logic tries

 
            for value in index + 1(): # not iterable
                if value < index +1:
                    citations.remove(value)
                if value == 0: 
                    return none
                if index + 1 == 0: 
                    return 0


Overcomplicating items, I just settled on if the value is less than the index + 1 in the loop return the index. 
This is important because the index represents the h value

This is represented with 

        for index, value in enumerate(citations):
                    if value < index + 1:        
                        return index

Sad thing is we aren't efficient or we dont handle fringe cases. 

added just in case citations is empty and the scholar is sad and lazy.
 

      if not citations:
                  return 0

Post Task

the task was not hard, it was more that the ask for h-index was unknown and needed to be understood very well to proceed.
After that, moving through the process was not hard.









