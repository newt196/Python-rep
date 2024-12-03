**https://leetcode.com/problems/invert-binary-tree**


**Invert Binary TREE**


Given the root of a binary tree, invert the tree and re turn its root.

Sources:
https://www.geeksforgeeks.org/introduction-to-binary-tree/
https://www.geeksforgeeks.org/complete-binary-tree/

Need to research how to manipulate nodes and the logic and variables to do so. 

EX:

			4								4
		2			7					7			2
	1		3	6		9			9		6	3		1

IO: root = [4,2,7,1,3,6,9]	
O: [4,7,2,9,6,3,1]

It doesn't look like we are exactly returning the root here which is 4, but logic that inverts(put upside down or in the opposite position, order, or arrangement)

Which when looking at the flip
2 and 7 have been flipped

and the order of the 2nd node has been flipped
meaning: 1369 > 9631

Literally all nodes have been flipped

Sounds EZ enough. 
**
Remember fringe cases or constraints like 0 or if the range is 0 or exceeds 100.
**
I understand it now
Constraints
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

if range of node == 0
return none
if range < 100
return none
else 

Last example for the rode.

EX 

				2					2	
			1		3			3		1

I: root = [2,1,3]
O: [2,3,1]

The first value is always root.
Initial thoughts for logic completion.

Need two things off the bat.

Need a way to achieve looking at each created node
Need a way to reverse(with code) within that group or node.
Also because root is already within its own node or root group, it wont be touched unless there is serious trolling.


This is first given within the comments which I haven't seen within leet 

      # Definition for a binary tree node.
      # class TreeNode:
      #     def __init__(self, val=0, left=None, right=None):
      #         self.val = val
      #         self.left = left
      #         self.right = right
      class Solution:


Logic run through, we can go through the root(without touching(which now thinking doesn't matter if i touch)) iterate through each child tree and group and reverse. 


In the discussion part of leet, found some help in some approaches for solving.

Recursive Approach: Swapping the left and right child of every node in subtree recursively.
(earlier mentioned) sadly i know little of recursion except for self iteration until the proble m is solved.
Using Iterative preorder traversal: Converting recursive approach to iterative by using stack.
(no idea)
Using Iterative level order traversal: Iterative approach by using a queue.
most straightforward
 by going through each node and inverting the number with its pair

Seems like when going through the discussion a bit more, the first option is a little beginner friendly.

**
Will go through other picks later on 
**

Going to start with 

       class TreeNode:
           def __init__(self, val=0, left=None, right=None):
               self.val = val
               self.left = left
               self.right = right

which was install commented out, but seems more straightforward
going to already make exceptions for 0 and 100 instead of thinking about it later.
Although I can see as a programmer how thinking about edge cases could start at any part of the problem solving phase.


Achieved the fringe case with an "or" statement including the following 

if self is None or self.val > 101:
            print(None)

handles the case of any value holding 0 or values above 100.
(probably need to greater than or equal to next time)

So apparently I missed the whole point of the start and need to start here 

      class TreeNode:
          def __init__(self, val=0, left=None, right=None):
              self.val = val
              self.left = left
              self.right = right
      class Solution:
          def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:


adjusted the exception for the following to make it a bit cleaner

        if root is None or root.val > 100:
            return None

we then uise this main function as early stated to invert the nodes and onl;y the child nodes as to no
touch or affect the root number

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

We call root.left and right and just apply the invert function to only the tree portion of the node.
So anything or entity that is not root will invert whether it is left or right.

We then return root for the finishing touch.


Also also shot out to 

https://favtutor.com/blogs/invert-binary-tree


















