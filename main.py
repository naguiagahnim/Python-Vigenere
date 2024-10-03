from module import *

def test_chiffrement():
    texte = "BONJOUR$@25"
    clef = "CLEF"
    texte_chiffre_attendu = "E@SPRFW*C>:"
    texte_chiffre = chiffrementVigenere(texte, clef)
    assert texte_chiffre == texte_chiffre_attendu, f"Expected {texte_chiffre_attendu}, but got {texte_chiffre}"

def test_dechiffrement():
    texte_chiffre = "E@SPRFW*C>:"
    clef = "CLEF"
    texte_dechiffre_attendu = "BONJOUR$@25"
    texte_dechiffre = dechiffrementVigenere(texte_chiffre, clef)
    assert texte_dechiffre == texte_dechiffre_attendu, f"Expected {texte_dechiffre_attendu}, but got {texte_dechiffre}"

def test_chiffrement_dechiffrement():
    texte = "BONJOUR$@25"
    clef = "CLEF"
    texte_chiffre = chiffrementVigenere(texte, clef)
    texte_dechiffre = dechiffrementVigenere(texte_chiffre, clef)
    assert texte_dechiffre.replace(" ", "").lower() == texte.replace(" ", "").lower(), \
        f"Expected {texte.replace(' ', '').lower()}, but got {texte_dechiffre.replace(' ', '').lower()}"

if __name__ == '__main__':
    test_chiffrement()
    test_dechiffrement()
    test_chiffrement_dechiffrement()
    print("Tous les tests fonctionnent.")