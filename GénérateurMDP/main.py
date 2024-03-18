#TEST
#coding:utf-8
import random
import hashlib
from tkinter import *
import json
import os

lettres_maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lettres_min = "abcdefghijklmnopqrstuvwxyz"
caracteres_speciaux = "!@#$%^&*"
nombres = "0123456789"


#FONCTION AVEC TTE LES CONDITIONS DE SECURITÉ DU MDP
def verification(mot_de_passe):
    if len(mot_de_passe) < 8:
        return False, "Le mot de passe doit contenir au moins 8 caractères."
    if not any(caractere in lettres_maj for caractere in mot_de_passe):
        return False, "Le mot de passe doit contenir des majuscules."
    if not any(caractere in lettres_min for caractere in mot_de_passe):
        return False, "Le mot de passe doit contenir des minuscules."
    if not any(caractere in caracteres_speciaux for caractere in mot_de_passe):
        return False, "Le mot de passe doit contenir des caractères spéciaux."
    if not any(caractere in nombres for caractere in mot_de_passe):
        return False, "Le mot de passe doit contenir au moins un chiffre."

    return True, "Mot de passe valide."

#FONCTION QUI GENERE MDP ALÉATOIRE
def generer_mot_de_passe(longueur_mdp):
    caractere = lettres_maj + lettres_min + caracteres_speciaux + nombres
    mdp = ""
    for i in range(longueur_mdp):
        mdp += random.choice(caractere)
        
    mdp_aleatoire_hache = hachage(mdp)
    enregistrer_json(mdp_aleatoire_hache)
    return mdp, mdp_aleatoire_hache


def saisie_mot_de_passe(entry_mot_de_passe, label_mot_valide, label_erreur):
    mot_de_passe = entry_mot_de_passe.get()
    mdp_valide, message = verification(mot_de_passe)
    if mdp_valide:
        label_mot_valide.config(text="Mot de passe valide.")
        mot_de_passe_hache = hachage(mot_de_passe)
        enregistrer_json(mot_de_passe_hache)
    else:
        label_erreur.config(text=message, fg='red')

def hachage(mot_de_passe):
    
    hash_obj = hashlib.sha256()
    hash_obj.update(mot_de_passe.encode('utf-8'))
    mot_de_passe_hache = hash_obj.hexdigest()
    return mot_de_passe_hache

def enregistrer_json(mot_de_passe_hache):
    if os.path.exists("mots_de_passe.json") and os.path.getsize("mots_de_passe.json") > 0:
        with open("mots_de_passe.json", "r") as json_file:
            mots_de_passe_existant = json.load(json_file)
    else:
        mots_de_passe_existant = []

    mots_de_passe_existant.append(mot_de_passe_hache)
        
    with open("mots_de_passe.json", "w") as json_file:
        json.dump(mots_de_passe_existant, json_file)


def fenetre_longueur():
    fenetre_demande_longueur = Toplevel()
    fenetre_demande_longueur['bg'] = '#F6A2B7'
    fenetre_demande_longueur.title("Nombre de caractères")
    
    label_longueur = Label(fenetre_demande_longueur, text="Veuillez entrer la longueur du mot de passe:",font='fixedsys', bg='#F6A2B7', fg='white')
    label_longueur.pack(pady=1)
    
    entry_longueur = Entry(fenetre_demande_longueur)
    entry_longueur.pack()
    
    def valider_longueur():
        longueur_mdp = int(entry_longueur.get())
        mdp_clair, mdp_hache = generer_mot_de_passe(longueur_mdp)
        label_mot_de_passe.config(text="Mot de passe généré : " + mdp_clair)
        
    bouton_valider_longueur = Button(fenetre_demande_longueur, text="Valider", command=valider_longueur, bg='#E03E59', fg='white')
    bouton_valider_longueur.pack(pady=10)
    
    label_mot_de_passe = Label(fenetre_demande_longueur, text="", bg='#F6A2B5',fg='white')
    label_mot_de_passe.pack(pady=10)
    
def afficher_mot_de_passe_haches():
    fenetre_mdp_haches = Toplevel()
    fenetre_mdp_haches.title("Hachage")
    fenetre_mdp_haches['bg' ]='#E03E59'
    mots_de_passe_haches = charger_mots_de_passe_haches()

    if mots_de_passe_haches:
        for mdp_hache in mots_de_passe_haches:
            label_mdp_hache = Label(fenetre_mdp_haches, text=f"MDP clair: {mdp_hache[:8]}... | MDP haché: {mdp_hache}")
            label_mdp_hache.pack()
    else:
        label_aucun_mdp = Label(fenetre_mdp_haches, text="Aucun mot de passe haché trouvé.", bg='#F6A2B5')
        label_aucun_mdp.pack()

def charger_mots_de_passe_haches():
    mots_de_passe_haches = []

    if os.path.exists("mots_de_passe.json") and os.path.getsize("mots_de_passe.json") > 0:
        with open("mots_de_passe.json", "r") as json_file:
            mots_de_passe_haches = json.load(json_file)

    return mots_de_passe_haches
        
def interface_graphique():
    fenetre = Tk()
    fenetre.geometry("500x400")
    fenetre.title("Gestion MDP")
    fenetre['bg'] = '#F6A2B7'
    
    label = Label(fenetre, text="Gestionnaire de mot de passe", font=("Fixedsys", 15), bg='#F6A2B7', fg='white')
    label.pack(pady=10)
     # FENETRE POUR ORGANISER ENTRY ET BOUTONS VALIDER
    frame_principale = Frame(fenetre, bg='#F6A2B7')
    frame_principale.pack(pady=20)

    label_mot_de_passe = Label(frame_principale, text="Créez votre mot de passe et vérifiez sa validité :",font='fixedsys', bg='#F6A2B7',fg='white')
    label_mot_de_passe.pack()

    entry_mot_de_passe = Entry(frame_principale, show="*",fg='#E03E59')
    entry_mot_de_passe.pack()

    bouton_valider = Button(frame_principale, text="Valider", command=lambda: saisie_mot_de_passe(entry_mot_de_passe, label_mot_valide, label_erreur),bg='#E03E59', fg='white')
    bouton_valider.pack(pady=1)
    
    # ETIQUETTE MESSAGE OK OU ERREUR SI MDP RESPECTE PAS CONDITIONS
    label_mot_valide = Label(frame_principale, bg='#F6A2B7', fg='green')
    label_mot_valide.pack()
    label_erreur = Label(frame_principale, bg='#F6A2B7',fg="red")
    label_erreur.pack()
    fenetre.update()


#BOUTON GENERER MDP
    bouton_generer = Button (frame_principale, text="Générer un MDP", command=(fenetre_longueur),bg='#E03E59', fg='white')
    bouton_generer.pack(pady=20)
    #bouton mdphachés
    bouton_mdp_haches = Button (frame_principale, text="Afficher les mots de passe cryptés", command=afficher_mot_de_passe_haches,bg='#E03E59', fg='white')
    bouton_mdp_haches.pack(pady=20)
    
    fenetre.mainloop()
    
#SCRIPT

interface_graphique()

