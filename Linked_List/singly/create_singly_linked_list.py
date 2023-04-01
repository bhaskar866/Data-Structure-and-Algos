class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

class Singly_Linked_List():
    def __init__(self):
        self.headvalue = None
        self.tail = None

List = Singly_Linked_List()
List.headvalue = Node("Mon")

el = List.headvalue

e2 = Node("Tue")

el.next = e2

List.tail = Node("Sun")

print(el.next.value)

