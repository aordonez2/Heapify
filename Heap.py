import PathNode
import sys
import Linked_List

class Heap:

    def __init__(self):
        self.tempPath = []
        self.ll = Linked_List.LinkedList()

    """
    Reads inputFile given at the command line and places the contents of each line into the
    path field found in each PathNode object. The order is the same as found in the text file.
    Adds the PathNode object to tempPath starting at tempPath[1].
    """
    def read_paths(self):
        with open(sys.argv[1]) as f:
            content_list = f.readlines()
        content_list = [x.strip() for x in content_list]
        for i in content_list:
            #create pathnode object from current item in content_list
            temp = i.split(" ")
            newPathNode = PathNode.PathNode(temp)
            #add that item to tempPath
            self.tempPath.append(newPathNode)




"""
Recursively builds a complete binary tree. Places PathNode objects in tempPath ArrayList into a
complete binary tree in order of appearance in the text file.

@param index Index of the current node in tempPath.
@param parent Parent of the current node.
@return A reference to the node just placed in the tree.
"""
def build_complete_tree(index, parent, tempPath):
    if parent == None:
        return None
        
    parent.left = build_complete_tree(index, tempPath[index + 1], tempPath)#set left of parent node to value of pathnode at index + 1
    parent.right = build_complete_tree(index, tempPath[index + 2], tempPath)#set right of parent node to value of pathnode at index + 2
    

"""
Recursive method that sets isLevelEnd.
param root Root of the subtree.
"""
def set_level_end(root):
    return None

"""
Recursive method that sets the "generation" link of PathNode objects from right-to-left.
generation is a term I use to indicate nodes on the same level (these may be siblings or
cousins)
@param root Root of the subtree.
"""
def setGenerationLinks( root):
    return None

    """
    Prints the node information from left-to-right at each level in the tree in the form specified
    by the examples.
    @param root Root of the whole tree to begin printing from.
    """
    def printTreeLevels( root):
        return None
