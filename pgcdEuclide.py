def pgcd(a, b):
    # S'assurer que a >= b
    if a < b:
        a, b = b, a  # Permuter a et b

    while b != 0:
        reste = a % b
        a = b
        b = reste
    return a

# Exemple d'utilisation :
a = 54
b = 24

resultat_pgcd = pgcd(a, b)
print(f"Le PGCD de {a} et {b} est : {resultat_pgcd}")
