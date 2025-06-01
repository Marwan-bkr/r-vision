def combi_de(nombre_des, somme_voulue):
    # dp[i][s] = nombre de façons d'obtenir la somme s avec i dés
    dp = [[0] * (6 * nombre_des + 1) for _ in range(nombre_des + 1)]
    # Base : 0 dés pour obtenir la somme 0, il y a 1 façon (ne rien lancer)
    dp[0][0] = 1

    # Pour chaque nombre de dés de 1 à nombre_des
    for des_lances in range(1, nombre_des + 1):
        # La somme minimale possible avec des_lances dés est des_lances (tous 1)
        # La somme maximale possible est 6 * des_lances (tous 6)
        for somme_actuelle in range(des_lances, 6 * des_lances + 1):
            # On additionne toutes les façons d'obtenir somme_actuelle
            # en considérant le résultat du dernier dé (entre 1 et 6)
            total_facons = 0
            for face in range(1, 7):
                somme_reste = somme_actuelle - face
                if somme_reste >= 0:
                    total_facons += dp[des_lances - 1][somme_reste]
            dp[des_lances][somme_actuelle] = total_facons

    # Si la somme voulue n'est pas possible avec nombre_des dés, retourner 0
    if somme_voulue < nombre_des or somme_voulue > 6 * nombre_des:
        return 0
    
    return dp[nombre_des][somme_voulue]
print(combi_de(2, 2))  # Exemple d'utilisation