class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self, root):
        self.root = Node(root)
    
    def print_tree(self, traversal_type):
        if traversal_type == 'preorder':
            return self.preorder_print(tree.root, "")
        elif traversal_type == 'inorder':
            return self.inorder_print(tree.root, "")
        elif traversal_type == 'postorder':
            return self.postorder_print(tree.root, "")

        else:
            print('na')
        print('hello')
    
    def preorder_print(self, start, traversal):
        if start:
            if start.value == 7:
                print('hello')
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
    
    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    #        1
    #       / \
    #     2    3
    #    / \  /  \
    #   4   5 6   7

# 1-
# 1-2-
# 1-2-4
# 1-2-4-5-3-6-7

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
# print(tree.print_tree('preorder')) #1-2-4-5-3-6-7-
# print(tree.print_tree('inorder')) #4-2-5-1-6-3-7-
# print(tree.print_tree('postorder')) #4-5-2-6-7-3-1-
#depth-first: in-order, pre-order, post-order


class Node:
    # A utility function to create a new node
    def __init__(self ,key):
        self.data = key
        self.left = None
        self.right = None
    def __repr__(self):
        return repr(self.data)
 
# Iterative Method to print the 
# height of a binary tree
def printLevelOrder(root):
    # Base Case
    if root is None:
        return
     
    # Create an empty queue 
    # for level order traversal
    queue = []
 
    # Enqueue Root and initialize height
    queue.append(root)
 
    while(len(queue) > 0):
       
        # Print front of queue and 
        # remove it from queue
        print (queue[0].data)
        node = queue.pop(0)
 
        #Enqueue left child
        if node.left is not None:
            queue.append(node.left)
 
        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)
 
#Driver Program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
print ("Level Order Traversal of binary tree is -")
printLevelOrder(root)
#This code is contributed by Nikhil Kumar Singh(nickzuck_007)