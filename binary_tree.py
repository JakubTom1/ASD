

class Node:
    def __init__(self, key=None, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    def print_tree(self):
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")

    def __print_tree(self, node, lvl):
        if node != None:
            self.__print_tree(node.right, lvl + 5)

            print()
            print(lvl * " ", node.key, node.value)

            self.__print_tree(node.left, lvl + 5)

    def print(self):
        output = []
        list = self.__print(self.root, [])
        for el in list:
            output.append(' '.join([str(i) for i in el]))
        return ','.join(output)

    def __print(self, node, list):
        if node is not None:
            self.__print(node.left, list)
            list.append([node.key, node.value])
            self.__print(node.right, list)
            return list
    def search(self, k, current_Node=None):
        if current_Node is None:
            return self.search(k, self.root)
        elif current_Node.key == k:
            data = current_Node.value
            return data
        elif k < current_Node.key:
            if current_Node.left is not None:
                return self.search(k, current_Node.left)
            else:
                print("Brak danej o podanym kluczu")
                return None
        else:
            if current_Node.right is not None:
                return self.search(k, current_Node.right)
            else:
                print("Brak danej o podanym kluczu")
                return None
    def insert(self, k, data, current_Node=None):
        if self.root is None:
            self.root = Node(k, data)
        elif current_Node is None:
            return self.insert(k, data, self.root)
        elif current_Node.key == k:
            current_Node.value = data
        elif k < current_Node.key:
            if current_Node.left is not None:
                return self.insert(k, data, current_Node.left)
            else:
                current_Node.left = Node(k, data)
        else:
            if current_Node.right is not None:
                return self.insert(k, data, current_Node.right)
            else:
                current_Node.right = Node(k, data)

    def delete(self, k, current_Node=None, parent=None):
        if current_Node is None:
            return self.delete(k, self.root)
        if k < current_Node.key:
            if current_Node.left is not None:
                return self.delete(k, current_Node.left, current_Node)
            else:
                print("Brak danej o podanym kluczu")
                return None
        if k > current_Node.key:
            if current_Node.right is not None:
                return self.delete(k, current_Node.right, current_Node)
            else:
                print("Brak danej o podanym kluczu")
                return None
        else:
            if (current_Node.left is None) and (current_Node.right is None):
                if parent is None:
                    self.root = None
                elif parent.left == current_Node:
                    parent.left = None
                else:
                    parent.right = None

            elif (current_Node.left is None) or (current_Node.right is None):
                if current_Node.right is not None:
                    if parent.left == current_Node:
                        parent.left = current_Node.right
                    else:
                        parent.right = current_Node.right
                else:
                    if parent.left == current_Node:
                        parent.left = current_Node.left
                    else:
                        parent.right = current_Node.left
            else:
                successor_node = current_Node.right
                parent_successor = current_Node
                while successor_node.left is not None:
                    parent_successor = successor_node
                    successor_node = successor_node.left
                    
                current_Node.key = successor_node.key
                current_Node.value = successor_node.value
                if parent_successor.right == successor_node:
                    parent_successor.right = successor_node.right
                else:
                    parent_successor.left = successor_node.right

    def hight(self, k=None, current_Node=None):
        if current_Node is None:
            return self.hight(k, self.root)
        if k is None:
            k=self.root.key
            return self.hight(k,current_Node)
        elif current_Node.key == k:
            new_list=[]
            list_of_tree = self.__print(current_Node, [])
            for key, value in list_of_tree:
                new_list.append(self.__hight(key, current_Node, 0))
            return max(new_list)
        elif k < current_Node.key:
            if current_Node.left is not None:
                return self.hight(k, current_Node.left)
            else:
                print("Brak danej o podanym kluczu")
                return None
        else:
            if current_Node.right is not None:
                return self.hight(k, current_Node.right)
            else:
                print("Brak danej o podanym kluczu")
                return None

    def __hight(self, k, node, size):
        if node.key == k:
            size += 1
            return size
        elif k < node.key:
            if node.left is not None:
                size += 1
                return self.__hight(k, node.left, size)
        else:
            if node.right is not None:
                size += 1
                return self.__hight(k, node.right, size)
if __name__ == '__main__':
    bst=BST()
    dict = {50:'A', 15:'B', 62:'C', 5:'D', 20:'E', 58:'F', 91:'G', 3:'H', 8:'I', 37:'J', 60:'K', 24:'L'}
    for key, value in dict.items():
        bst.insert(key,value)
    bst.print_tree()
    print(bst.print())
    print("Wartość dla klucza '{}' wynosi '{}'".format(24, bst.search(24)))
    bst.insert(20, 'AA')
    bst.insert(6, 'M')
    bst.delete(62)
    bst.insert(59, 'N')
    bst.insert(100, 'P')
    bst.delete(8)
    bst.delete(15)
    bst.insert(55, 'R')
    bst.delete(50)
    bst.delete(5)
    bst.delete(24)
    print(bst.hight())
    print(bst.print())
    bst.print_tree()



