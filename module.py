# Chemins des fichiers
chemin_texte = './Sauvegarde/texte.txt'
chemin_clef = './Sauvegarde/clef.txt'
chemin_sortie = './Sauvegarde/texte_chiffre.txt'

def lire_fichier(chemin):
    """Lit le contenu d'un fichier et le retourne sous forme de chaîne de caractères."""
    with open(chemin, 'r', encoding='utf-8') as fichier:
        return fichier.read()

def ecrire_fichier(chemin, contenu):
    """Écrit le contenu dans un fichier."""
    with open(chemin, 'w', encoding='utf-8') as fichier:
        fichier.write(contenu)

def car_vers_index(c):
    """Retourne l'indice de la lettre c dans l'alphabet personnalisé."""
    if '@' <= c <= 'Z':
        return ord(c) - ord('@')
    else:
        return ord(c)

def index_vers_car(i, is_upper):
    """Retourne la lettre de l'alphabet personnalisé correspondant à l'indice i."""
    if 0 <= i < 27:
        return chr(i + ord('@'))
    else:
        return chr(i)

def chiffrementVigenere(texte, clef):
    """Chiffre un texte avec la méthode de Vigenère en suivant l'ordre de l'alphabet personnalisé."""
    texteChiffre = []
    clefTexte = [clef[i % len(clef)] for i in range(len(texte))]

    for i in range(len(texte)):
        char_code = car_vers_index(texte[i])
        key_code = car_vers_index(clefTexte[i])
        if '@' <= texte[i] <= 'Z':
            char_code_chiffre = (char_code + key_code) % 27
            texteChiffre.append(index_vers_car(char_code_chiffre, texte[i].isupper()))
        else:
            texteChiffre.append(chr((char_code + key_code) % 1114112))

    texteChiffre = ''.join(texteChiffre)
    ecrire_fichier(chemin_sortie, texteChiffre)
    return texteChiffre

def dechiffrementVigenere(texte, clef):
    """Déchiffre un texte chiffré avec la méthode de Vigenère en suivant l'ordre de l'alphabet personnalisé."""
    texteDechiffre = []
    clefTexte = [clef[i % len(clef)] for i in range(len(texte))]

    for i in range(len(texte)):
        char_code = car_vers_index(texte[i])
        key_code = car_vers_index(clefTexte[i])
        if '@' <= texte[i] <= 'Z':
            char_code_dechiffre = (char_code - key_code) % 27
            texteDechiffre.append(index_vers_car(char_code_dechiffre, texte[i].isupper()))
        else:
            texteDechiffre.append(chr((char_code - key_code) % 1114112))

    texteDechiffre = ''.join(texteDechiffre)
    return texteDechiffre