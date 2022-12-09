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
        tp[indexInner].left.parent = tp[indexInner]
    indexOuter = indexOuter + 1
    if (indexOuter < len(tp)):
        tp[indexInner].right = tp[indexOuter]
        tp[indexInner].right.parent = tp[indexInner]
    indexInner = indexInner + 1
    if (indexInner < len(tp)):
        build_complete_tree(indexInner, indexOuter, tp)
    #else:
    return tp[0]
    
def print_ll_helper(ll):
    current = ll.head
    print ("current path: " , current.val.path)
    if (current.next != None):
        print ("left child node's path: " , current.val.left.path)
        print ("Right child node's path: " , current.val.right.path, "\n")
    print ("=====")

def heapify(rootNode):
    print ("Current node: " , str(rootNode.path))#### almost works, right side of tree messed up
    if rootNode.left != None:
        if (compare_child_nodes(rootNode) == "left"):
            heapify(rootNode.left)
    if (rootNode.right != None):
        if (compare_child_nodes(rootNode) == "right"):
            heapify(rootNode.right)
    if (rootNode.left == None and rootNode.right == None):
        return None
    if (rootNode.parent != None):
        heapify(rootNode.parent)


    """currentNode = rootNode #### idk if it works or not
    while (currentNode.left != None):
        currentNode = currentNode.left
    print("CurrentNode is " , str(currentNode.path))
    currentNode = currentNode.parent
    print("CurrentNode is " , str(currentNode.path))
    if (rootNode)"""
def compare_child_nodes(parent):
    returnVal = "NA"
    childL = parent.left#assume for explanation that parent = 3, L = 2, R = 1
    childR = parent.right
    if (parent.edges > childL.edges):# 3 > 2
        swap_nodes(parent, parent.left)# so now parent = 2, L = 3, r = 1
        returnVal = "left"
        #recursive call?
    if(parent.edges > childR.edges):# 2 > 1
        swap_nodes(parent, parent.right)# so now parent = 1, L = 3, r = 2
        returnVal = "right"
    return returnVal

def swap_nodes(node1, node2):
    heldPath = node1.path
    heldEdges = node1.edges
    node1.path = node2.path
    node1.edges = node2.edges
    node2.path = heldPath
    node2.edges = heldEdges
'''def swap_nodes(node1, node2):
    tempNode = node1
    node1.path = node2.path
    node1.edges = len(node1.path) - 1
    node1.parent = node2.parent
    node1.left = node2.left
    node1.right = node2.right
    if node1.generationLeft != None:
        node1.generationLeft = node2.generationRight
    if node1.isLevelEnd != None:
        node1.isLevelEnd = node2.isLastLevel
    if node1.isLastNode != None:
        node1.isLastNode = node2.isLastNode

    node2.path = tempNode.path
    node2.edges = len(node2.path) - 1
    node2.parent = tempNode.parent
    node2.left = tempNode.left
    node2.right = tempNode.right
    if node1.generationLeft != None:
        node2.generationLeft = tempNode.generationRight
    node2.isLevelEnd = tempNode.isLastLevel
    node2.isLastNode = tempNode.isLastNode'''

"""
Recursive method that sets isLevelEnd.
param root Root of the subtree.
"""
def set_level_ends(rootNode):
    if rootNode.left == None:
        return None
    set_level_ends(rootNode.left)
    rootNode.isLevelEnd = True
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
