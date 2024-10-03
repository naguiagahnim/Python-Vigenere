def car_vers_index(c):
    """Retourne l'indice de la lettre c dans l'alphabet personnalisé.
    Entrée : un caractère c
    Sortie : un entier"""
    if '@' <= c <= 'Z':
        return ord(c) - ord('@')
    else:
        return ord(c)

def index_vers_car(i):
    """Retourne la lettre de l'alphabet personnalisé correspondant à l'indice i.
    Entrée : un entier i
    Sortie : un caractère"""
    if 0 <= i < 27:
        return chr(i + ord('@'))
    else:
        return chr(i)

def chiffrementVigenere(texte, clef):
    """Chiffre un texte avec la méthode de Vigenère en suivant l'ordre de l'alphabet personnalisé.
    Entrée : le texte à chiffrer, la clef de chiffrement
    Sortie : le texte chiffré
    """
    texteChiffre = []
    clefTexte = [clef[i % len(clef)] for i in range(len(texte))]

    for i in range(len(texte)):
        char_code = car_vers_index(texte[i])
        key_code = car_vers_index(clefTexte[i])
        if '@' <= texte[i] <= 'Z':
            char_code_chiffre = (char_code + key_code) % 27
            texteChiffre.append(index_vers_car(char_code_chiffre))
        else:
            texteChiffre.append(chr((char_code + key_code) % 1114112))

    texteChiffre = ''.join(texteChiffre)
    return texteChiffre

def dechiffrementVigenere(texte, clef):
    """Déchiffre un texte chiffré avec la méthode de Vigenère en suivant l'ordre de l'alphabet personnalisé.
    Entrée : le texte chiffré, la clef de chiffrement
    Sortie : le texte déchiffré
    """
    texteDechiffre = []
    clefTexte = [clef[i % len(clef)] for i in range(len(texte))]

    for i in range(len(texte)):
        char_code = car_vers_index(texte[i])
        key_code = car_vers_index(clefTexte[i])
        if '@' <= texte[i] <= 'Z':
            char_code_dechiffre = (char_code - key_code) % 27
            texteDechiffre.append(index_vers_car(char_code_dechiffre))
        else:
            texteDechiffre.append(chr((char_code - key_code) % 1114112))

    texteDechiffre = ''.join(texteDechiffre)
    return texteDechiffre
