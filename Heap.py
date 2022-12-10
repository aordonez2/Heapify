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
    """"This fucntion will display the values of the left chile 
            and right chile of the current node.

    Args:
        ll (linked list ): linked list that holds our PathNode onjects.
    """    """"""
    current = ll.head
    print ("current path: " , current.val.path)
    if (current.next != None):
        print ("left child node's path: " , current.val.left.path)
        print ("Right child node's path: " , current.val.right.path, "\n")

def newHeapify(currentNode):
    """Will call the compare_childes fuction then it will call itsself witht
     the value of currents parent

    Args:
        currentNode (PathNode object): the current node that were heapifying

    Returns:
        PathNode oject: the new current node whihc is the paret node of the previuse call
    """    """"""
    if currentNode == None:
        return None
    
    
    compare_child_nodes(currentNode.left)
    compare_child_nodes(currentNode.right)
    newHeapify(currentNode.parent)
    return currentNode
    #currentNode = compare_child_nodes(currentNode.left)
    #currentNode = compare_child_nodes(currentNode.right)
    #currentNode = compare_child_nodes(currentNode)
    """currentNode = rootNode #### idk if it works or not
    while (currentNode.left != None):
        currentNode = currentNode.left
    print("CurrentNode is " , str(currentNode.path))
    currentNode = currentNode.parent
    print("CurrentNode is " , str(currentNode.path))
    if (rootNode)"""


def test_heap(rootNode):#traverses from leftmost last node to top
    """This fucntion will heapify the tree.

    Args:
        rootNode (PathNode object): the root node that which will start the 
            proces of hipyfing the complete tree

    Returns:
        pathnode objcet: the new rootNode value 
    """    """"""
    if rootNode == None:
        return None
    #something here, probably inner recursive loop
    rootNode = test_inner_recursive(rootNode)
    test_heap(rootNode.parent)#do a recursive call, using parent node
    return rootNode # having the top of the tree be the final return value is probably a good idea, but not sure how to go about it

def test_inner_recursive(rootNode):#check child nodes
    """will test our inner recursive function recursibly 

    Args:
        rootNode (PathNode object): the rootNode or node that we are currently working with 


    Returns:
        PathNode object: the new nodePath object we will be working with in the recursion
    """    """"""
    if rootNode == None:
        return None
    compare_nodes_test(rootNode.left)# compare our child nodes
    compare_nodes_test(rootNode.right)
    #compare_nodes_test(rootNode.left)
    if (rootNode.parent == None):
        compare_nodes_test(rootNode)
    return rootNode

def compare_nodes_test(rootNode):
    """It will check for the new 

    Args:
        rootNode (PathNode): _description_

    Returns:
        _PathNode: _description_
    """    """"""
    if rootNode == None:
        return None
    if rootNode.left != None:# same as below but left before right
        if rootNode.edges > rootNode.left.edges:
            swap_nodes(rootNode, rootNode.left)
            compare_nodes_test(rootNode.left)
    if rootNode.right != None:
        if rootNode.edges > rootNode.right.edges:
            swap_nodes(rootNode, rootNode.right)
            compare_nodes_test(rootNode.right)
    '''if rootNode.right != None:# same as above but right before left
        if rootNode.edges > rootNode.right.edges:
            swap_nodes(rootNode, rootNode.right)
            compare_nodes_test(rootNode.right)
    if rootNode.left != None:
        if rootNode.edges > rootNode.left.edges:
            swap_nodes(rootNode, rootNode.left)
            compare_nodes_test(rootNode.left)'''

    """currentNode = rootNode #### idk if it works or not
    while (currentNode.left != None):
        currentNode = currentNode.left
    print("CurrentNode is " , str(currentNode.path))
    currentNode = currentNode.parent
    print("CurrentNode is " , str(currentNode.path))
    if (rootNode)"""

def compare_child_nodes(parent):
    """The conpare_child_node will compare the curretn nodePath Objcet left and right chile and
    id either of the right or the left is smallet than the parent node it will call the 
    fuction swap

    Args:
        parent (PathNode object): the node whos left or right children nodes we'll be checking

    Returns:
        PathNode Object: the new node path object value 
    """    """"""
    if parent == None:
        return None
    returnVal = parent
    childL = parent.left#assume for explanation that parent = 3, L = 2, R = 1
    childR = parent.right
    if (parent.left != None):
        if (parent.edges > childL.edges):# 3 > 2
            swap_nodes(parent, parent.left)# so now parent = 2, L = 3, r = 1
            returnVal = parent
            #recursive call?
    if (parent.right != None):
        if(parent.edges > childR.edges):# 2 > 1
            swap_nodes(parent, parent.right)# so now parent = 1, L = 3, r = 2
            #probably should move into PathNode, where it has a similar method already
            returnVal = parent
    return 

def swap_nodes(node1, node2):#probably should move into PathNode, where it has a similar method already
    #set node1's subnodes to have pointers to node2
    """The swap_nodes fuction will swap the data from one node to another node

    Args:
        node1 (PathNode onject): the parent node which data we'll swapping with the child node
        node2 (pathNode onject): the child node whose data we'll be swapping with the parents data 
    """    """"""
    temp_path = node1.path
    temp_edges = node1.edges
    node1.path = node2.path
    node1.edges = node2.edges
    node2.path = temp_path
    node2.edges = temp_edges
    '''if node1.left == node2:
        node1.right.parent = node2
    elif node1.right == node2:
        node1.left.parent = node2
    
    #set node1's parent to have pointers to node2
    if (node1.parent != None):
        if node1.parent.left == node1:
            node1.parent.left = node2
        elif node1.parent.right == node1:
            node1.parent.right = node2
    
    temp_left_child = node1.left
    temp_right_child = node1.right
    temp_parent = node1.parent
    temp_path = node1.path
    temp_edges = node1.edges
    temp_genLeft = node1.generationLeft
    temp_genRight = node1.generationRight
    temp_is_lvl_end = node1.isLevelEnd
    temp_is_last_node = node1.isLastNode
    if node2.left != None:#handles node2's child's pointers
        node2.left.parent = node1
    if node2.right != None:
        node2.right.parent = node1
    node1.left = node2.left
    node1.right = node2.right
    node1.parent = node2.parent
    node1.path = node2.path
    node1.edges = node2.edges
    node1.generationLeft = node2.generationLeft
    node1.generationRight = node2.generationRight
    node1.isLevelEnd = node2.isLevelEnd
    node1.isLastNode = node2.isLastNode
    node2.left = temp_left_child
    node2.right = temp_right_child
    node2.parent = temp_parent
    node2.path = temp_path
    node2.edges = temp_edges
    node2.generationLeft = temp_genLeft
    node2.generationRight = temp_genRight
    node2.isLevelEnd = temp_is_lvl_end
    node2.isLastNode = temp_is_last_node'''

def print_tree_levels(rootNode, name):
    """ Prints the node information from left-to-right at each level in the tree in the form specified
by the examples.
    Args:
        rootNode (PathNode Object):  Root of the whole tree to begin printing from
        name (file ): the file whihc we will be printing the outputs of our program

    Returns:
        string: is the outputs of our trees before and after heapyfing it 
    """    """"""
    iteration = 0
    returnString = "digraph " + name + "{\n"
    outerNode = rootNode
    while outerNode != None:
        innerNode = outerNode
        while innerNode != None:
            path = path_finding_helper(innerNode.path)
            returnString = returnString + "\t\t " + str(iteration) + "[label=\""+ str(innerNode.edges) + path + "\"];\n"
            iteration = iteration + 1
            innerNode = innerNode.generationRight
        outerNode = outerNode.left
    #print(returnString)
    outerCount = 0
    innerCount = 1
    while innerCount < iteration:
        returnString = returnString + "\t\t " + str(outerCount) + " -> " + str(innerCount) + ";\n"
        innerCount = innerCount + 1
        if (innerCount < iteration):
            returnString = returnString + "\t\t " + str(outerCount) + " -> " + str(innerCount) + ";\n"
        outerCount = outerCount + 1
        innerCount = innerCount + 1
    returnString = returnString + "}"
    return returnString

def clear_info(rootNode):# goes root, leftChild, rightChild
    """ It clreas the data from the rootNode  

    Args:
        rootNode (PathNode object: the node whos data will be clear.

    Returns:
        PathNode object: node whos data will be cleard 
    """    """"""
    if (rootNode == None):
        return None
    rootNode.generationLeft = None
    rootNode.generationRight = None
    if (rootNode.left != None):
        clear_info(rootNode.left)
    if (rootNode.right != None):
        clear_info(rootNode.right)
    return rootNode


'''def testing_formatted_print(ll, name):
    iteration = 0
    returnString = "diagraph " + name + "{\n"
    head = ll.head
    while head.next != None:
        path = path_finding_helper(head.val.path)
        returnString = returnString + "\t" + str(iteration) + "[label=\""+ str(head.val.edges) + path + "\"];\n"
        iteration = iteration + 1
        head = head.next
    returnString = returnString + "\t" + str(iteration) + "[label=\""+ str(head.val.edges) + path_finding_helper(head.val.path) + "\"];\n"
    #add bottom printout thing
    #print("Testing print output:")
    #print(returnString)
    return returnString'''

"""Given a path, return a formatted string of that path"""
def path_finding_helper(edges):
    """ return a formatted string of path of the PathNode Object object 

    Args:
        edges (string): the path of the PathNode oject whihc is a list 

    Returns:
        string: the string that represent the PathNode objects path. 
    """    """"""
    returnString = "("
    length = len(edges)
    if (length == 2):
        returnString = returnString + str(edges[0]) + ", " + str(edges[1]) + ")"
    elif (length > 2):
        i = 0
        while (i < len(edges) - 1):
            returnString = returnString + str(edges[i]) + ", "
            i = i + 1
        returnString = returnString + str(edges[i]) + ")"
    return returnString


def set_generation_links(rootNode):
    """calss helper fuctions to set the right and the left chile 
    of the current nodePath Onjec

    Args:
        rootNode (PathNode object): the current object which lef and 
        rigth chille the function will setting 

    Returns:
        None: it will reiturn None if the rootNode is equals to None 
    """    """"""
    if rootNode == None:
        return None
    dual_go_in(rootNode, rootNode)
    set_generation_links(rootNode.right)
    set_generation_links(rootNode.left)
    '''print("At " , rootNode.path)
    #cousinFinder(rootNode)
    dual_go_in(rootNode, rootNode)
    if (rootNode.right != None):
        rootNode.right.generationLeft = rootNode.left#sets current rootNode's right node's generation left
    set_generation_links(rootNode.left)
    heldNode = set_generation_links(rootNode.right)
    if heldNode != None:
        print("HeldNode " , heldNode.path)
        heldNode.generationLeft = heldNode.parent.left
    return rootNode'''

def set_level_ends(rootNode):
    """will set the level of the tree using the rootNode as the begining of the fucntion

    Args:
        rootNode (PathNOde Object): the root Node from our tree 

    Returns:
        returs: None if the node is equel to None
    """    """"""
    if rootNode == None:
        return None
    rootNode.isLevelEnd = True
    set_level_ends(rootNode.left)

def set_last_node(rootNode):
    """ looks the last node of the tree and it retirns a true if the most fardest right node in a tree.

    Args:
        rootNode (PathNode): the node we will be checking 

    Returns:
        PathNode Object: the node that is the last node.
    """    
    if rootNode == None:
        return None
    if rootNode.right == None:
        rootNode.isLastNode = True
    set_last_node(rootNode.right)


"""def outer(rootNode, outerCount):
    sends the data from the curent PathNode to the inner function.

    Args:
        rootNode (PathNond Pnject):the node whichs data well be send it to the inner fucntion
        outerCount (_type_): _description_

    Returns:
        _type_: _description_

    if rootNode == None:
        return None
    print ("Currently at " , rootNode.path)
    inner(rootNode.right, 0, outerCount)
    print ("Currently at " , rootNode.path)
    outer(rootNode.left)
    print ("Currently at " , rootNode.path)"""


"""def inner(rootNode, count, outerCount):
    if rootNode.right == None:
        return (rootNode, count, outerCount)
    print ("Currently at " , rootNode.path)
    heldVal = inner(rootNode.right, count + 1, outerCount)
    print ("Currently at " , rootNode.path, "Inner index " , heldVal)
    #set heldVal's generation left to return of this next inner function's call?
    inner(rootNode.left, count + 1, outerCount)
    print ("Currently at " , rootNode.path)"""


def dual_go_out(currLeft, currRight):
    """the dual_go_in function checks if the the currentleft is not equals to curren strigth if they are not 
    it will make them siblings as long as they share the same parent.
    Args:
        currLeft (pathNode object): it's the pathNode objects left chile 
        currRight (pathNode object): it's the pathNode objects rigth chile 

    Returns:
        it will return None if the current right or left fiels are set to None
    """    """"""
    if currLeft == None or currRight == None:
        return None
    currRight.generationLeft = currLeft
    currLeft.generationRight = currRight
    dual_go_in(currLeft.right, currRight.left)

def dual_go_in(currLeft, currRight):
    """the dual_go_in function checks if the the currentleft is not equals to curren strigth if they are not 
    it will make them siblings as long as they share the same parent.
    Args:
        currLeft (pathNode object): it's the pathNode objects left chile 
        currRight (pathNode object): it's the pathNode objects rigth chile 

    Returns:
        it will return None if the current right or left fiels are set to None
    """    """"""
    if currLeft == None or currRight == None:
        return None
    if (currLeft != currRight):#if not firstrun
        currRight.generationLeft = currLeft
        currLeft.generationRight = currRight
    dual_go_out(currLeft.left, currRight.right)

def printLN(root):
    if root.left != None:
        print("root ", root.path)
        printLN(root.left)
    else:
        print(root.path)
        
