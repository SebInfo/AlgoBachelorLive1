def indice_plus_petit_element(tableau):
    indice_petit = 0

    # Parcourir le tableau à partir du deuxième élément
    for i in range(1, len(tableau)):
        if tableau[i] < tableau[indice_petit]:
            indice_petit = i
    return indice_petit


# Exemple d'utilisation :
tableau = [5, 8, 3, 9, 1, 4]

indice = indice_plus_petit_element(tableau)
print(f"L'indice du plus petit élément est : {indice}")
print(f"Le plus petit élément est : {tableau[indice]}")
