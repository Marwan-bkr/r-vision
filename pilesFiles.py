class Pile:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if not self.is_empty() else None

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)  
    
    def afficher(self):
        if self.is_empty():
            print("La pile est vide.")
        else:
            print("Éléments de la pile :")
            for item in reversed(self.items):
                print(item)
    
    def vider(self):
        self.items.clear()
    
class File:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0) if not self.is_empty() else None

    def peek(self):
        return self.items[0] if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def afficher(self):
        if self.is_empty():
            print("La file est vide.")
        else:
            print("Éléments de la file :")
            for item in self.items:
                print(item)
    
    def vider(self):
        self.items.clear()

# Exemple d'utilisation de la classe Pile
pile = Pile()
pile.push(1)
pile.push(2)
pile.push(3)
pile.afficher()
print("Élément au sommet de la pile :", pile.peek())