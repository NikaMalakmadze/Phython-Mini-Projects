
import random

# class for nodes
class Node:

    # each node have:
    #   value
    #   right/left child
    #   level of depth
    #   its parent
    def __init__(self, value, depth, parent):
        self.value = value
        self.right = None
        self.left = None
        self.depth = depth
        self.parent = parent

    def __str__(self):
        return str(self.value)          # return node's value as an string form of node objects

# class of Binary Seacrh Tree
class BST:

    # binary tree have root node
    # starting depth as 0
    # array of its nodes
    def __init__(self):
        self.root = None
        self.depth = 0
        self.nodes = []

    # method to insert node in binary tree
    def insert(self, value):
        # if theres no root element 
        if self.root is None:
            self.root = Node(value, self.depth + 1, None)       # then make it root of binary tree
            self.nodes.append(self.root)                            # append it in nodes array
        else:                                                       
            self.insert_recursively(self.root, value, self.root.depth + 1)      # if not start inserting recursively

    # recursive method thats insert nodes in binary tree
    def insert_recursively(self, node, value, depth):
        # check where should node go
        # if its value is less then parent node's value then it goes as left child
        if value < node.value:
            if node.left is None:                           # if node has not left child
                node.left = Node(value, depth, node)            # then its left child is new node with this value
                self.nodes.append(node.left)                        # append it to nodes array
            else:
                # if left child already exists, then call function for that left child                                               
                self.insert_recursively(node.left, value, depth + 1)    
        # if its value is greater or equal to parent node's value then it goes as right child
        elif value > node.value or value == node.value:
            if node.right is None:                          # if node has not left child
                node.right = Node(value, depth, node)           # then its right child is new node with this value
                self.nodes.append(node.right)                       # append it to nodes array
            else:
                # if right child already exists, then call function for that right child
                self.insert_recursively(node.right, value, depth + 1)

    # function to seacrh node with inputed value
    #  it calls recursive function
    def search(self, value):
        return self.search_recursively(self.root, value)

    def search_recursively(self, node, value):
        if node is None or node.value == value:                 # return node if value was finded or node is None(not finded)
            return node
        if value < node.value:                                      # if inputed value is less then its parent node's value
            return self.search_recursively(node.left, value)            # visit left child of node
        else:
            return self.search_recursively(node.right, value)           # visit right child of node
    
    # simple method that returns total num of nodes in binary tree
    def nodes_count(self):
        return len(self.nodes)

    # simple method that returns size of binary tree
    def tree_depth(self):
        return max([node.depth for node in self.nodes])

    # simple method that returns node with biggest value
    def max_node(self):
        return max([node.value for node in self.nodes])

    # simple method that returns node with smallest value
    def min_node(self):
        return min([node.value for node in self.nodes])
    
    # simple method that returns nodes with smallest and biggest value as an tuple
    def min_max_node(self):
        return (self.min_node(), self.max_node())

    # simple function that returns parent node of node with inputed value
    def get_parent_of(self, value):
        get_node = [node for node in self.nodes if node.value == value]
        if get_node:
            return get_node[0].parent
        return None

    # method for inorder_traversal
    def inorder_traversal(self):
        result = []
        self._inorder_traversal_recursively(self.root, result)
        return result

    def _inorder_traversal_recursively(self, node, result):
        if node:
            self._inorder_traversal_recursively(node.left, result)      # Left subtree first
            result.append(node.value)                                   # Then root
            self._inorder_traversal_recursively(node.right, result)     # Then right

    # method for preorder_traversal
    def preorder_traversal(self):
        result = []
        self._preorder_traversal_recursively(self.root, result)
        return result

    def _preorder_traversal_recursively(self, node, result):
        if node:
            result.append(node.value)                                   # Visit root first
            self._preorder_traversal_recursively(node.left, result)     # Then left
            self._preorder_traversal_recursively(node.right, result)    # Then right

    # method for postorder_traversal
    def postorder_traversal(self):
        result = []
        self._postorder_traversal_recursively(self.root, result)
        return result

    def _postorder_traversal_recursively(self, node, result):
        if node:
            self._postorder_traversal_recursively(node.left, result)    # Left subtree first
            self._postorder_traversal_recursively(node.right, result)   # Right subtree
            result.append(node.value)                                   # Visit root last

bst = BST()

# add 20 random nodes in binary tree
values = random.sample(range(1, 101), 20)
for value in values:
    bst.insert(value)

print(bst.root)
print(bst.min_node())
print(bst.max_node())
print(bst.tree_depth())
print(bst.nodes_count())
print(bst.min_max_node())
print(bst.inorder_traversal())
print(bst.preorder_traversal())
print(bst.postorder_traversal())
print(bst.search(random.randint(1,120)))