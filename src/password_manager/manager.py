import os, json, sys, hashlib 
# from prompt_toolkit import prompt
# from prompt_toolkit.document import Document
# from prompt_toolkit.validation import Validator, ValidationError

def creation_master_password():
    mot_de_passe = input("Entré un mot de passe: ")
    mot_de_passe_a_confirmer = input("Confirmer le mot de passe: ")
    # if len(mot_de_passe) <= 12:
        # confirmation_mot_de_passe_faible = input("Votre mot de passe est faible.\n Voulez vous continuer avec un mot de passe faible?(y/n): ")
        # if confirmation_mot_de_passe_faible == "y":


    if mot_de_passe == mot_de_passe_a_confirmer:
        mot_de_passe_confirmer = mot_de_passe
    else:
        valide = False
        while valide == False:
            print("mot de passe")
            mot_de_passe_a_confirmer = input("Confirmer le mot de passe: ")
            if mot_de_passe == mot_de_passe_a_confirmer:
                valide = True
    return mot_de_passe
creation_master_password()
