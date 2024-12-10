**Bubble Sort** 


https://csvistool.com/BubbleSort

https://see-algorithms.com/sorting/BubbleSort

Firstly Bubble Sort is a simple comparison-based sorting algorithm. It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. This process is repeated until the list is sorted. It does this until the desired element if found. 


In my humble explanation it just seems the we have two pointers or two entities that compare two elements and swap if they are out of order. Reiterating over the list until the order is correct.

 
[9,5,3,4,56,68,5,1] > [1,3,4,5a,5b,9,56,68] per the website.

For the most part, should not be used. Use cases are so small, its not usefull. Better
sorts are Quick, Merge and Heap.

BIG O efficiency 

Sorted: O(n)

Average: O(n^2)

Worst Case(List is in reverse order): O(n^2) 


Algorithm Steps:
- Start with the first two elements of the list.
- Compare them:
                 If the first element is greater than the second, swap them.
                 Otherwise, return
- Move to the next pair of elements and repeat the comparison.
- Continue until the end of the list is reached.
- Repeat the process for 


As for the website see-algorithms, they have provided logic that is language agnostic.

It starts with the following. 

      for i = 1 to (n - 1):
              swapped = false
              for j = 1 to (n - i):
                  if arr[j] < arr[j + 1]:
                      swap(j, j + 1)
                      swapped = true
              if not swapped:
                  break


Now for the example

		for j = 1 to (n - i):
            		if arr[j] < arr[j + 1]:
               		 swap(j, j + 1)
                	 swapped = true

this is the code block/loop that is doing the heavy lifting.

In this case its only used to sort the array sequentially. [100,9,3] > [3,9,100] 
Lets break it down with the provided code logic from the website

starting with 

		for j = 1 to (n - i):

a for loop is used to iterate through the array to compare adjacent items.
For each pass, i in the outer loop, the inner loop reduces its range with n-1. 
	

            		if arr[j] < arr[j + 1]:

the if condition is used to check wether the element is smaller than the next. 
<  arr[j + 1] if truem the elemtns are in the wrong order and then swapped with 
swap(j, j + 1)



As for the base case with python, we have the following code and explanation at the bottom. 

      def bubble_sort(array):
      	n = len(array)
      	for i in range(n)L
      		swapped = False
      		for j in range(0, n-i-1):
      			if arr[j] >arr[j+1]:
      				arr[j], arr[j+1], arr[j]
      				swapped = True
      		if not swapped:
      	return arrary

^^going to be a bit hard to remember

break down is as follow

      def bubble_sort(array):	
- straightforward for the given array

      n = len(array)
- The variable n stores the number of elements in the list (array)
- This helps to control the number of iterations in the outer loop

      for i in range(n):
- The for loop is used to run over (n) times from 0 to n-1.
- for each pass through the array we do the following:

1. The largest unsorted element moves or bubbles up to the correct position
2. After i passes, the last elements are sorted and do not need to be checked again.

Swapped = False
- This used to start the variable as false at the beginning of each pass
- This checks whether any items were swapped during the pass

      for j in range(0, n-i-1):
- Current loop compares adjacent elements
- Range = 0 to n-i-1
- n-i-1 ensures we avoid rechecking the last i sorted elements

Together we have 

          if array[j] > array[j+1]
          	array[j], array[j+1] = array[j+1], array[j]

- The first condition checks if the current elements is greater than the next element
- If the case passes if true, then the elements are swapped to the correct order

- The second condition is then used to exchange the two elements.

- The swapped flag is used to indicate that the swap has occurred.

^This is the main element for the comparison and swap when thinking about it





	
