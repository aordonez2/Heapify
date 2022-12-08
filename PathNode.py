import Linked_List

class PathNode:

    """def __init__(self, parent, left=None, right=None):
        self.parent = parent
        self.left = left
        self.right = right"""
    def __init__(self, path):
        self.path = path
        self.edges = len(path) - 1
        self.parent = None
        self.left = None
        self.right = None
        self.generationLeft = None
        self.isLevelEnd = False
        self.isLastNode = False
    
    def swap(self, node1, node2):
        if self.left == node1:
            self.left = node2
        elif self.left == node2:
            self.left = node1
        
        if self.right == node1:
            self.right = node2
        elif self.right == node2:
            self.right = node1

    def __repr__(self):
        return( self.path, self.edges, self.parent, self.left, 
        self.right, self.generationLeft, self.isLevelEnd, self.isLastNode)
"""class PathNode:

    new_Path = Linked_List.LinkedList()
    
    def __init__(self, path, right_child, left_child, parent_node):# create a new PathNode
        self.path = path#An ArrayList of vertex IDs ordered by appearance in the path.
        self.right_child = right_child# A refrence to the right child node
        self.left_child = left_child#A refrence to the left child node
        self.parent_node = parent_node#A refrence to the parent node
        generation_left = None
        is_level_end = False
        is_last_node = False

          #
         # #
        # # #
    # Physically swapping node implementation
    def swap_current_withParent(self):
        temp_node = self.parent_node
        if (self.parent_node.right_child == self):#if this is the right child node
            temp_node.parent_node = self.parent_node#set the current node's parent to current node
            self.left_child = temp_node.left_child # set the current node's left child to the parent node's left child
            self.right_child = temp_node #move parent node into right child of parent node
        elif(self.parent_node.left_child == self):
            temp_node.parent_node = self.parent_node#set the current node's parent to current node
            self.right_child = temp_node.right_child # set the current node's right child to the parent node's right child
            self.left_child = temp_node #move parent node into left child of parent node

    #alternate swapping data implementation
    def swap_current_with_other_node_data(self, other_node):
        temp_data = other_node.data
        other_node.data = self.data
        self.data = temp_data"""