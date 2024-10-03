from tests import *
import time

def lancerTests() :
    separateur = '\n-------------------------------------\n'
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
    #lancerTests()
    entree_1_non_chiffre = """Ensuite, il a beaucoup bavardé. On l'aurait bien étonné en lui disant
qu'il finirait concierge à l'asile de Marengo. Il avait soixante-quatre
ans et il était Parisien. À ce moment je l'ai interrompu : « Ah, vous
n'êtes pas d'ici ? » Puis je me suis souvenu qu'avant de me conduire
chez le directeur, il m'avait parlé de maman. Il m'avait dit qu'il fallait
l'enterrer très vite, parce que dans la plaine il faisait chaud, surtout
dans ce pays. C'est alors qu'il m'avait appris qu'il avait vécu à Paris et
qu'il avait du mal à l'oublier."""
    entree_1 = chiffrementVigenere(entree_1_non_chiffre, "ABSURDE")
    print(kasiski(entree_1))
