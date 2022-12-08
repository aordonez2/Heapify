import Heap
import sys
import Linked_List

##obj = Heap.Heap()
##from Heap import read_paths

def main():
    myHeap = Heap.Heap()
    myHeap.read_paths()
    rootNode = Heap.build_complete_tree(0, 0, myHeap.tempPath)
    ll = Linked_List.LinkedList()
    ll.create_Linked_list(myHeap.tempPath)
    print ("Seperates here")
    print_ll_helper(ll.head)
    print ("Stop here")
    #myHeap.build_tempPath_helper(myHeap.tempPath, content_list) 

def print_ll_helper(head):
    while head.next != None:
        print("Path of current Node: " ,  str(head.val.path))
        if (head.val.left != None):
            print ("Left node's path: ", str(head.val.left.path))
        if (head.val.right != None):
            print ("Right node's path: " , str(head.val.right.path))
        print()
        head = head.next



if __name__=="__main__":
    main()
