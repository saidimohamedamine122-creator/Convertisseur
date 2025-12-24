import time

# Dictionnaire des unités par rapport au mètre
ConversionLongueur = {
    "m": 1,
    "km": 1000,
    "cm": 0.01,
    "mm": 0.001,
    "miles": 1609.34,
    "foot": 0.3048
}

# Fonction qui permet de convertir des longueurs
def ConvertirLongueur():

    # Demande de données a l'utilisateur
    UniteDepart = input("Veuillez entrer une unité de départ (m, km, cm, mm, miles, foot) : ").strip().lower()
    UniteArrive = input("Veuillez entrer une unité d'arrivée (m, km, cm, mm, miles, foot) : ").strip().lower()
    Valeur = float(input("Veuillez entrer une valeur à convertir : "))

    # Calcul de la conversion via le mètre (unité de référence)
    if UniteDepart in ConversionLongueur and UniteArrive in ConversionLongueur:
        ValeurEnM = Valeur * ConversionLongueur[UniteDepart]
        resultat = ValeurEnM / ConversionLongueur[UniteArrive]

        # Affiche le résultat    
        print("\n✅ Résultat :")
        print(f"{Valeur} {UniteDepart} = {resultat:.2f} {UniteArrive}")

    # Message d'erreur 
    else:
        print("❌ Erreur : une ou les deux unités ne sont pas reconnues.")

    # Retour au menu principale
    input("\nAppuyez sur Entrée pour revenir au menu principal...")

