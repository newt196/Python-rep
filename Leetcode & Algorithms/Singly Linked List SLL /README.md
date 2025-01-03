**Info on Singly Linked List**

https://csvistool.com/LinkedList

Going through data structures linearly starting with Arrays, I found a structure or list? or item called a Singly Linked list.

Not to be confused with an Array,...sort of and different from a Doubly Linked List.

According to https://www.datacamp.com/tutorial/python-linked-lists

Linked lists was "created to overcome various drawbacks associated with storing data in regular lists and arrays, as outlined below:"

-Ease of insertion
-Dynamic Size
-Memory efficiency

*Inserted after reviewing SLL notes*

Most elements are an efficiency of O(n)	except for the following 
Insertion and deletion at head, really anything to do with the head or the beginning of the list.

This makes sense, because its at the start where no elements need to be went through.

Now if we have to add, search, or delete or anything outside of the head the complexity is linear. 

Meaning we need to go through each element to do a certain task. Simple and not intensive, unless the list is very hard/

Should probably memorize or at least know very very well.




Not going to get into the specifics of the item, because we just need the general overview of "SLL" going to use for now...Will
go into more detail as more leetcode questions get solved with SLL efficiency.


Simple type of Linked list that consist of two parts
-Data(Actual information stored in a note
-Next Pointer(A reference to the next node) 
*Editors note Seems the last nodes next pointer is set to null....usually*

Remember (pretty ez) nodes are created in a linear fashion

Chat 

Key Operations:

Insertion:
Add a node at the beginning, middle, or end.

Deletion:
Remove a node by value or position.

Traversal:
Visit each node to perform actions or search for an element.

Creating a SLL

					class Node:
    						def __init__(self, data):
						        self.data = data  # Value stored in the node
						        self.next = None  # Pointer to the next node (initially None)

Logic here

Appending,add Nodes
-If the list is empty the new node becomes the head

Traversal/iteration
-Start from the head(obvious)
-Following the next pointers until the end of the node is None or at the End

Insertion
-Going next until a key value is found or None is returned

Deletion
-To delete a node update the next pointer of the previous node to skips the node to be deleted

Some basic Chat examples to be used if you want to implement SLL

Inset element at the beginning


		def prepend(self, data):
		    new_node = Node(data)
		    new_node.next = self.head  # Point the new node to the current head
		    self.head = new_node       # Update the head to the new node


Delete by value, same with add by value if methods are adjusted

			def delete(self, value):
			    if not self.head:  # If the list is empty
			        return
			    if self.head.data == value:  # If the head contains the value
			        self.head = self.head.next  # Update the head to the next node
			        return
			    current = self.head
			    while current.next and current.next.data != value:
			        current = current.next
			    if current.next:  # If the value is found
			        current.next = current.next.next


*Editors note found in "https://csvistool.com/LinkedList" 
Remember we can start at the beginning or tail end, unsure if this was mentioned within the notes


Some basic leetcode code models provide by Chat

note the _init_ meaning the initialization vector for both the class and def for self.



	class Node:
	    def __init__(self, data):
	        self.data = data
	        self.next = None
	
	class SinglyLinkedList:
	    def __init__(self):
	        self.head = None
	
	    # Print the linked list
	    def print_list(self):
	        current = self.head
	        while current:
	            print(current.data, end=" -> ")
	            current = current.next
	        print("None")
		

^this is an example for the basic setup for a SLL^

Reverse SLL

	def reverse_linked_list(head):
	    prev = None
	    current = head
	    while current:
	        next_node = current.next  # Store the next node
	        current.next = prev       # Reverse the pointer
	        prev = current            # Move prev one step forward
	        current = next_node       # Move current one step forward
	    return prev  # New head of the reversed list


Find the Middle if available


	def find_middle(head):
	    slow, fast = head, head
	    while fast and fast.next:
	        slow = slow.next       # Move slow by 1 step
	        fast = fast.next.next  # Move fast by 2 steps
	    return slow  # Slow pointer will be at the middle


Merge two lists

	def merge_sorted_lists(l1, l2):
	    dummy = Node(0)
	    current = dummy
	    while l1 and l2:
	        if l1.data < l2.data:
	            current.next = l1
	            l1 = l1.next
	        else:
	            current.next = l2
	            l2 = l2.next
	        current = current.next
	    current.next = l1 or l2  # Append the remaining nodes
	    return dummy.next


Remove the nth node from the end of the list
*note this uses two pointers from left to right and right to left


	def remove_nth_from_end(head, n):
	    dummy = Node(0)
	    dummy.next = head
	    slow = fast = dummy
	
	    # Move fast ahead by n+1 steps
	    for _ in range(n + 1):
	        fast = fast.next
	
	    # Move slow and fast together until fast reaches the end
	    while fast:
	        slow = slow.next
	        fast = fast.next
	
	    # Remove the nth node
	    slow.next = slow.next.next
	    return dummy.next

		class Node:
		    def __init__(self, data): # some key notes __ > _ | init is used to initalize the class
		        self.item = data    # self and data are used and seperated with ","
		        self.ref = None

^^^Remember 


		Class Node:
			def__init__(self, data): # correct
				self.item = Data # this was wrong, remember that item needs to be replaced or reference the current data
				self.ref = None	# was all wrong, need to remember we have self.item and self.ref(for the next item) this needs to be None
						for the reference of the next node or item
^^^ first part of SLL


Cases for adding to the Beginning and End


Beginning

		def beginning(self, data):
			new_node = Node(data) # referencing the new data coming to the head
			new_node.next = self.head # pushing the old node by 1
			self.head = new_node # pushed nodes 

Going to better understand this with an example <--- just for me
EX: [0,4,9,7,8]
Add the value 3
New Node points to the beginning > we assign the new node to the self.head which is the number 3.

The number 3 is then set to the beginning. Nothing more nothing less. We then can keep adding numbers due to the nature of new_node self iterating in the 3 and 5th line

End
						
      							def End(self, data):
							new_node = Node(data)
							if not self.head: 
								self.head = new_node
								return
							current = self.head
							while current.next:
								current = current.next
							current.next = new_node

Just for me.

In the example we have the following
EX: [3,0,4,9,7,8]

We want add 12 at the end. 

new_node now is set to Node(12) which will be used to access "where" it goes. Which in this case is at the end

the first if statement is used to see if the list is empty.

Because we are have items we move to the iteration
We use .next to move through the list sequentially until we reach the end.

In this case the end is reached current.next is now the new node.
Meaning 
[3,0,4,9,7,8,12]

visualizing the code means we iterate with .next until the end is reached
Once reached current.next is set to new_node. 




















