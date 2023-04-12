class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        current_Node = self.head
        out_list = []
        while current_Node is not None:
            out_list.append(str(current_Node.data))
            current_Node = current_Node.next
        return '->' + '\n->'.join(out_list)

    def destroy(self):
        current_Node = self.head
        while current_Node is not None:
            temp_Node = current_Node
            current_Node = current_Node.next
            temp_Node = None
        self.head = None
        self.tail = None

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
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            if self.head.prev is None:
                previous_Node = Node(data)
                previous_Node.next = self.head
                self.head = previous_Node


    def append(self, data):
        if self.tail is None:
            self.tail = Node(data)
            self.head = self.tail
        else:
            if self.tail.next is None:
                previous_Node = self.tail
                self.tail = Node(data)
                self.tail.prev = previous_Node
                previous_Node.next = self.tail

    def remove(self):
        if self.tail is not None:
            to_remove_Node = self.head
            previous_Node = to_remove_Node.prev
            next_Node = to_remove_Node.next
            if previous_Node is None:
                if next_Node is None:
                    self.head = None
                    self.tail = None
                else:
                    self.head = next_Node
                    next_Node.prev = None

    def remove_end(self):
        if self.tail is not None:
            to_remove_Node = self.tail
            previous_Node = to_remove_Node.prev
            next_Node = to_remove_Node.next
            if next_Node is None:
                if previous_Node is None:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = previous_Node
                    previous_Node.next = None


if __name__ == "__main__":
    Un = [('AGH', 'Kraków', 1919),
          ('UJ', 'Kraków', 1364),
          ('PW', 'Warszawa', 1915),
          ('UW', 'Warszawa', 1915),
          ('UP', 'Poznań', 1919),
          ('PG', 'Gdańsk', 1945)]

    universities = LinkedList()

    universities.append(Un[0])
    universities.append(Un[1])
    universities.append(Un[2])
    universities.add(Un[3])
    universities.add(Un[4])
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