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
        self.reverse_llist()

    def reverse_llist(self):
        before = None
        current = self.head
        if current is None:
            return
        after = current.next
        while after:
            current.next = before
            before = current
            current = after
            after = after.next
        current.next = before
        self.head = current