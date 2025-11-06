import random
symboles_lettre_nombres = [
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
    ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
    ['!', '#', '$', '%', '&', '(', ')', '*', '+']
]
def creation_mot_de_passe():
    """
    Creation d'un mot de passe utilisant un nombre de valeurs donnee par l'utilisateur
    :return: Le mot de pass generee apres l'avoir assemble
    """
    mot_de_passe_generate = []
    nbr_chiffre_raw = input("Entrer le nombre de valeurs voulu pour le mot de passe:")
    try:
        nbr_chiffre = int(nbr_chiffre_raw)
        for i in range(nbr_chiffre):
            random_rangee = random.choice(symboles_lettre_nombres)
            random_valeur = random.choice(random_rangee)
            mot_de_passe_generate.append(random_valeur)
            mot_de_passe_generate_merge = "".join(mot_de_passe_generate)
            return mot_de_passe_generate_merge
    except ValueError:
        print("Entrer un chiffre.")




if __name__ == '__main__':
    mot_de_passe = creation_mot_de_passe()
    print(mot_de_passe)
