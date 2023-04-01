class Node():
    def __init__(self,value):
        self.value = value
        self.next = None
class Singly_Linked_List():
    def __init__(self):
        self.head = None
        self.tail = None
        
    def Add_at_begaining(self,node):
        node.next = self.head
        self.head = node
        
    def Add_at_end(self,end_node):
        node  = self.head
        while(True):
            if node.next != None:
                node  = node.next
            else:
                node.next = end_node
                break
                
    def Add_in_between(self,middle_node,New_node):
        New_node.next = middle_node.next
        middle_node.next = New_node
        
    def Remove_Node(self,Node):
        Head = self.head
        node = Head
        
        if Head.value == Node.value:
            self.head = self.head.next
            return
        while(True):
            if node.next != None:
                if node.value == Node.value:
                    Prev.next = node.next
                    break
                Prev = node
                node  = node.next
            else:
                break
        
        
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

e4 = Node('Fri')

e5 = Node("Sun")

e6 = Node('new Node')

List.Add_at_begaining(e4)

List.Add_at_end(e5)

List.Add_in_between(e2,e6)

List.Remove_Node(e6)

List.print_values()