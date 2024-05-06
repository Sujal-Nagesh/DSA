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

Ll = LL()
Ll.head = LLnode(5)
Ll.head.next = LLnode(1)
Ll.head.next.next = LLnode(3)
Ll.head.next.next.next = LLnode(4)

Ll.display()




