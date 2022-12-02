class Heap:
    #Temporary storage for the paths starting at tempPath[1]
    tempPath = []
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
                print (input_array[i])


    def build_complete_tree(index, parent):
        return None
