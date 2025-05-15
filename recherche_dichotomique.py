from countries import countries_plus as countries


def rech_dich(tableau, element):

    debut = 0
    fin = len(tableau)-1
    tableau.sort()

    while debut <= fin :
        milieu = (debut + fin)//2
        if tableau[milieu] == element:
            return f'{element} trouvé à l\'index {milieu} de la liste'
        elif tableau[milieu] < element:
            debut = milieu +1
        elif element < tableau[milieu]:
            fin = milieu -1
    return f'{element} non trouvé dans la liste'
print(rech_dich(countries, 'France'))