from random import randint

Quite = False
while Quite != True :
    Cuisine = 0
    Mechanique = 0
    Charisme = 0
    Physique = 0
    Logique = 0
    Créativité = 0
    Nettoyage = 0

    Competance = [Cuisine, Mechanique, Charisme,Physique,Logique,Créativité,Nettoyage]
    Boucle = 0
    while Boucle != 10:
        Competance[randint(0,6)] += 1
        Boucle += 1
        print (Competance)


    print ("Le sims aura les compétence si dessous \n Cuisine =",Competance[0],"\n Mechanique =",Competance[1],"\n Charisme =",Competance[2],"\n Physique =",Competance [3],"\n Logique =",Competance[4],"\n Créativité =", Competance[5],"\n Nettoyage =",Competance[6] )

    Quit = input ()
    if Quit == "s" :
        break