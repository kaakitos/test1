def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b


def calculatrice():
    print("=== Calculatrice ===")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")

    choix = input("Choisissez une opération (1 à 4) : ")

    a = float(input("Premier nombre : "))
    b = float(input("Deuxième nombre : "))

    if choix == "1":
        resultat = addition(a, b)
    elif choix == "2":
        resultat = soustraction(a, b)
    else:
        resultat = "Choix invalide."

    print("Résultat :", resultat)


# Lancement du programme
calculatrice()