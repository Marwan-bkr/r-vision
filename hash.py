from liste_chainée import ListeChainee

def hachage_chaine_séparée(chaine):
    """
    Fonction de hachage pour une chaîne de caractères.
    :param chaine: La chaîne à hacher.
    :return: Le code de hachage.
    """
    code_hachage = 0
    for caractere in chaine:
        code_hachage += ord(caractere)
    return code_hachage % 1000  # Limiter le code de hachage à 3 chiffres
print(hachage_chaine_séparée("exemple"))  # Exemple d'utilisation

class tableau_haché:
    def __init__(self, taille):
        self.taille = taille
        self.tableau = [None] * taille

    def inserer(self, valeur):
        index = hachage_chaine_séparée(valeur) % self.taille
        if self.tableau[index] is None:
            liste_chainée = ListeChainee()
            self.tableau[index] = liste_chainée
        self.tableau[index].inserer(valeur)

    def afficher(self):
        for i in range(self.taille):
            if self.tableau[i] is not None:
                print(f"Index {i}: {self.tableau[i].afficher()}")
                print(f"---------------------------------------------------------")

tableau_haché = tableau_haché(100)
for i in range(100):
    tableau_haché.inserer(f"chaine_{i}")
tableau_haché.afficher()