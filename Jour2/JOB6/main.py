
# vérifier si c'est un nb premier

def nb_premier (n):  
    if n <=2:          #SI N EST INF OU EGAL A 2
      return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# ---
for n in range(0, 101):
    if nb_premier(n):
        print(n)



