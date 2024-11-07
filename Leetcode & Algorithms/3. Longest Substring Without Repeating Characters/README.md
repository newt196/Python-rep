
**https://leetcode.com/problems/longest-substring-without-repeating-characters/**

<img width="451" alt="image" src="https://github.com/user-attachments/assets/b9072a4b-69c6-4649-9a80-3f6d8ac857be">


Given a string, find the length of the longest substring without repeating characters. 


s = abcabcbb
Output = 3
ANS = The output is abs, with the length of 3

s = bbbb
Output = 1
ANS = The output is only "b", with the length of 1


Initial planout. 
for i in range. Analyzing the given string to find the matching string of the given string. 

When doing some "maxlen" research within stack overflow. Seems the sliding door method needs to be implemented here. 
General principle here 

s = 8 elements 
window size = 3

Output = 
123
234
345
etc

The window size should always be 3. 
Need a way to organize the program to go through S and arrange the strings that are non matching. 


Going to take the engine or block approach here. 

Started with a method to store the S args and to properly store the arg within a function called set()
char_set = set() # This will be used to store the args within S
left = 0 #English left to right for the args.
max_length = #0 Store the max length of the substring provided within args

For more info we are going to use left and right pointers within this algo, to keep track of our position within the program.


Next steps are the following.
for right in range(len(s)): # here we want to move the pointer across the provided S
	whiles[right] in char_set: #While is used to process the "right range find" within the left change right now
		char_set.remove(s[left])
		left += 1 This resets our window or size from the left. 
 
	char_set.add(s[right]) #add the current character to the set within the iteration

	max_length = max(max_length, right - left + 1) #the final update and check to find the max length found within the provided ARG
	return max length

Chats visual representation of the logic starting with the "while" loop


<img width="340" alt="image" src="https://github.com/user-attachments/assets/a9f644b6-71f7-416d-8024-67625211aa95">


