def lire_fichier(chemin):
    """Lit le contenu d'un fichier et le retourne sous forme de chaîne de caractères.
    Entrée : chemin (str) le chemin du fichier à lire
    Sortie : le contenu du fichier"""
    with open(chemin, 'r', encoding='utf-8') as fichier:
        return fichier.read()


def ecrire_fichier(chemin, contenu):
    """Écrit le contenu dans un fichier.
    Entrée : chemin (str) le chemin du fichier, contenu (str) le contenu à écrire
    Sortie : aucune"""
    with open(chemin, 'w', encoding='utf-8') as fichier:
        fichier.write(contenu)

def car_vers_index(c):
    """Retourne l'indice de la lettre c dans l'alphabet.
    Entrée : c (str) un caractère
    Sortie : i (int) l'indice de c dans l'alphabet"""
    if 'A' <= c <= 'Z':
        return ord(c) - ord('A')
    elif 'a' <= c <= 'z':
        return ord(c) - ord('a')
    else:
        return ord(c)


def index_vers_car(i, is_upper):
    """Retourne la lettre de l'alphabet correspondant à l'indice i.
    Entrée : i (int) un indice, is_upper (bool) True si la lettre est en majuscule, False sinon
    Sortie : c (str) la lettre de l'alphabet correspondant à i"""
    if 0 <= i < 26:
        return chr(i + ord('A')) if is_upper else chr(i + ord('a'))
    else:
        return chr(i)

def chiffrementVigenere(texte, clef):
    """Chiffre un texte avec la méthode de Vigenère en suivant l'ordre de l'alphabet. Ecrit la sortie dans le fichier texte_chiffre.txt
    Entrée : texte (str) le texte à chiffrer, clef (str) la clé de chiffrement
    Sortie : texteChiffre (str) le texte chiffré"""

    texteChiffre = ""
    rsltListe = []  # Liste pour stocker le résultat chiffré
    clefTexte = []  # Liste pour stocker la clé répétée

    # Remplir clefTexte avec la clé répétée
    for i in range(len(texte)):
        clefTexte.append(clef[i % len(clef)])

    # Chiffrer chaque caractère du texte
    for i in range(len(texte)):
        char_code = car_vers_index(texte[i])  # Convertir le caractère en indice
        key_code = car_vers_index(clefTexte[i])  # Convertir le caractère de la clé en indice
        if 'A' <= texte[i] <= 'Z' or 'a' <= texte[i] <= 'z':
            # Chiffrer les lettres en suivant l'ordre de l'alphabet
            char_code_chiffre = (char_code + key_code) % 26
            rsltListe.append(index_vers_car(char_code_chiffre, texte[i].isupper()))
        else:
            # Chiffrer les caractères spéciaux et espaces en utilisant le code Unicode
            rsltListe.append(chr((char_code + key_code) % 1114112))

    # Convertir la liste en chaîne de caractères
    texteChiffre = ''.join(rsltListe)
    ecrire_fichier(chemin_sortie, texteChiffre)
    return texteChiffre

# Chemins des fichiers
chemin_texte = './Sauvegarde/texte.txt'
chemin_clef = './Sauvegarde/clef.txt'
chemin_sortie = './Sauvegarde/texte_chiffre.txt'

def texteFichier(chemin_texte, chemin_clef):
    """Lit les fichiers texte et clé et retourne leur contenu. On l'utilisera si l'utilisateur veut utiliser des fichiers pour la fonction."""
    texte = lire_fichier(chemin_texte)
    clef = lire_fichier(chemin_clef)
    return texte, clef

