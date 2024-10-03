def lire_fichier(chemin):
    """Lit le contenu d'un fichier et le retourne sous forme de chaîne de caractères."""
    with open(chemin, 'r', encoding='utf-8') as fichier:
        return fichier.read()

def ecrire_fichier(chemin, contenu):
    """Écrit le contenu dans un fichier."""
    with open(chemin, 'w', encoding='utf-8') as fichier:
        fichier.write(contenu)