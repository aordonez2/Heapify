class PathNode:
    #An ArrayList of vertex IDs ordered by appearance in the path.
    path = None
    # A refrence to the left child node
    left_child = None
    #A refrence to the right child node
    right_child = None
    #A refrence to the parent node
    parent_node = None
    #Reference to the node directly to the left on the same tree level.
    generation_left = None
    #True if the node is last in the level
    is_level_end = False
    #True if the node is the right-most node in the last level.
    is_last_node = False
    
    def __init__(self, path, right_child, left_child, parent_node, data):# create a new PathNode
        self.path = path
        self.right_child = right_child
        self.left_child = left_child
        self.parent_node = parent_node
        self.data = data

          #
         # #
        # # #
    #physically swapping node implementation
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
        self.data = temp_data
        
        
    def __repr__(self):
        return( self.path, self.edges, self.parent, self.left, 
        self.right, self.generationLeft, self.isLevelEnd, self.isLastNode)
