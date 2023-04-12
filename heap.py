

class Element:
    def __init__(self, __dane=None, __priorytet=None):
        self.__dane = __dane
        self.__priorytet = __priorytet

    def __lt__(self, other):
        if self.__priorytet < other.__priorytet:
            return True
    def __gt__(self, other):
        if self.__priorytet > other.__priorytet:
            return True
    def __str__(self):
        return str(self.__dane) + ':' + str(self.__priorytet)

class Queue:
    def __init__(self):
        self.tab = []
        self.size = 0
    def __str__(self):
        list = []
        for el in self.tab:
            list.append(str(el))
        return list
    def left(self, idx):
        if 2 * idx + 1 > self.size-1 or idx < 0:
            return None
        else:
            return 2*idx+1

    def right(self, idx):
        if 2 * idx + 2 > self.size-1 or idx < 0:
            return None
        else:
            return 2*idx+2

    def parent(self, idx):
        p = (idx+1) // 2 - 1
        if idx < 0:
            return None
        else:
            return p

    def print_tab(self):
        print('{', end=' ')
        print(*self.tab[:self.size], sep=', ', end=' ')
        print('}')

    def print_tree(self, idx, lvl):
        if idx is not None and idx < self.size:
            self.print_tree(self.right(idx), lvl + 1)
            print(2 * lvl * '  ', self.tab[idx] if self.tab[idx] else None)
            self.print_tree(self.left(idx), lvl + 1)

    def is_empty(self):
        if self.size==0:
            return True
        else:
            return False

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.tab[0]

    def dequeue(self):
        if self.is_empty():
            return None
        if self.size == 1:
            self.size -= 1
            return self.tab[0]
        else:
            to_return = self.tab[0]
            self.tab[0], self.tab[self.size-1] = self.tab[self.size-1], self.tab[0]
            self.size -= 1
            self.repare()
            return to_return

    def repare(self, idx=0):
        right = self.right(idx)
        left = self.left(idx)
        if right is not None and self.tab[idx] < self.tab[right] and right<self.size:
            self.tab[idx], self.tab[right] = self.tab[right], self.tab[idx]
            return self.repare(right)
        if left is not None and self.tab[idx] < self.tab[left]:
            self.tab[idx], self.tab[left] = self.tab[left], self.tab[idx]
            return self.repare(left)
        if idx > 0:
            return self.repare(self.parent(idx))

    def enqueue(self, data, priority):
        new_el = Element(data, priority)
        if len(self.tab) == self.size:
            self.tab.append(new_el)
        else:
            self.tab[self.size] = new_el

        self.size += 1
        self.repare(self.size -1)

if __name__ == '__main__':
    kol_prior = Queue()
    for data, priority in zip('GRYMOTYLA', [7, 5, 1, 2, 5, 3, 4, 8, 9]):
        kol_prior.enqueue(data,priority)
    kol_prior.print_tree(0, 0)
    kol_prior.print_tab()
    remember = kol_prior.dequeue()
    print(kol_prior.peek())
    kol_prior.print_tab()
    print(remember)
    while kol_prior.is_empty() is False:
        print(kol_prior.dequeue())
    kol_prior.print_tab()