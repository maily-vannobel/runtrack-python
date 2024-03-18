"""Créer une fonction qui prend en paramètre un nombre nommé « nombre ».
Afficher « positif » si le nombre est supérieur à 0.
Afficher « négatif » si le nombre est inférieur à 0.
Appeler cette fonction plusieurs fois en y passant des paramètres différents
pour afficher ces résultats."""

def nombre (num):
 if num < 0:
  return ("négatif, nombre inférieur à 0")
 elif num > 0:
  return ("positif, nombre supérieur à 0")
 else:
  return ("Le chiffre est zéro")
 

print("22 est", nombre(22)) 
print("-9 est", nombre(-9)) 
print("0:", nombre(0)) 

