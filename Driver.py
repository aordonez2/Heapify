import Heap
import sys
import Linked_List

##obj = Heap.Heap()
##from Heap import read_paths

def main():
    myHeap = Heap.Heap()
    myHeap.read_paths()
    rootNode = Heap.build_complete_tree(0, 0, myHeap.tempPath)#create an unsorted binary tree from the tempPath
    Heap.set_generation_links(rootNode)
    returnVal = Heap.print_tree_levels(rootNode, sys.argv[2] + "before" )
    print (returnVal)

    Heap.set_level_ends(rootNode)#set the level end fields
    Heap.set_last_node(rootNode)#set last node (bottom right)

    f = open(sys.argv[2] + "before.dot", "w")
    f.write(returnVal)
    f.close()
    
    currentNode = rootNode
    while (currentNode.left != None):#walk to last node on left
        currentNode = currentNode.left
    #rootNode = Heap.newHeapify(currentNode.parent)#heapifies the tree starting from the last leftmost node that is not a leaf
    rootNode = Heap.test_heap(currentNode)
    currentNode = rootNode
    while (currentNode.parent != None):#walk back up to the top
        currentNode = currentNode.parent
    rootNode = currentNode

    Heap.clear_info(rootNode)#clears out genleft/right, isLevelEnd and isLastNode
    #we only need to call clear_info if we're swapping out node data and not the physical nodes
    returnVal = Heap.print_tree_levels(rootNode, sys.argv[2] + "after")
    #while loop that walks back up to the top via parent nodes?
    print (returnVal)

    f = open(sys.argv[2] + "after.dot", "w")
    f.write(returnVal)
    f.close()

    Heap.set_level_ends(rootNode)#set the level end fields
    Heap.set_last_node(rootNode)#set last node (bottom right)

def placeHolder_trav(rootNode):# goes root, leftChild, rightChild
    if (rootNode == None):
        return None
    print("At node: " , str(rootNode.path))
    if (rootNode.left != None):
        placeHolder_trav(rootNode.left)
    if (rootNode.right != None):
        placeHolder_trav(rootNode.right)
    return rootNode

def test_trav(rootNode):#I think does same thing
    print("Current Node: ", rootNode.path)
    if (rootNode.left != None):
        print("Going left to ", rootNode.left.path, "From ", rootNode.path)
        test_trav(rootNode.left)
    print("Now at ", rootNode.path)
    if (rootNode.right != None):
        print("Going right to ", rootNode.right.path, "From ", rootNode.path)
        test_trav(rootNode.right)
    print ("Now at ", rootNode.path)


def test_print(rootNode):
    currentNode = rootNode
    level = 0
    #left trav, gets the height of the leftmost side
    print(currentNode.path)
    while currentNode.left != None:
        currentNode = currentNode.left
        level = level + 1
        print("On level " + str(level))
        print(currentNode.path)
    
    testNode = rootNode
    j = 0
    print ("Currently at: " , testNode.path)
    for j in range (level):
        testNode = testNode.right
        print ("Currently at: " , testNode.path)

def level_printer(ll):#needs to be done inside heap and with the rootNode
    '''starts at the begining of the linked list and prints out levels'''
    head = ll.head
    while (head.next != None):
        print (head.val.path)
        head = head.next
    print (head.val.path)


if __name__=="__main__":
    main()
