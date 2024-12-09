Info on Singly Linked List

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








