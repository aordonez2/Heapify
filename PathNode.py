import Linked_List

class PathNode:
    def __init__(self, path):
        self.path = path
        self.edges = len(path) - 1
        self.parent = None
        self.left = None
        self.right = None
        #Reference to the node directly to the left on the same tree level. */
        #Alternatively you could do generationRight instead going to the right
        self.generationLeft = None
        self.generationRight = None
        self.isLevelEnd = False
        self.isLastNode = False
    
    def swap(self, node1, node2):
        temp = node1
        temp1L = node1.left
        temp1R = node1.right
        temp1P = node1.parent
        temp1LP = node1.left.parent # can we just use node1?
        temp1RP = node1.right.parent
        if node1.parent.left.path == node1.path:
            temp1PC = node1.parent.L
        elif node1.parent.right.path == node1.path:
            temp1PC = node1.parent.R

        #saving node1 pointers done, assign node2 pointers to node1
        node1.left = node2.left
        node1.right = node2.right
        node1.parent = node2.parent
        #do parent/child pointers
        node1.left.parent = node2
        node1.right.parent = node2

        node1.parent = node2.parent
        if (node1.parent != None):
            if (node1.parent.left.path == node1.path):
                node1.parent.left = node2
            elif (node1.parent.right.path == node1.path):
                node1.parent.right = node2

        #applying tempNode pointers to node2
        node2.left = temp1L
        node2.right = temp1R
        node2.parent = temp
        if (node2.left != None):
            node2.left.parent = temp1LP
        if (node2.right != None):
            node2.right.parent = temp1RP
        '''if self.left == node1:
            self.left = node2
        elif self.left == node2:
            self.left = node1
        
        if self.right == node1:
            self.right = node2
        elif self.right == node2:
            self.right = node1'''
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