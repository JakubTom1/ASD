
import random

class Node:
    def __init__(self, key, value, height):
        self.key = key
        self.value = value
        self.next = [None] * height

class SkipList:

    def __init__(self, maxLevel):
        self.maxLevel = maxLevel
        self.head = Node(None, None, maxLevel)

    def __str__(self):
        output = []
        node = self.head.next[0]
        while node:
            output.append('('+str(node.key)+':'+str(node.value)+')')
            node = node.next[0]
        return ','.join(output)

    def randomLevel(self, p = 0.5):
      lvl = 1
      while random.random() < p and lvl < self.maxLevel:
            lvl = lvl + 1
      return lvl

    def search(self, key):
        current = self.head
        for i in range(self.maxLevel-1, -1, -1):
            while current.next[i] is not None and current.next[i].key < key:
                current = current.next[i]
        current = current.next[0]
        if current is not None and current.key == key:
            return current.value
        return None

    def insert(self, key, value):
        level = self.randomLevel()
        new_node = Node(key, value, level)
        current = self.head
        update = [None] * self.maxLevel
        for i in range(self.maxLevel-1, -1, -1):
            while current.next[i] is not None and current.next[i].key < key:
                current = current.next[i]
            update[i] = current
        current = current.next[0]
        if current is not None and current.key == key:
            current.value = value
        else:
            for i in range(level):
                new_node.next[i] = update[i].next[i]
                update[i].next[i] = new_node

    def remove(self, key):
        current = self.head
        update = [None] * self.maxLevel
        for i in range(self.maxLevel-1, -1, -1):
            while current.next[i] is not None and current.next[i].key < key:
                current = current.next[i]
            update[i] = current
        current = current.next[0]
        if current and current.key == key:
            for i in range(len(current.next)):
                update[i].next[i] = current.next[i]
            del current

    def displayList_(self):
        node = self.head.next[0]  # pierwszy element na poziomie 0
        keys = []  # lista kluczy na tym poziomie
        while (node != None):
            keys.append(node.key)
            node = node.next[0]

        for lvl in range(self.maxLevel - 1, -1, -1):
            print("{}: ".format(lvl), end=" ")
            node = self.head.next[lvl]
            idx = 0
            while (node != None):
                while node.key > keys[idx]:
                    print("  ", end=" ")
                    idx += 1
                idx += 1
                print("{:2d}".format(node.key), end=" ")
                node = node.next[lvl]
            print("")

if __name__ == "__main__":
    skip_list1 = SkipList(9)
    alfabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
    size = len(alfabet)
    for el in range(size):
        skip_list1.insert(el+1, alfabet[el])
    print(skip_list1)
    print(skip_list1.search(2))
    skip_list1.insert(2, 'Z')
    print(skip_list1.search(2))
    skip_list1.remove(5)
    skip_list1.remove(6)
    skip_list1.remove(7)
    skip_list1.displayList_()
    skip_list1.insert(6,'W')
    skip_list1.displayList_()

    skip_list2 = SkipList(9)
    for el in range(size):
        skip_list2.insert(size-el, alfabet[size - el-1])
    print('\n',skip_list2)
    print(skip_list2.search(2))
    skip_list2.insert(2, 'Z')
    print(skip_list2.search(2))
    skip_list2.remove(5)
    skip_list2.remove(6)
    skip_list2.remove(7)
    skip_list2.displayList_()
    skip_list2.insert(6,'W')
    print(skip_list1)
    skip_list2.displayList_()