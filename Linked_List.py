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