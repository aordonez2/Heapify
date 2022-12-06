import Linked_List
import PathNode

class Heap:

    """
    Reads inputFile given at the command line and places the contents of each line into the
    path field found in each PathNode object. The order is the same as found in the text file.
    Adds the PathNode object to tempPath starting at tempPath[1].
    """
    def read_paths(input_array):
        if (len(input_array) == 0):
            raise Exception ("Can't find input file or input file is empty")
        else:
            for i in input_array:
                print ("Placeholder for loop printing out everything being passed to read_paths")
                # create a new pathnode
                newPathNode = PathNode(i, i[2], i[0], i[1])
                print (newPathNode)

    def build_complete_tree(index, parent):
        return None

    def go():
        #Temporary storage for the paths starting at tempPath[1]
        tempPath = Linked_List.LinkedList()
        blankNode = Linked_List.Node()
        tempPath.add_node(blankNode)#fill in slot one so that we start at tempPath[1]

        fileName = input("\nEnter File Name:")
        with open(fileName) as f:
            content_list = f.readlines()

        # remove new line characters
        content_list = [x.strip() for x in content_list]
        print(content_list)#raw list of paths

        for i in content_list: # for every path in the content list,
            # create a new pathnode object from current path in content list
            newPathNode = PathNode.PathNode()
            #then add that pathnode to a list of nodes
            tempPath.add_node(newPathNode)
        
        build_complete_tree(1, tempPath)#create a heap from all built pathnode objects
