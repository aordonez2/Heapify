import PathNode
import sys

class Heap:
    """
    Reads inputFile given at the command line and places the contents of each line into the
    path field found in each PathNode object. The order is the same as found in the text file.
    Adds the PathNode object to tempPath starting at tempPath[1].
    """
    def read_paths():
        tempPath = []
        with open(sys.argv[1]) as f:
            content_list = f.readlines()
        content_list = [x.strip() for x in content_list]

        for i in content_list:
            #create pathnode object from current item in content_list
            temp = i.split(" ")
            newPathNode = PathNode.PathNode(temp)
            #add that item to tempPath
            tempPath.append(newPathNode)
        print (tempPath)
        
    """
    Recursively builds a complete binary tree. Places PathNode objects in tempPath ArrayList into a
    complete binary tree in order of appearance in the text file.

    @param index Index of the current node in tempPath.
    @param parent Parent of the current node.
    @return A reference to the node just placed in the tree.
    """
    def build_complete_tree(index, parent):
        #create a new tree
        #for every element in tempPath call insert function
        return None

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
