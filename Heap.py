import PathNode
import sys

class Heap:

    """
    Reads inputFile given at the command line and places the contents of each line into the
    path field found in each PathNode object. The order is the same as found in the text file.
    Adds the PathNode object to tempPath starting at tempPath[1].
    """
    def read_paths():

        print("were here!")
        with open(sys.argv[1]) as f:
            content_list = f.readlines()
        """try:
            fielName = input("\nEnter Fiel Name: ")
            
            with open(fielName) as f:
                content_list = f.readlines()

            # remove new line characters
            content_list = [x.strip() for x in content_list]
            ##obj.read_paths(content_list)
            Heap.Heap.read_paths(content_list)
            ##Heap.read_paths(content_list)
            print("Here")
            return content_list 
            except:
            print('\n\n\nYou have entered an invalid File Name.\n\n\n')"""
        content_list = [x.strip() for x in content_list]

        print(content_list)
        
    """
    Recursively builds a complete binary tree. Places PathNode objects in tempPath ArrayList into a
    complete binary tree in order of appearance in the text file.

    @param index Index of the current node in tempPath.
    @param parent Parent of the current node.
    @return A reference to the node just placed in the tree.
    """

    def build_complete_tree(index, parent):
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
