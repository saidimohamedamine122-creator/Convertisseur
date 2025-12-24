import time

def ConvertirTemperature():

    # Demande de données a l'utilisateur
    valeur = float(input("Entrez la température à convertir : "))
    unite_depart = input("Unité de départ (C, F, K) : ").strip().lower()
    unite_arrivee = input("Unité d'arrivée (C, F, K) : ").strip().lower()

    # Vérification des unités saisies par l'utilisateur
    if unite_depart not in ["c", "f", "k"] or unite_arrivee not in ["c", "f", "k"]:
        print("❌ Erreur : unité invalide (choisir c, f ou k).")
        input("\nAppuyez sur Entrée pour revenir au menu principal...")
        return

    # Étape 1 : Calcule pour passer au Celsius
    if unite_depart == "c":
        celsius = valeur
    elif unite_depart == "f":
        celsius = (valeur - 32) * 5 / 9
    elif unite_depart == "k":
        celsius = valeur - 273.15

    # Étape 2 : Calcule de conversion
    if unite_arrivee == "c":
        resultat = celsius
    elif unite_arrivee == "f":
        resultat = (celsius * 9 / 5) + 32
    elif unite_arrivee == "k":
        resultat = celsius + 273.15

    # Afficher le résultat
    print("\n✅ Résultat :")
    print(f"{valeur} {unite_depart.upper()} = {resultat:.2f} {unite_arrivee.upper()}")

    input("\nAppuyez sur Entrée pour revenir au menu principal...")
