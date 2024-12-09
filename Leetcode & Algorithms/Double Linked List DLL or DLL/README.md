Now for Doubly Linked List or DLL

Credit to:
https://www.geeksforgeeks.org/doubly-linked-list-in-python/
https://csvistool.com/DoublyLinkedList

Instead of a value stored in a node and a pointer to the next.

DLL is the same, plus a pointer to the previos node
So

-Data
-Pointer to the next node
-Pointer to the previous Node

Seems to add more versatility then SLL. 

For a more structured de provided by geeks is 

Doubly Linked List (DLL) is a special type of linked list in which each node contains a pointer to the 
previous node as well as the next node of the linked list. 
In a Doubly Linked List, we can traverse in forward and 
backward direction using the next and previous pointer respectively.

This is the standard setup 

    class Node:
        def __init__(self, data):
            self.data = data  # Data stored in the node
            self.prev = None  # Pointer to the previous node
            self.next = None  # Pointer to the next node


#List Class Structure

    class DoublyLinkedList:
        def __init__(self):
            self.head = None
    
        # Print the list forward
        def print_forward(self):
            current = self.head
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")
    
        # Print the list backward
        def print_backward(self):
            current = self.head
            while current and current.next:
                current = current.next  # Move to the last node
            while current:
                print(current.data, end=" -> ")
                current = current.prev
            print("None")



So instead of 1 > 2 > 3 > 4

We have 1 <> 2 <> 3 <> 4

So like the example given each node has two pointers pointing to the next and the previous node

The first node’s prev pointer is None, and the last node’s next pointer is None.

Note*

Insertion 
- Add a node at the beginning, middle or end


Advantages Over Singly Linked Lists:

- Bidirectional traversal.
- Easier deletion of a node when a pointer to it is provided (no need to traverse the list to find its predecessor).


Some Key code examples for leetcode usage

Inserting a given element at the beginning

      def insert_at_beginning(self, data):
          new_node = Node(data)
          if self.head is None:  # Empty list
              self.head = new_node
          else:
              new_node.next = self.head
              self.head.prev = new_node
              self.head = new_node

Insert at the end

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:  # Empty list
            self.head = new_node
            return
        current = self.head
        while current.next:  # Traverse to the last node
            current = current.next
        current.next = new_node
        new_node.prev = current

Delete at a given node

    def delete_node(self, target):
        if self.head is None:  # Empty list
            return
        if self.head.data == target:  # Node to delete is the head
            self.head = self.head.next
            if self.head:  # Update the new head's prev pointer
                self.head.prev = None
            return
        current = self.head
        while current and current.data != target:
            current = current.next
        if current:  # Node with target data found
            if current.next:  # Not the last node
                current.next.prev = current.prev
            if current.prev:
                current.prev.next = current.next


Reverse a given list

    def reverse(self):
        current = self.head
        prev = None
        while current:
            # Swap next and prev pointers
            next_node = current.next
            current.next = prev
            current.prev = next_node
            prev = current
            current = next_node
        self.head = prev  # Update head to the new first node

The complexity is the same DLL as SLL

Changes and searches are only fast at the beginning

Everything else is O(n)


ADV and DIS

Advantages:

- Bidirectional traversal is required.
- Efficient deletion or insertion at both ends or when a pointer to the target node is available.
- More flexible than singly linked lists.


Disadvantages

- Higher memory usage due to two pointers per node.
- Slightly more complex implementation.











 
