
class Queue:
    def __init__(self, size=5):
        self.tab = [None for i in range(size)]
        self.size = size
        self.read_space = 0
        self.save_space = 0

    def __str__(self):
        outlist = []
        for el in range(self.size):
            if self.tab[el] is not None:
                outlist.append(str(self.tab[el]))
        return "[" + ", ".join(outlist) + "]"

    def realloc(self, current_idx):
        oldSize = self.size
        new_size = 2 * oldSize

        new_tab = [None for i in range(new_size)]
        for el in range(oldSize):
            if el >= current_idx:
                new_tab[oldSize + el] = self.tab[el]
            else:
                new_tab[el] = self.tab[el]

        self.tab = new_tab
        self.read_space += oldSize
        self.save_space = current_idx
        self.size = new_size
        return self.tab

    def is_empty(self):
        return self.read_space == self.save_space

    def peek(self) -> object:
        if self.is_empty():
            return None
        else:
            return self.tab[self.read_space]


    def dequeue(self):
        if self.read_space == self.save_space:
            return None
        else:
            throwback = self.tab[self.read_space]
            self.tab[self.read_space] = None
            self.read_space = (self.read_space + 1) % self.size
            return throwback


    def enqueue(self, data):
        self.tab[self.save_space] = data
        if self.save_space + 2 > self.size:
            self.save_space = 0
        else:
            self.save_space += 1


        if self.save_space == self.read_space:
            current_idx = self.read_space
            self.tab = self.realloc(current_idx)

    def print_tab(self):
        return str(self.tab)

if __name__ == '__main__':
    queue = Queue()
    for element in [1,2,3,4]:
        queue.enqueue(element)
    print(queue.dequeue())
    print(queue.peek())
    print(queue)
    for element in [5,6,7,8]:
        queue.enqueue(element)
    print(queue.print_tab())
    while queue.is_empty() is False:
        print(queue.dequeue())
    print(queue)