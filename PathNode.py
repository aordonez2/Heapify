import Linked_List

Linked_List.Linked_List.myPrint()

class PathNode:
    
    def __init__(self, path, right_child, left_child, parent_node, data):# create a new PathNode
        self.path = path#An ArrayList of vertex IDs ordered by appearance in the path.
        self.right_child = right_child# A refrence to the right child node
        self.left_child = left_child#A refrence to the left child node
        self.parent_node = parent_node#A refrence to the parent node
        self.data = data
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
        self.data = temp_data