import PathNode
import sys

class Heap:

    def __init__(self):
        self.tempPath = []

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
def build_complete_tree(indexInner, indexOuter, tp):
    indexOuter = indexOuter + 1
    if (indexOuter < len(tp)):
        tp[indexInner].left = tp[indexOuter]
    indexOuter = indexOuter + 1
    if (indexOuter < len(tp)):
        tp[indexInner].right = tp[indexOuter]
    indexInner = indexInner + 1
    if (indexInner < len(tp)):
        build_complete_tree(indexInner, indexOuter, tp)
    #else:
    return tp[0]
#def build_complete_tree(index, tempPath, ll):
    """if index > len(tempPath) - 1:
        return None
    currentNode = tempPath[index]
    #ll.add_node(currentNode)#add current to linked list
    
    #currentNode.left = build_complete_tree(index + 1, tempPath[index + 1], tempPath, ll)#set left of parent node to value of pathnode at index + 1
    #currentNode.right = build_complete_tree(index + 2, tempPath[index + 2], tempPath, ll)#set right of parent node to value of pathnode at index + 2
    if (index != len(tempPath) - 1):# if not last node
        leftIndex = (2 ** index)
        print ("Value of leftIndex: " + str(leftIndex))
        print ("Assigning left child to " + str(leftIndex))
        print ("Assigning right child to " + str(leftIndex + 1))
        currentNode.left = tempPath[leftIndex]
        #ll.add_node(tempPath[index + 1])
        ll.add_node(currentNode)
    if (index + 1 < len(tempPath) - 1):
        currentNode.right = tempPath[leftIndex + 1]
    #ll.add_node(tempPath[index + 2])
    print_ll_helper(ll)
    #new_index = index + 1
    new_indexb =  (index + 1) ** 2
    build_complete_tree(index + 1, tempPath, ll)"""
    
def print_ll_helper(ll):
    current = ll.head
    print ("current path: " , current.val.path)
    if (current.next != None):
        print ("left child node's path: " , current.val.left.path)
        print ("Right child node's path: " , current.val.right.path, "\n")
    print ("=====")

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
