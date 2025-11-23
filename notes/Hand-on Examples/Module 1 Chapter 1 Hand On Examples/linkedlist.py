class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating nodes
node1 = Node(1)
node2 = Node(2)
node1.next = node2

# Traverse
current = node1
while current:
    print(current.data)
    current = current.next
