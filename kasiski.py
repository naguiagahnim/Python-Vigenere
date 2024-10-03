def kasiski(texte) -> int:
    """Utilise la méthode de Kasiski pour retrouver la taille de la clef utilisée pour chiffrer un texte suivant la méthode de Vigenère, donné en entrée.
    Entrée : Une chaîne de caractères texte.
    Sortie : Un entier représentant la taille de la clef
    """
    if not texte:
        raise ValueError("Le texte ne peut pas être vide")

    repet = []
    for i in range(len(texte)-3):
        for j in range(i+3, len(texte)):
            if texte[i:i+3] == texte[j:j+3]:
                repet.append((texte[i:i+3], j-i))
    repet.sort(key=lambda x: len(x[0]), reverse=True)

    if not repet:
        return 0

    candidats = []
    for i in range(2, repet[0][1]//2+1):
        if repet[0][1] % i == 0:
            candidats.append(i)

    for rep in repet[1:]:
        temp = []
        for cand in candidats:
            if rep[1] % cand == 0:
                temp.append(cand)
        if temp:
            candidats = temp
        else:
            continue
    return candidats[0] if candidats else 0