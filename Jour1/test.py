#utf-8

pseudo = input("Quel est votre pseudo?")

import random

#variables pour les caractères
lettres = "ABCDEFGHI"
nombres = "12345"
symboles = "$!?"

caracteres = lettres + nombres + symboles
caracteresNoSymbol = lettres + nombres


while True: #tant que c'est vrai
    longueurMdp = int(input("De quelle taille voulez vous votre MDP?"))
    askCaractere = str(input("Voulez vous des caractères spéciaux ?"))
    if askCaractere == "oui": 
        for i in range (0,longueurMdp):#de 0 au nb que l'utilis. entre
         mdpCaract = random.choice (caracteres)
         mdp = mdp + mdpCaract
         print("Votre MDP est:",mdp[i])


        mdpCaract = random.choice (caracteresNoSymbol)
        mdp += mdpCaract
# SI IL VEUT PAS DE SYMBOLES DANS LE MDP ET DIT 'non'
    elif askCaractere == "non":
       for i in range (0,longueurMdp):
        print("Votre MDP est:",mdp[i]) 
        # i entre crochet pour quil prenne tous les caracteres pas que mdp

# SI IL ENTRE AUTRE CHOSE QUE 'oui' OU 'non'
else: askCaractere != 'oui' and 'non'#si askC PAS EGAL a oui ou non erreur
print ("erreur")