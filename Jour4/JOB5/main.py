"""
Écrire un programme qui crée une liste nommée « L » d’au moins 5 entiers
puis successivement :
➔ Afficher la deuxième valeur de la liste
➔ Écrire une fonction qui remplace L[3] par la somme des cases voisines
L[2] & L[4], puis afficher à nouveau le tableau.
➔ Puis afficher la dernière valeur de la liste."""

L = [1,2,3,4,5] 
print(L[1])

def remplace(L, index):
    remplace = (L[2]) + (L[4])
    remplace(L, 3)


print(L)
#remplacer [3] par [2]+[4]