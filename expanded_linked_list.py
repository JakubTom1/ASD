
class El_of_LinkedList:
    def __init__(self, size=6):
        self.tab = [None for i in range(size)]
        self.num_of_el = 0
        self.size = size
        self.next = None

    def insert(self,idx,data):
        for i in range(self.num_of_el, idx, -1):
            self.tab[i] = self.tab[i-1]
        self.tab[idx] = data
        self.num_of_el += 1

    def delete(self, idx):
        for i in range(idx, self.num_of_el):
            self.tab[i] = self.tab[i + 1]
        self.num_of_el -= 1

class UnrolledLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __str__(self):
        current_Node = self.head

        out_list = []
        while current_Node is not None:
            el_list = []
            for el in current_Node.tab:
                if el is not None:
                    el_list.append(str(el))
            out_list.append(str("[" + ", ".join(el_list) + "]"))
            current_Node = current_Node.next
        return '->' + '\n ->'.join(out_list)

    def get(self,idx):
        current = self.head
        while idx >= current.num_of_el:
            idx -= current.num_of_el
            current = current.next
        return current.tab[idx]

    def __len__(self):
        size = 0
        current = self.head
        while current is not None:
            current = current.next
            size += 1
        return size

    def insert(self, idx, data):
        if self.head is None:
            self.head = El_of_LinkedList()
            self.head.tab[0] = data
            self.head.num_of_el = 1
            self.tail = self.head
            return

        current = self.head
        prev = None
        while idx > current.num_of_el:
            idx -= current.num_of_el
            prev = current
            current = current.next

        if current.num_of_el < current.size:
            current.insert(idx, data)
        else:
            new_element = El_of_LinkedList()
            half = current.size//2
            for i in range(current.size):
                if i >= half:
                    new_element.tab[i-half] = current.tab[i]
                    current.tab[i] = None
            new_element.num_of_el = half
            current.num_of_el = current.size - half
            if idx >= current.size:
                new_element.tab[half] = data
                new_element.num_of_el += 1
                new_element.next = current.next
                current.next = new_element
            else:
                idx -= new_element.num_of_el
                new_element.insert(idx, data)
                new_element.next = current.next
                current.next = new_element

            if self.tail == current:
                self.tail = new_element

    def delete(self, idx):
        current = self.head
        prev = None
        half = current.size//2
        while idx >= current.num_of_el:
            idx -= current.num_of_el
            prev = current
            current = current.next
        current.delete(idx)
        if current.num_of_el < half:
            next_el = current.next
            current.tab[half-1] = next_el.tab[0]
            next_el.delete(0)
            if next_el.num_of_el < half:
                for i in range(next_el.num_of_el):
                    current.tab[half+i] = next_el.tab[i]
                current.next = next_el.next

if __name__ == "__main__":
    linked_list = UnrolledLinkedList()
    for el in range(9):
        data = el+1
        linked_list.insert(el, data)
    print(linked_list.get(4))
    linked_list.insert(1, 10)
    linked_list.insert(8, 11)
    print("\n", linked_list)
    linked_list.delete(1)
    linked_list.delete(2)
    print("\n", linked_list)