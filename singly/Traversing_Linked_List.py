class Node():
    def __init__(self,value):
        self.value = value
        self.next = None
class Singly_Linked_List():
    def __init__(self):
        self.head = None
        self.tail = None
        
    def print_values(self):
        node  = self.head
        while(True):
            print(node.value)
            if node.next != None:
                 node  = node.next
            else:
                break
        
List = Singly_Linked_List()

List.head = Node('Mon')


e2 = Node('Tue')
List.head.next = e2


e3 = Node('Wed')
e2.next = e3

List.print_values()
    