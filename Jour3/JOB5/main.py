"""Créer une fonction nommée « calcule » qui prend 3 paramètres :
➔ Le premier, « num1 », est un nombre,
➔ Le deuxième, « operator », est un caractère (string) contenant le type
d’opération(+, -, *, /, %),
➔ Le troisième, « num2 », est un nombre.
La fonction doit retourner le résultat de l’opération."""

#créer la fonction 'calcule' qui prends 3 paramètres
#SI OPERATEUR == TRUC, ALORS CA RETURN(RENVOIE/DONNE): num1 TRUC num2

def calcule (num1,operator,num2):
 if operator == '+':
  return num1 + num2
 elif operator == '-':
  return num1 - num2
 elif operator == '*':
  return num1 * num2
 elif operator == '/':
  return num1 / num2
 
 # ON A FAIS LES RETURN DANS LA FONCTION 'calcule'
 # ON PEUX PRINTER OU ON VEUT ???

print ("1+4 =", calcule(1,'+',4))
print ("10-5 =", calcule(10, '-', 5))
print ("20 / 6 =", calcule(20,'/',6))