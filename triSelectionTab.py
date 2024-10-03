def tri_selection(tableau):
    # Parcourir les éléments jusqu'à l'avant-dernier
    for i in range(len(tableau) - 1):  # On s'arrête à l'élément n-1
        # Trouver l'indice du plus petit élément à partir de l'indice i
        min_indice = i
        for j in range(i + 1, len(tableau)):
            print(j)
            if tableau[j] < tableau[min_indice]:
                min_indice = j

        # Échanger l'élément à l'indice i avec le plus petit élément trouvé
        tableau[i], tableau[min_indice] = tableau[min_indice], tableau[i]

    return tableau

# Exemple d'utilisation :
tableau = [29, 10, 14, 37, 14]
tableau_trie = tri_selection(tableau)
print(f"Tableau trié : {tableau_trie}")
