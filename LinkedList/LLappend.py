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

    
    def LLappend(self, x):
        newnode = LLnode(x)
        
        if self.head is None:
            self.head = newnode
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = newnode


def array_to_linked_list():
    input_array = input("Enter the elements of the array separated by spaces: ").split()
    ll = LL()
    for element in input_array:
        ll.LLappend(int(element))
    return ll

Ll = LL()

ll = array_to_linked_list()
ll.display()

y = int(input("Enter no. for appending : "))
ll.LLappend(y)
ll.display()