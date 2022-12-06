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


"""class Linked_List:

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    
    def __init__(self):
        self.head = None
        self.last_node = None
    
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            self.last_node.next = new_node
            self.last_node = new_node

    def remove(self, data):
        if self.head is None:
            raise Exception ("can't remove item, empty list")
        else:
            current_node = self.head
            while current_node.next.data != None:
                if current_node.next.data == data:
                    current_node.next = current_node.next.next

    def myPrint():
        print("Inside LL")"""