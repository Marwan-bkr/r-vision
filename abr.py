
class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.gauche = None
        self.droite = None

class ArbreBinaireRecherche:
    def __init__(self):
        self.racine = None

    def inserer(self, valeur):
        if self.racine is None:
            self.racine = Noeud(valeur)
        else:
            self._inserer_recursif(self.racine, valeur)

    def _inserer_recursif(self, noeud, valeur):
        if valeur < noeud.valeur:
            if noeud.gauche is None:
                noeud.gauche = Noeud(valeur)
            else:
                self._inserer_recursif(noeud.gauche, valeur)
        else:
            if noeud.droite is None:
                noeud.droite = Noeud(valeur)
            else:
                self._inserer_recursif(noeud.droite, valeur)
    def afficher(self):
        if self.racine is not None:
            self.afficher_recursif(self.racine)

    def afficher_recursif(self, noeud):
        if noeud is not None:
            self.afficher_recursif(noeud.gauche)
            print(noeud.valeur)
            self.afficher_recursif(noeud.droite)
    def rechercher(self, valeur):
        return self.rechercher_recursif(self.racine, valeur)

    def rechercher_recursif(self, noeud, valeur):
        if noeud is None:
            return False
        if noeud.valeur == valeur:
            return True
        elif valeur < noeud.valeur:
            return self.rechercher_recursif(noeud.gauche, valeur)
        else:
            return self.rechercher_recursif(noeud.droite, valeur)
        
    def supprimer(self, valeur):
        self.racine = self.supprimer_recursif(self.racine, valeur)

    def supprimer_recursif(self, noeud, valeur):
        if noeud is None:
            return noeud
        if valeur < noeud.valeur:
            noeud.gauche = self.supprimer_recursif(noeud.gauche, valeur)
        elif valeur > noeud.valeur:
            noeud.droite = self.supprimer_recursif(noeud.droite, valeur)
        else:
            # Noeud à supprimer trouvé
            if noeud.gauche is None:
                return noeud.droite
            elif noeud.droite is None:
                return noeud.gauche
            else:
                # Noeud avec deux enfants
                min_droit = self.trouver_minimum(noeud.droite)
                noeud.valeur = min_droit.valeur
                noeud.droite = self.supprimer_recursif(noeud.droite, min_droit.valeur)
        return noeud
    
    def trouver_minimum(self, noeud):
        current = noeud
        while current.gauche is not None:
            current = current.gauche
        return current
    
    def trouver_maximum(self, noeud):
        current = noeud
        while current.droite is not None:
            current = current.droite
        return current
    
    def hauteur(self):
        return self.hauteur_recursif(self.racine)
    
    def hauteur_recursif(self, noeud):
        if noeud is None:
            return 0
        else:
            gauche_hauteur = self.hauteur_recursif(noeud.gauche)
            droite_hauteur = self.hauteur_recursif(noeud.droite)
            return max(gauche_hauteur, droite_hauteur) + 1
    
# Exemple d'utilisation

arbre = ArbreBinaireRecherche()
arbre.inserer(5)
arbre.inserer(3)
arbre.inserer(7)
arbre.inserer(2)
arbre.inserer(4)
arbre.inserer(6)
arbre.inserer(8)

print("Affichage de l'arbre :")
arbre.afficher()

print("Recherche de la valeur 4 :", arbre.rechercher(4))
print("Recherche de la valeur 10 :", arbre.rechercher(10))

arbre.supprimer(3)
print("Affichage de l'arbre après suppression de 3 :")
arbre.afficher()

