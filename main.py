from tests import *
from gestion_fichiers import *

# Chemins des fichiers
chemin_texte = './Sauvegarde/texte.txt'
chemin_clef = './Sauvegarde/clef.txt'
chemin_texte_chiffre = './Sauvegarde/texte_chiffre.txt'

def menu():
    while True:
        print("\nMenu:")
        print("1 - Chiffrer un texte")
        print("2 - Déchiffrer un texte")
        print("3 - Afficher le contenu d'un fichier")
        print("4 - Méthode de Kasiski sur un texte")
        print("5 - Lancer les tests")
        print("6 - Quitter")
        choix = input("Choisissez une option: ")

        if choix == '1':
            texte = lire_fichier(chemin_texte)
            clef = lire_fichier(chemin_clef)
            texte_chiffre = chiffrementVigenere(texte, clef)
            print("Texte chiffré: ", texte_chiffre)
            ecrire_fichier(chemin_texte_chiffre, texte_chiffre)
            print("\033[95mTexte chiffré sauvegardé avec succès dans texte_chiffre.txt\033[0m")
        elif choix == '2':
            texte = lire_fichier(chemin_texte_chiffre)
            clef = lire_fichier(chemin_clef)
            texte_dechiffre = dechiffrementVigenere(texte, clef)
            print("Texte déchiffré: ", texte_dechiffre)
        elif choix == '3':
            print("a - texte.txt")
            print("b - clef.txt")
            print("c - texte_chiffre.txt")
            choix_fichier = input("Choisissez un fichier: ")
            if choix_fichier == 'a':
                fichier_affiche = lire_fichier(chemin_texte)
            elif choix_fichier == 'b':
                fichier_affiche = lire_fichier(chemin_clef)
            elif choix_fichier == 'c':
                fichier_affiche = lire_fichier(chemin_texte_chiffre)
            else:
                print("Choix invalide")
                continue
            print("Contenu du fichier : ", lire_fichier(fichier_affiche))
        elif choix == '4':
            texte_chiffre = lire_fichier(chemin_texte_chiffre)
            clef = kasiski(texte_chiffre)
            print("Clef trouvée par la méthode de Kasiski: ", clef)
        elif choix == '5':
            lancerTests()
        elif choix == '6':
            print("\033[95mAu revoir!\033[0m")
            break
        else:
            print("\033[91mChoix invalide, veuillez réessayer.\033[0m")

if __name__ == '__main__':
    menu()