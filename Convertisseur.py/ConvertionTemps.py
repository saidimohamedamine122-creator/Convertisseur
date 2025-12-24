import time 

# Dictionnaire des unités par rapport seconde
ConversionTemps = {
    "s" : 1,
    "min" : 60,
    "h" : 3600,
    "j" : 86400,
    }

# Fonction pour convertir le temps 
def ConvertirTemps():
    
    # Demande de données a l'utilisateur
    UniteDepart = input("Veuillez entrez une unité de départ (s, min, h, j) : ").strip().lower()
    UniteArrive = input("Veuillez entrez une unité d'arrivée (s, min, h, j) : ").strip().lower()
    valeur = int(input("Entrez une valeur a convertir : "))
    
    # Verification pour voir si les unité rentrer sont dans le dictionnaire
    if UniteDepart in ConversionTemps and UniteArrive in ConversionTemps:
        
        # Calcule de conversion 
        ValeurEnS = valeur * ConversionTemps[UniteDepart]
        resultat = ValeurEnS / ConversionTemps[UniteArrive]

        # Afficher le resultat
        print("\n✅ Résultat :")
        print(f"{valeur} {UniteDepart} = {resultat:.2f} {UniteArrive}")

    # Message d'erreur    
    else:
        print("❌ Erreur : une ou les deux unités ne sont pas reconnues. Réessayez.\n")

    # Retour au menu pricipale
    input("\nAppuyez sur Entrée pour revenir au menu principal...")

   
