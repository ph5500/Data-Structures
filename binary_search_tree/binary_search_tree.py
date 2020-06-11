"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
# from collections import queue
# import linked_list from LinkedList
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
    

        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #self will be the root
        # compare the target against self
        if target == self.value:
            return True
        if target < self.value:
        # go left if left is a BSTNode
            if not self.left:
                return False
            return self.left.contains(target)
        else:
        # go right if right is a BSTNode
            if not self.right:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        current_max = self.value
        
        while self.right is not None:
            current_max = self.right.value
            self.right = self.right.right
        return current_max
        
        # if not self.right:
        #     return self.value
        # return self.right,get_max()

    # Call the function `fn` on the value of each node
    # doesn't actually return anything
    def for_each(self, fn):
    # this method specifically does want to traverse every tree node
    # has to call the fn on self.value
        fn(self.value)
    # is there a left child?
        # if yes, call it's for_each with the same fn
        if self.left:
            self.left.for_each(fn)
    # is there a left child?    
        if self.right:
        # if yes, call it's for_each with the same fn            
            self.right.for_each(fn)


#  			def depth_first_for_each(self, fn):
# 				# this method specifically does want to traverse every tree node 
# 				# this has to call the fn on self.value 
# 				fn(self.value)
# ​
# 				# how do we propagate to all the other nodes in the tree? 
# 				# is there a left child? 
# 				if self.left:
# 					# if yes, then call its `for_each` with the same fn 
# 					self.left.depth_first_for_each(fn)
# 					# is there a right child?
# 					if self.right:
# 						# if yes, then call its `for_each` with the same fn 
# 						self.right.depth_first_for_each(fn)
# ​
# 						def iter_depth_first_for_each(self, fn):
# 							# with depth-first traversal, there's a certain order to when we visit nodes 
# 							# what's that order? 
# 							# init a stack to keep track of the order of nodes we visited 
# 							stack = []
# 							# add the first node to our stack 
# 							stack.append(self)
# 							# continue traversing until our stack is empty
# 							while len(stack) > 0: 
# 								# pop off the stack 
# 								current_node = stack.pop()
# 								# add its children to the stack 
# 								# add the right child first and left child second
# 								# to ensure that left is popped off the stack first 
# 								if current_node.right:
# 									stack.append(current_node.right)
# 									if current_node.left:
# 										stack.append(current_node.left)
# 										# call the fn function on self.value 
# 										fn(self.value)
# ​
# 										def iter_breadth_first_search(self, fn):
# 											# breadth first traversal follows FIFO ordering of its nodes
# 											# init a deque 
# 											q = deque()
# 											# add the first node to our q 
# 											q.append(self)
# ​
# 											while len(q) > 0:
# 												current_node = q.popleft()
# 												if current_node.left:
# 													q.append(current_node.left)
# 													if current_node.right:
# 														q.append(current_node.right)
# 														fn(self.value)
            #same as dequeing from our stack 
    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
