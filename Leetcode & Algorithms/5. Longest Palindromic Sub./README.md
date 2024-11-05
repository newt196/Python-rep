<img width="578" alt="image" src="https://github.com/user-attachments/assets/37a40b05-0afb-415e-a72e-d788cea491a8">



<img width="570" alt="image" src="https://github.com/user-attachments/assets/827608d1-afac-4c16-89b3-fc532400b6bb">


5. Longest Palindromic Substring(String that reads the same forward and backward

Given a string, return the longest palindromic substring.
EX: s=babad
O=bab or O=aba

EX:s=cbbd
O=bb



Ideas 
Setting a string to an array in (for i in range) and using a function to find links between the set. (Unsure if an array should be used)
Somehow evaluate the string set the string to be evaluated front and backwards
Subpoint(we can create two strings from the evaluated string. Setting both string in a if == statement that evaluates both strings backwards or forwards.

Sub sub point, we can evaluate and append non necessary letters and reverse the second string backwards. 

        print(s)
        rev = s[::-1]
        print(rev)

# we now hav "rev" and "s"
# EX babad & dabab

We need a way to extract the same "aba" for both s and rev

First creating a set to store the values for the second part of the logic. 

        longest_palindrome = ""

we then set a for loop within i and j iterating over (i,n) iterating over all possible instances of both combinations.

i is the starting index while j is the ending index of the substring. we are comparing each substring of s with a corresponding substring in rev to check if they are the same. This is seen in 


        for i in range(n):
            for j in range(i,n):



i is the starting index of the substring.
j is the ending index of the substring.
By varying i and j, we can capture every substring in s, starting from each character and extending to all subsequent characters.



Step 4: Find the Matching Substring in rev
To check if substring_s is a palindrome, we want to see if there’s an equivalent substring in rev at a mirrored position. The corresponding substring in rev for s[i:j+1] is found with this line:

                substring_s = s[i:j+1]
                substring_rev = rev[n-j-1:n-1]

is used for the logic afterwards to compare the two strings. 

Step 5: Check for Palindromic Substring
Now that we have substring_s from s and substring_rev from rev, we check if they are equal:


                if substring_s == substring_rev and len(substring_s) > len(longest_palindrome):
                    longest_palindrome = substring_s












