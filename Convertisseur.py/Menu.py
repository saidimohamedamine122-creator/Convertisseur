# Import des fonctions dans les autres fichier 
from ConvertionLongueur import ConvertirLongueur
from ConvertionTemps import ConvertirTemps
from ConvertionTemperature import ConvertirTemperature

# Fontion qui permet d'afficher le menu princiaple 
def menu():
    while True:
        print("\n===== CONVERTISSEUR MULTI-UNITÉS =====")
        print("1️⃣  Conversion de longueur")
        print("2️⃣  Conversion de temps")
        print("3️⃣  Conversion de température")
        print("4️⃣  Quitter")

        choix = input("\n👉 Entrez le numéro de votre choix : ")

        if choix == "1":
            ConvertirLongueur()
        elif choix == "2":
            ConvertirTemps()
        elif choix == "3":
            ConvertirTemperature()
        elif choix == "4":
            print("👋 Au revoir !")
            break   
        else:
            print("❌ Choix invalide, réessayez.")
