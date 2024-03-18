

"""1.boucle for pour générer chaque ligne
2.elle itère de 1 à la longueur de alphabet +1 
3. Sélectionner les premiers caractères de l'alphabet
avec le slicing, 
"""
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(1, len(alphabet) + 1):
    ligne = alphabet[:i]  
    print(ligne)