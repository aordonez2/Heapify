class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Define the Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # This method adds a new node to the Linked List
    def add_node(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
    
    def create_Linked_list(self, tp):
        i = 0
        while i < len(tp):
            self.add_node(tp[i])
            i = i + 1


'''def create_linked_list(root,ll):
    if not root:
        # base case: the tree is empty, so there is no linked list to create
        return None

    # create a linked list node with the value of the current tree node
    head = Node(root)
    print("Current node: " , str(head.val.path))
    if (head.val.left != None):
        print ("Value of current node's left: ", str(head.val.left.path))
    if (head.val.left != None):
        print ("Value of current node's right: ", str(head.val.right.path))
    ll.add_node(root)

    # create the rest of the linked list by recursively calling the function
    # with the left and right subtrees of the current tree node
    head.next = create_linked_list(root.left, ll)
    head.next = create_linked_list(root.right, ll)

    return head'''