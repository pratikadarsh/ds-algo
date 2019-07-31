''' Class definition for single linked list.'''


class Linked_List():


    def __init__(self, element=None):
        self.head = element


    def display(self):

        if self.head:
            current = self.head
            while current:
                print(current.value)
                current = current.next
        else:
            print("Linked list empty !")


    def append(self, element):
        
        if self.head == None:
            self.head = element
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = element


    def insert_pos(self, position, element):

        if self.head:
            if position == 1:
                element.next = self.head.next
                self.head = element
            else:
                counter = 1
                current = self.head
                while counter < position -1:
                    counter += 1
                    current = current.next
                element.next = current.next
                current.next = element
        else:
            pass


    def insert_first(self, element):

        if self.head:
            element.next = self.head
            self.head = element
        else:
            self.head = element

    def delete(self, value):

        if self.head:
            current = self.head
            previous = current
            while current:
                if current.value == value:
                    previous.next = current.next
                    break
                else:
                    previous = current
                    current = current.next
            del(current)
        else:
            print("List is Empty")

    def delete_first(self):
        
        if self.head:
            first = self.head
            self.head = first.next
            del(first)
        else:
            print("List is Empty")

    def delete_last(self):
        
        if self.head:
            current = self.head
            previous = current
            while current.next:
                previous = current
                current = current.next
            previous.next = None
            del(current)
        else:
            print("List is Empty")
