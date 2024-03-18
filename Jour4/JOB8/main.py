"""Écrire un programme qui calcule la somme de toutes les valeurs paires de la
liste : L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]."""

"""
-L = liste avec les chiffres
-paires = pour stocker les pairs
-for nombre in L - POUR les nb de la liste, DANS la liste
-SI le nb modulo 2 = 0 (divisible par 2 sans reste)
   nb est pair donc l'ajouter a l'addition"""



L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
paires = 0

for nombre in L :
    if nombre % 2 == 0:

"""si un nb est divisible par 2 sans reste: il est pair
si un bn divisé par 2 laisse un reste de 1: il est impair
n % == 0  pair
n % == 1   impair """