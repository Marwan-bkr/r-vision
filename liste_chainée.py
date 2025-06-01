class Maillon :
    def __init__(self, valeur, suivant):
        self.valeur = valeur
        self.suivant = suivant
        
class ListeChainee :
    def __init__(self):
        self.tete = None
        self.queue = None
        self.taille = 0
    
    def inserer(self, valeur):
        nouveau_maillon = Maillon(valeur, None)
        if self.tete is None:
            self.tete = nouveau_maillon
            self.queue = nouveau_maillon
        else:
            self.queue.suivant = nouveau_maillon
            self.queue = nouveau_maillon
        self.taille += 1
    
    def afficher(self):
        courant = self.tete
        while courant is not None:
            print(courant.valeur)
            courant = courant.suivant

    def supprimer(self, valeur):
        courant = self.tete
        precedent = None
        while courant is not None:
            if courant.valeur == valeur:
                if precedent is None:
                    self.tete = courant.suivant
                else:
                    precedent.suivant = courant.suivant
                self.taille -= 1
                return
            precedent = courant
            courant = courant.suivant

    def rechercher(self, valeur):
        courant = self.tete
        while courant is not None:
            if courant.valeur == valeur:
                return True
            courant = courant.suivant
        return False


lst = ListeChainee()
lst.inserer(1)
lst.inserer(2)
lst.inserer(3)
lst.afficher()