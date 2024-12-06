**https://leetcode.com/problems/length-of-last-word\**



**Length of Last Word**


Given a string s consist of words and spaces, return the length of the last word in the string.

Easy enough with no need to put the examples here.

Things to note:
Spaces need to be put into serious consideration or cutout altogether to get to the last word.
Note the last word within {s}



started out with traversing the array with 


			help = ""

Starts the array while we setup the for loop to iterate over the spaces and words

We then want to collect set the length of s with 

		length = len(s)

While we have the necessary structures and functions to 


			      for i in range(length - 1, -1, -1):  

We specify the range with the following 

Starting point: length -1 | 0th index
Stopping point: -1 | Before reaching -1 we include 0 as the loop reiterates.
Point to increment: also -1 | logic here is that we are going backwards hence getting us closer to 
the answer.



We now use the following to check for only strings and removing spaces.


	            if s[i] == " ":
                	if help:  
                   	 break


" ": is done backwards to check for strings, while the below if statement
is used to ignore empty spaces.

Needed help with [if help] to wonder how to ignore empty spaces.
Although like most solutions here, it was a google search away. 

Now that we have the main search function, we use the following to collect the index or characters 

hence the +=, remember that we build what help was supposed to be with help = ""

So as we iterate through the loop we are doing the following



			        for i in range(length - 1, -1, -1):  


iterate backwards starting at -1, 


            if s[i] == " ":
throw out any blank spaces  

else

help will find and add characters it finds in the given [S]
 with 


                help += s[i]


In all we have 



      class Solution:
          def lengthOfLastWord(self, s: str) -> int:
              help = ""
              length = len(s)
              for i in range(length - 1, -1, -1):  
                  if s[i] == " ":
                      if help:  
                          break
                  else:
                      help += s[i]
              return len(help)


About 30 minutes to figure out, with only 2 or 3 minutes to figure out the logic.
While it it took 15 minutes to code it out. 










