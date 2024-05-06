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

Ll = LL()
Ll.head = LLnode(5)
Ll.head.next = LLnode(1)
Ll.head.next.next = LLnode(3)
Ll.head.next.next.next = LLnode(4)

Ll.display()
x = int(input("Enter a value to delete: "))
Ll.deleteNode(x)
Ll.display()




    # def compare(self, c1):
    #     for i in range


    
    # def append(self,data):
    #     new_node = LLnode(data)
    #     cur = self.head
    #     while cur.next != None:
    #         cur = cur.next
    #     cur.next = new_node