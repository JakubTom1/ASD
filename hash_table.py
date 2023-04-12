
class Element:
    def __init__(self, key, data):
        self.key = key
        self.data = data

class HashTab:
    def __init__(self, size, c1=1, c2=0):
        self.tab = [None for i in range(size)]
        self.size = size
        self.c1 = c1
        self.c2 = c2

    def __str__(self):
        outlist = []
        for el in range(self.size):
            if self.tab[el] is not None:
                outlist.append(str(self.tab[el].key) + ":" + str(self.tab[el].data))
        return "{" + ", ".join(outlist) + "}"

    def mix(self, key):
        if type(key) is str:
            sum = 0
            for letter in key:
                sum += ord(letter)
            return sum % self.size
        else:
            return key % self.size

    def solve_collision(self, idx, key):
        for i in range(self.size):
            new_idx = (idx + self.c1*i + self.c2*i**2) % self.size
            if (self.tab[new_idx] is None) or (self.tab[new_idx].key is None) or (self.tab[new_idx].key == key):
                return new_idx
        return None

    def search(self, key):
        for idx in range(self.size):
            if self.tab[idx] is not None:
                if self.tab[idx].key == key:
                    return self.tab[idx].data

        idx = self.mix(key)
        if self.tab[idx].key is None:
            return None

    def insert(self, key, data):
        idx = self.mix(key)
        if (self.tab[idx] is None) or (self.tab[idx].key is None) or (self.tab[idx].key == key):
            self.tab[idx] = Element(key, data)
        else:
            idx = self.solve_collision(idx, key)
            if idx is None:
                print("Brak miejsca")
                return None
            else:
                self.tab[idx] = Element(key, data)

    def remove(self, key):
        idx = self.mix(key)
        if self.tab[idx].key is not None:
            self.tab[idx] = None
        else:
            print("Brak danej o podanym kluczu")
            return None

if __name__ == '__main__':
    def test_1(alfabet, c1=1, c2=0):
        tab = HashTab(13, c1, c2)
        for i in range(len(alfabet)):
            key = i+1
            if key == 6:
                key = 18
            if key == 7:
                key = 31
            tab.insert(key, alfabet[i])
        print(tab)
        print(tab.search(5))
        print(tab.search(14))
        tab.insert(5, "Z")
        print(tab.search(5))
        tab.remove(5)
        print(tab)
        print(tab.search(31))
        tab.insert('test','W')
        print(tab)

    def test_2(alfabet, c1=1, c2=0):
        tab = HashTab(13, c1, c2)
        for i in range(len(alfabet)):
            key = (i+1)*13
            tab.insert(key, alfabet[i])
        print(tab)

    alfabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
    print("Pierwsza funkcja testująca(próbkowanie liniowe)")
    test_1(alfabet)
    print("\nDruga funkcja testująca(próbkowanie liniowe)")
    test_2(alfabet)
    print("\nDruga funkcja testująca(próbkowanie kwadratowe)")
    test_2(alfabet,0,1)
    print("\nPierwsza funkcja testująca(próbkowanie kwadratowe)")
    test_1(alfabet,0,1)