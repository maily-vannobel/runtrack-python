
#créer variable pour stocker reponse
logiciel_pref = input ("Quel est votre logiciel preferé ?")

def langages (langage):
    if langage == ("JavaScript"):
        return (" Vous êtes un développeur web")
    elif langage == ("python"):
      return (" Vous êtes un développeur IA")
    elif langage == ("java"):
       return (" Vous êtes un développeur logiciel")
    elif langage == ("reactjs"):
       return ("Vous êtes un développeur mobile")
    else: 
       return ("oups")

print(langages(logiciel_pref))
