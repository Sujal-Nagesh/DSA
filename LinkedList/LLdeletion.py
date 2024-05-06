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

    def deleteNode(self, x):
        temp = self.head

        # If the list is empty
        if not temp:
            print("List is empty")
            return
        
        # If the node to delete is the head node
        if temp.data == x:
            self.head = temp.next
            return

        while temp.next:
            if temp.next.data == x:
                temp.next = temp.next.next  # Skip the node to delete
                return
            temp = temp.next

        print("Node not found in the linked list")

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


ll = array_to_linked_list()
ll.display()
x = int(input("Enter a value to delete: "))
ll.deleteNode(x)
ll.display()
