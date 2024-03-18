1
#inventaire


nomProduit = ("Bouteille")
prixUnitaire = float(1.20)
quantiteStock = int(23) 

print ("Nom:",nomProduit)
print ("Prix:",prixUnitaire,"$")
print("Stock restant:",quantiteStock)



achatClient = int(input("Combien en prenez-vous?"))
quantiteReste = quantiteStock-achatClient

print ("Il en reste maintenant",quantiteReste)



#POURCENTAGES:10% = 0.10
# VERIFIER COMMENT CALCULER POURCENTAGES
haussePrix = float(0.10)
nouveauPrix = prixUnitaire * (1+ haussePrix)

print ("A cause de l'inflation, le prix augmente de 10%")
print ("Le nouveau prix est de", nouveauPrix)