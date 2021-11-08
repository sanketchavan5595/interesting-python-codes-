print('Hello World')
class Node:
    def __init__(self, data):
        self.data = data
        self.next  = None 
    

node1 = Node(1)
node2 = Node(2)
node1.next = node2
