**https://leetcode.com/problems/string-to-integer-atoi**

<img width="455" alt="image" src="https://github.com/user-attachments/assets/1faf5863-9a05-4950-8347-8ee3983a1361">



<img width="574" alt="image" src="https://github.com/user-attachments/assets/eb895aeb-0c27-40da-b26f-8bf97d799b5d">

We are given "" a string is provided with absolute numbers, no(letters) and white space.
We need to conver the S to a 32 bit integer or a number

Seems like we need to return the exact string remove anyt whitespace provided within S
* we have a if else statement that removes integers that are outside of [-2**31, 2**31 - 1]

Input: s = "42"

Expected O = 42

Input: s = " -042" (note the blank space)

Expected O = -42

Standout = "1337c0d3"

Expected O = 1337

Inital thoughts and logic.

We need a way to convert the first str to an integer. 

Possibly starting with 
STR = []

and then using a pointer to then go through the provided string and its spaces to return only the str(removing the letters and open spaces)
Also remember we need to account for (-)

First we need a way to strip the white spaces. This can be done with 

        s = s.strip()

The STout is the string without white spaces which is good. 

Although we need to address case two being "  -042"
We need to account for - substring and the 0 in front of the price being "42"
Tried stack overlfowe and found 

        s = s.lstrip('0')


Although this did not remove the 0 as expected. In doing more reading, I need to account for the substring first and then account 
for the 0 provided. 

We first need to create a function to remove the substrings within the provided string...for now.
We assign sign the following 

	sub = 1 (which is positive by default)
	if s and s[0] == '-'" 
		sub = -1
		s = s[1:]

This first checks if the string starts with the negative substring.
It then checks if s is not empty within  (s[0] == '-')
The a negative is found then sub = -1 lets the program know the string is negative
Check if the string starts with '-':
Once it knows the string is negative we then slice the substring with 

		s = s[1:]


We then move to the positive with 

		elif s and s[0] == '+':
            	s = s[1:]

Doing the same thing if a positive integer is found. 

This satifies the substring task within the problem. 


Completed this through '' defining a method that will be used to convert the str to int. 

This is done be creating the following 

	tran = ''

This helps us create an empty space 

	for char in s:
           if char.isdigit():
                tran += char
           else:
                break  

tran will take the charecters from sub and convert them to int.

We first use a for loop to iterate over each str within S using 

 	for char in s:
            if char.isdigit():
                tran += char

the if statement then uses isdigit to convert each iteration of the loop to convert the characters into an int

          	else:
                break 

We close with a else/break to close at the first stop of a char that is not a number. 

Not going to lie, had to lookup the logic for limiting the min and max. 

        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

For next time i am going to convert the str earlier, because doing it afterwards was a bit silly and not productive. Only good for learning extra steps :(
