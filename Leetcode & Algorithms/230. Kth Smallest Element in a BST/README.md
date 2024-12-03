https://leetcode.com/problems/kth-smallest-element-in-a-bst

**Kth Smallest Element in a BST**



Given the root of a binary search tree, and an integer k, return the kth smallest value(1-indexed)(unsure what this means)) of all values of the nodes in the 
tree

Maybe the example will clear things up.

EX1
I: root = [3,1,4,null,2], k = 1
O = 1

Doesn't help much

			3
		1		4
		
	2

EX2
I: Root = [5,3,6,2,4,null,null,1], k = 3
O = 3

				5
			3		6
		2		3	
	1
Initial thoughts looks like we need to return k within the given binary tree.
The item that makes me nervous is that the problem is medium and is most likely wanting something more 
difficult then just return k given tree.
Constraints are that n = number of nodes(not much of a constraint)

**
k needs to have a constraint on it less than 1 and not exceed 10^4 == 10000\
The same thing should be checked with the node value also.
**


all check cases for the constraints given initially
will add as i see fit. 

        if root is None or root.val > 10000:
            return None
        if k < 0: 
            return None


Hints help a bit
**
Try in-order traversal. (When initially thinking about that, need to traverse the BST in place and return k)
**
Still having trouble understanding what it means further to return the k or what the questions is 
asking.

tried to cheese the answer with 
			return k


no go :(

Ohh, I need to first build the tree out and then return k. Although it still seems to easy.
Will build it out for now and worry about k later.
May be as simple as its give.


After reading more of the discussion I see that you need to keep track of the traversal or travel of the logic/if loop
while moving through the BST. 

I understand it now

We first need a counter for the going through each node starting at 0 or root.

This is done with 

			self.count = 0

This will also help us compare the value with the kth value for later on

Now we need something to keep track of the value when moving through the BST

This is done with 

			self.result = None

None is used because we start with an empty value and will fill in that value as we move through the future loop.

If {count} is used to move through the Node then {result} is used to keep track of the  value to eventually return the compared value of k

self.count = 0 ensures you start counting nodes from the beginning of the traversal.
self.result = None acts as a global variable to store the k-th smallest value once found.

Honestly it makes sense when thinking about the ask in a general sense.
There was a breakdown in my python thinking when it comes to searching for a select item.
Without these declarations, how can we keep track and compare select {k} or given item.

Once we have the start date we now def a function called to_order which helps us move through and keep track of the items within the BST.

(Node) is used within the function to first compare and use throughout. 

We start with checking if the Node or the result of the Node is empt and returning None if that is the case.

			if not node or self.result is not None:
    				return

We then start to move throughout the BST within the first left with node.left
more specifically with 
			to_order(node.left)


how this was explained in the first BST leet, we move through the BST recursively to the left of the current node
starting at the root. 

After initializing we declare the self.count with += 1 to increment the count within the if statement.

Remembering this keeps track of .count to then compare to the next value of the given node

This means 

            self.count += 1
            if self.count == k:
                self.result = node.val
                return


With each loop[ we increment the .count
and return for k if they equal.

Essentially finding {k} if the values match. Nice

We then move to the right after the value is stored.

Its interesting to note that the code install started with traversing each node with 

		to_order(node.left)
            	to_order(node.right)
Sadly as a beginner this looks sound, but this does not respect the in order traversal that is being asked here. 

Also something I didn't know and makes sense is that smaller values are stores within the left tree
Just respecting the nature of how BST are setup.

Good to know. 

So we are left with


			in_order(node.left)
			self.count += 1
			if self.count == k:
			    self.result = node.val
			    return

			in_order(node.right)

We need to make sure that all small values are stored to the left and the highest value is stored on the right.

It also makes sense that we can also run and the code still works. 



	  to_order(node.left)
            
            self.count += 1
            if self.count == k:
                self.result = node.val
                return


Technically we just need to find the smallest value for the ask :)

we then end the code with



			        to_order(root)
			        return self.result 

This allows us to start the traversal and return as said way earlier the self.result

Overall, not bad. Good way to get some practice with more python fundamentals and some more
specific use with BST and the search functionality within BST. 
            















