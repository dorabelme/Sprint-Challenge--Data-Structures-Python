from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if insterting we must already have a tree/root
        # if value is less than self.value go left, make a new tree node if empty otherwise keep going (recursion)
        # if greater than or equal to then go right, make a new tree node if empty otherwise recursion
        if not self.value:
            self.value = value
        elif value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # if target == self.value return it
        # otherwise go left or right based on smaller or bigger
        if target == self.value:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        elif target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # if right exists, go right
        # otherwise return self.value
        if self.right == None:
            return self.value
        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

    def for_each(self, cb):
        # if not self.value:
        #     return None
        # cb(self.value)
        # if self.left:
        #     self.left.for_each(cb)
        # if self.right:
        #     self.right.for_each(cb)

        # cb(self.value):
            # if self.left:
                # self.left.for_each(cb)
            # if self.right:
                # seelf.right.for_each(cb)

        stack = Stack()
        stack.push(self)

        while stack.len() > 0:
            current_node = stack.pop()
            if current_node.right:
                stack.push(current_node.right)
            if current_node.left:
                stack.push(current_node.left)
            cb(current_node.value)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        if self.value:

            # First recur on left child
            if self.left:
                self.left.in_order_print(self.left)

        # Then print the data of node
            print(self.value)

        # now recur on right child
            if self.right:
                self.right.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)
        while queue.len() > 0:
            node = queue.dequeue()
            print(node.value)
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while stack.len() > 0:
            node = stack.pop()
            print(node.value)
            if node.left:
                stack.push(node.left)
            if node.right:
                stack.push(node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT

    def pre_order_dft(self, node):
        if self.value:
            print(self.value)
            if self.left:
                self.left.pre_order_dft(self.left)
            if self.right:
                self.right.pre_order_dft(self.right)

    # Print Post-order recursive DFT

    def post_order_dft(self, node):
        if self.value:
            if self.left:
                self.left.post_order_dft(self.left)
            if self.right:
                self.right.post_order_dft(self.right)
            print(self.value)
