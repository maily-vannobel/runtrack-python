"""Écrire une fonction qui contient une liste nommée « fruits » qui contient les
strings pomme, cerise, orange, melon. Cette fonction doit à son appel ajouter
à la liste « fruits » une string « mangue » à l’index 2.
Résultat attendu : [‘pomme’, ‘cerise’, mangue, ‘orange’, ‘melon’]"""

def liste():
    fruits = ["pomme","cerise","orange","melon"]
    fruits.insert (2,"mangue")
    return fruits

print (liste()) 


