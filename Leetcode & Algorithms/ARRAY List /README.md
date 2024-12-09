**General info for info provided in an Array List**


https://csvistool.com/ArrayList

Most info is provided from a general understanding of leetcode problems, CS visualization, and general info from videos. 

Mostly info and yapping about Array Lists that could make solving leetcodes or problems regarding Array Lists.

Going to go backwards from 

-General info
-Leetcode notes
-CS visualization


Starting with general info going to have a rundown on how lists are or could be handled.

Syntax: my_list = [1, 2, 3, "apple", True]   <--- This is mutable

my_list = [1, 2, 3]
my_list.append(4)  # Adds 4 to the end
my_list.remove(2)  # Removes the element with value 2
my_list[1] = 99   # Updates the second element to 99
print(my_list[0]) # Access the first element

Dont need to review index and more freshman material, just revieing syntax rules.


Leetcode Notes

Typically single iteration O(N) for complexity, this is due to the fact that we are looping through each element through the index.

For the python code, we typically use a for loop looking like >


			for item in my_list:
			    print(item)

Useful Methods:

.append(value): Add an item to the end.
.pop(index): Remove and return the item at a specific index.
.sort(): Sorts the list in place.
.reverse(): Reverses the order of elements in place.

These need to be memorized near perfectly. This should help in solving problems and help manipulating over items more easily.


For The visualization, there isn't much to understand here.

We can understand this more be visiting "https://csvistool.com/ArrayList"


For a better understanding of methods used to modify lists we can use the a random list like 

[3,15,16,2,12,1]
 0  1  2 3 4  5

The bottom number are already understood.


The most complicated of these is removing and adding numbers between the index.

*Editors note* Iterating and finding given n at i index.


Notating that when we add or removing a given element we need to notate the new index for the changed array order.


Chat was able to better explain this with the methods provided. 

*Need to notate this to shortcut methods when solving leetcode problems

APPEND	

				my_list = [1, 2, 3]
				my_list.append(4)
				print(my_list)  # Output: [1, 2, 3, 4]


Extend 

				my_list = [1, 2, 3]
				my_list.extend([4, 5])
				print(my_list)  # Output: [1, 2, 3, 4, 5]

Modify be Index

				my_list = [1, 2, 3]
				my_list[1] = 99  # Update the second element
				print(my_list)  # Output: [1, 99, 3]
Modify by Slicing
				
				my_list = [1, 2, 3, 4]
				my_list[1:3] = [99, 88]  # Replace elements at indices 1 and 2
				print(my_list)  # Output: [1, 99, 88, 4]

Remove by Index

				my_list = [1, 2, 3]
				removed_element = my_list.pop(1)  # Remove element at index 1
				print(my_list)  # Output: [1, 3]
				print(removed_element)  # Output: 2
Sort ascend or descend

				my_list = [3, 1, 2]
				my_list.sort()  # Ascending order
				print(my_list)  # Output: [1, 2, 3]

				my_list.sort(reverse=True)  # Descending order
				print(my_list)  # Output: [3, 2, 1]

Replace and Assign
      			
              my_list = [1, 2, 3, 4]
      				my_list[1:3] = [99, 88]  # Replace elements at indices 1 and 2
      				print(my_list)  # Output: [1, 99, 88, 4]




















