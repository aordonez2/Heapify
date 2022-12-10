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

'''def newHeapify(currentNode):
    if currentNode == None:
        return None
    #currentNode = compare_child_nodes(currentNode.left)
    #currentNode = compare_child_nodes(currentNode.right)
    #currentNode = compare_child_nodes(currentNode)
    compare_child_nodes(currentNode.left)
    compare_child_nodes(currentNode.right)
    newHeapify(currentNode.parent)
    return currentNode'''


def test_heap(rootNode):#traverses from leftmost last node to top
    if rootNode == None:
        return None
    #something here, probably inner recursive loop
    rootNode = test_inner_recursive(rootNode)
    test_heap(rootNode.parent)#do a recursive call, using parent node
    return rootNode # having the top of the tree be the final return value is probably a good idea, but not sure how to go about it

def test_inner_recursive(rootNode):#check child nodes
    if rootNode == None:
        return None
    compare_nodes_test(rootNode.left)# compare our child nodes
    compare_nodes_test(rootNode.right)
    #compare_nodes_test(rootNode.left)
    if (rootNode.parent == None):
        compare_nodes_test(rootNode)
    return rootNode


def compare_nodes_test(rootNode):
    if rootNode == None:
        return None
    if rootNode.left != None:# same as below but left before right
        if rootNode.edges > rootNode.left.edges:
            #swap_nodes(rootNode, rootNode.left)
            testing_swap(rootNode, rootNode.left)
            compare_nodes_test(rootNode.left)
    if rootNode.right != None:
        if rootNode.edges > rootNode.right.edges:
            #swap_nodes(rootNode, rootNode.right)
            testing_swap(rootNode, rootNode.right)
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
    if parent == None:
        return None
    returnVal = parent
    childL = parent.left#assume for explanation that parent = 3, L = 2, R = 1
    childR = parent.right
    if (parent.left != None):
        if (parent.edges > childL.edges):# 3 > 2
            #swap_nodes(parent, parent.left)# so now parent = 2, L = 3, r = 1
            testing_swap(parent, parent.left)
            #returnVal = parent
            #recursive call?
            compare_child_nodes(parent, parent.left)#need to ensure lower levels are still heaped
    if (parent.right != None):
        if(parent.edges > childR.edges):# 2 > 1
            #swap_nodes(parent, parent.right)# so now parent = 1, L = 3, r = 2
            testing_swap(parent, parent.right)
            #need a recursive call to check lower nodes
            compare_child_nodes(parent.right)
            #probably should move into PathNode, where it has a similar method already
            #returnVal = parent
    return returnVal

def swap_nodes(node1, node2):#probably should move into PathNode, where it has a similar method already
    #set node1's subnodes to have pointers to node2
    temp_path = node1.path
    temp_edges = node1.edges
    temp_parent = node1.parent
    node1.path = node2.path
    node1.edges = node2.edges
    node2.path = temp_path
    node2.edges = temp_edges


def testing_swap(node1, node2):
    #handle node1's parent's child pointers
    node1_is_left_child = False
    node1_is_right_child = False
    c1_p_pointer_l = None
    c1_p_pointer_r = None
    if node1.parent != None:#if node1 has a parent,
        p_pointer = node1.parent
        if p_pointer.left == node1:#and node1 is a left node;
            node1_is_left_child = True
            #p_pointer.left = None # temporarily set node 1's parent's .left to none
        elif p_pointer.right == node1:#Or if node1 is a right node,
            node1_is_right_child = True
            #p_pointer.right = None# temporarily set node 1's parent's .right to none
    #handle node1's child's parent
    if node1.left == node2:#if the node we're swapping with is on the left,
        c1_p_pointer_r = node1.right# save node1's right child
        #c1_p_pointer_r.parent = None
    elif node1.right == node2:#if the node we're swapping with is on the right,
        c1_p_pointer_l = node1.left#save node1's left child
        #c1_p_pointer_l.parent = None
    #at this point, if node1 has a child that is not node2, that child is saved

    c2_p_pointer_l = None
    c2_p_pointer_r = None

    #handle node2's child's pointers
    if node2.left != None:#if node2 has a left child,
        c2_p_pointer_l = node2.left#save that child
        #c2_p_pointer_l.parent = None
    elif node2.right != None:#if node2 has a right child,
        c2_p_pointer_r = node2.right#save that child
        #c2_p_pointer_r.parent = None
    #at this point, if node2 has children, they are saved

    #take the properties of node1 and save them
    temp_gen_left = node1.generationLeft
    temp_gen_right = node1.generationRight
    temp_is_lvl_end = node1.isLevelEnd
    temp_is_last_node = node1.isLastNode

    #assign node1's properties to node2's properties
    node1.generationLeft = node2.generationLeft
    node1.generationRight = node2.generationRight
    node1.isLevelEnd = node2.isLevelEnd
    node1.isLastNode = node2.isLastNode

    #assign node2's properties to the saved properties originally from 1
    node2.generationLeft = temp_gen_left
    node2.generationRight = temp_gen_right
    node2.isLevelEnd = temp_is_lvl_end
    node2.isLastNode = temp_is_last_node

    #save node1's pointers\
    node1_pointer_to_node2_l = None
    node1_pointer_to_node2_r = None
    temp_n1_parent = node1.parent
    if node1.left == node2:# if node2 is a left child node of node1,
        temp_n1_right = node1.right
        node1_pointer_to_node2_l = node1.left
    elif node1.right == node2:# if node2 is a right child node of node1,
        temp_n1_left = node1.left
        node1_pointer_to_node2_r = node1.right
    
    #assign node1's pointers to node2's pointers
    node1.parent = node2#otherwise we're just setting node1's parent to itself,
                        #since node2 is a child of node1
    node1.left = node2.left
    node1.right = node2.right

    #assign node2's pointers to node1's saved pointers
    node2.parent = temp_n1_parent
    if node1_pointer_to_node2_l != None:#if node2 is a left child of node1,
        node2.left = node1#set node2's left child to node1
        #might have to create 'if not none' checks here
        node2.right = temp_n1_right#set node2's right child to node1's right child if it exists
    elif node1_pointer_to_node2_r != None:#if node2 is a right child of node1,
        node2.right = node1#set node2's right child to node1
        node2.left = temp_n1_left#set node2's left child to node1's left child if it exists
    
    ####now, set all the extra node's pointers back to node1 and 2:

    #set node1's original parent and kids pointers to node2
    if node1_is_left_child == True:#if node1 was originally a left child,
        p_pointer.left = node2# set that parent's left child pointer to node2
    elif node1_is_right_child == True:#if node1 was originally a right child,
        p_pointer.right = node2# set that parent's right child pointer to node2
    if c1_p_pointer_l != None:#if node1 had a left child,
        c1_p_pointer_l.parent = node2#set that left child's parent pointer to node2
    if c1_p_pointer_r != None:#if node1 had a right child,
        c1_p_pointer_r.parent = node2#set that right child's parent pointer to node2

    #set node2's child pointers to node1
    if c2_p_pointer_l != None:#if node2 had a left child,
        c2_p_pointer_l.parent = node1#set it's parent to node1
    if c2_p_pointer_r != None:# if node2 had a right child,
        c2_p_pointer_r.parent = node1# set it's parent to node1



"""
Prints the node information from left-to-right at each level in the tree in the form specified
by the examples.
@param root Root of the whole tree to begin printing from.
"""
def print_tree_levels(rootNode, name):
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
    if rootNode == None:
        return None
    rootNode.isLevelEnd = True
    set_level_ends(rootNode.left)

def set_last_node(rootNode):
    if rootNode == None:
        return None
    if rootNode.right == None:
        rootNode.isLastNode = True
    set_last_node(rootNode.right)


def outer(rootNode, outerCount):
    if rootNode == None:
        return None
    print ("Currently at " , rootNode.path)
    inner(rootNode.right, 0, outerCount)
    print ("Currently at " , rootNode.path)
    outer(rootNode.left)
    print ("Currently at " , rootNode.path)


def inner(rootNode, count, outerCount):
    if rootNode.right == None:
        return (rootNode, count, outerCount)
    print ("Currently at " , rootNode.path)
    heldVal = inner(rootNode.right, count + 1, outerCount)
    print ("Currently at " , rootNode.path, "Inner index " , heldVal)
    #set heldVal's generation left to return of this next inner function's call?
    inner(rootNode.left, count + 1, outerCount)
    print ("Currently at " , rootNode.path)


def dual_go_out(currLeft, currRight):
    if currLeft == None or currRight == None:
        return None
    currRight.generationLeft = currLeft
    currLeft.generationRight = currRight
    dual_go_in(currLeft.right, currRight.left)

def dual_go_in(currLeft, currRight):
    if currLeft == None or currRight == None:
        return None
    if (currLeft != currRight):#if not firstrun
        currRight.generationLeft = currLeft
        currLeft.generationRight = currRight
    dual_go_out(currLeft.left, currRight.right)