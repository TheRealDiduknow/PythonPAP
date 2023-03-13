import random
stop = False
choix= 'y'
nbParties = 0
totalCoups = 0
while (choix.lower()=='y') and not stop:
    secret = random.randint(1,100)
    nbParties = nbParties + 1
    print("Tapez -1 pour quitter le jeu")
    #print(secret) #Affiche le nombre secret pour débugger
    nbCoups=0
    n=102 #pour rentrer dans la boucle
    while n != secret and not stop:
        n= int(input("Entrez un nombre \n"))
        stop= n<0
        if not stop:
            nbCoups = nbCoups + 1
            if n<secret:
                print("Le nombre est trop petit")
            elif n>secret :
                print("Le nombre est trop grand")

    if not stop:
        totalCoups= totalCoups + nbCoups
        print(f'Super tu as trouvé en {nbCoups} coup{"s" if nbCoups>1 else ""}!!!')
        print(f'Ta moyenne est de {round(totalCoups/nbParties,2)} coups en {nbParties} partie(s)')
        choix=input("Tapez 'y' pour refaire une partie ")
    
if stop:
    print("Dommage … A la prochaine fois")
else:
    print("A la prochaine")
        