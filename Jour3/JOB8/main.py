"""Créer une fonction qui prend 2 paramètres :
➔ Le premier reçoit un String nommé « type »
➔ Le second reçoit un String nommé « saison »
Si la valeur de « type » est égale à « fruits » et que celle de saison est égale à «
hiver », affichez « orange, mandarine et kiwi »
Si la valeur de « type » est égale à « fruits » et que celle de saison est égale à «
été », affichez « Poire, fraise, cassis »
Si la valeur de « type » est égale à « légume » et que celle de saison est égale
à « hiver », affichez « carotte, topinambour, endive »
Si la valeur de « type » est égale à « légume » et que celle de saison est égale
à « été », affichez « artichaut, aubergine,navet »."""
#definir fonction(parametre), definir les conditions (if ect)
#créer variable pour retenir infos

def saison_type (type,saison):
    if type == ("fruit") and saison == ("hiver"):
        return ("orange, mandarine et kiwi")
    elif type == ("fruit") and saison == ("été"):
        return ("poire, fraise, cassis")
    elif type == ("légume") and saison ==("hiver"):
        return ("carotte, topinanbour, endive")
    elif type == ("légume") and saison ==("été"):
        return ("artichaut, aubergine, navet")
    
choixSaison = input("Choisir une saison (été ou hiver)")
choixType = input("Choisir un type(fruit ou légume)")

print(saison_type(choixType,choixSaison))
