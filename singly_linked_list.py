
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        current_Node = self.head
        out_list = []
        while current_Node is not None:
            out_list.append(str(current_Node.data))
            current_Node = current_Node.next
        return '->'+'\n->'.join(out_list)

    def destroy(self):
        self.head = None

    def get(self):
        if self.head is not None:
            return self.head.data

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def length(self):
        size = 0
        current_Node = self.head
        while current_Node is not None:
            current_Node = current_Node.next
            size += 1
        return size

    def add(self, data):
        current_Node = Node(data)
        current_Node.next = self.head
        self.head = current_Node

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            to_add_Node = self.head
            current_Node = self.head
            while current_Node is not None:
                to_add_Node = current_Node
                current_Node = current_Node.next
            to_add_Node.next = Node(data)

    def remove(self):
        if self.head is not None:
            self.head = self.head.next

    def remove_end(self):
        if self.head is not None:
            current_Node = self.head
            to_remove_Node = self.head
            while current_Node.next is not None:
                to_remove_Node = current_Node
                current_Node = current_Node.next
            to_remove_Node.next = None

if __name__ == "__main__":
    Un = [('AGH', 'Kraków', 1919),
     ('UJ', 'Kraków', 1364),
     ('PW', 'Warszawa', 1915),
     ('UW', 'Warszawa', 1915),
     ('UP', 'Poznań', 1919),
     ('PG', 'Gdańsk', 1945)]

    universities = LinkedList()

    '''universities.append(Un[0])
    universities.append(Un[1])
    universities.append(Un[2])
    universities.add(Un[3])
    universities.add(Un[4])'''
    universities.add(Un[5])

    print(universities)
    print(universities.length())

    universities.remove()
    print(universities.get())

    universities.remove_end()
    print(universities)

    universities.destroy()
    print(universities.is_empty())

    universities.remove()
    universities.remove_end()