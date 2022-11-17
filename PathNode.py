class PathNode:
    #An ArrayList of vertex IDs ordered by appearance in the path.
    path = null
    # A refrence to the left child node
    right_child = null
    #A refrence to the right child node
    left_child = null
    #A refrence to the parent node
    parent_node = null
    #Reference to the node directly to the left on the same tree level.
    generation_left = null
    #True if the node is last in the level
    is_level_end = False
    #True if the node is the right-most node in the last level.
    is_last_node = False
    
    def __init__(self, path, right_child, left_child, parent_node):
        self.path = path
        self.right_child = right_child
        self.left_child = left_child
        self.parent_node = parent_node