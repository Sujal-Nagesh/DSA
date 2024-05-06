class LLnode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None

    def display(self):
        elems = []
        curn = self.head
        while curn:
            elems.append(curn.data)
            curn = curn.next
        print(elems)

    def LLappend(self,x):
        
        newnode = LLnode(x)
        
        if self.head == None:
            self.head = newnode
            return

        current = self.head
        while current.next:

            current = current.next

        current.next = newnode

Ll = LL()
Ll.head = LLnode(5)
Ll.head.next = LLnode(1)
Ll.head.next.next = LLnode(3)
Ll.head.next.next.next = LLnode(4)

Ll.display()
y = int(input("Enter no. for appending : "))
Ll.LLappend(y)
Ll.display()