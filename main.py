from tests import *
import time

def lancerTests() :
    separateur = '\n-------------------------------------'
    temps_avant_exec = time.time()
    test_chiffrement()
    temps_apres_exec = time.time()
    print("Temps écoulé pour le chiffrement: ", temps_apres_exec - temps_avant_exec, " secondes.")
    temps_avant_exec = time.time()
    print(separateur)
    test_dechiffrement()
    temps_apres_exec = time.time()
    print("Temps écoulé pour le déchiffrement: ", temps_apres_exec - temps_avant_exec, " secondes.")
    temps_avant_exec = time.time()
    print(separateur)
    test_chiffrement_dechiffrement()
    temps_apres_exec = time.time()
    print("Temps écoulé pour le chiffrement et le déchiffrement: ", temps_apres_exec - temps_avant_exec, " secondes.")
    temps_avant_exec = time.time()
    print(separateur)
    test_kasiski()
    temps_apres_exec = time.time()
    print("Temps écoulé pour kasiski: ", temps_apres_exec - temps_avant_exec, " secondes.")
    temps_avant_exec = time.time()
    print(separateur)
    print("Tous les tests fonctionnent.")




if __name__ == '__main__':
    lancerTests()