#Here the second exercice
with open("exercice1.txt", "r") as my_file:
    text = [my_file.readline(),my_file.readline(),my_file.readline(),my_file.readline()]
            #WWWW-----W,W-------W,WWW-M--WWW,WWWWWW--WW
for i in text:
    print(i)    
    


#Here The third exercice

def exercice_3(lettre):
    for lettre in text[:]:
        klink = 'WWWW-----W'
        if klink == text[0]:
            print('True')
        else:
            print('False')
exercice_3("WWWW-----W")

#Here the fourth execice

"""def exercice_4(lettre):
    if lettre in text:
        print("La ",lettre,"se situe dans la positon :",text.index(lettre),"\n Et dans la colone :")
    else:
        print('La lettre ', lettre, ' est introuvable dans la chaine text')
exercice_4("M")"""

# Here exercice number 5


# Here exercice number 6


# Here exercice number 7
"""def game():
    continuer = "o"
    while continuer == "o":
        enter = input('Voulez Vous continuer ? tapez o pour oui et n pour non : ')
        if enter == "n":
            continuer = enter
            print ('programe est términer')
        elif enter == "o" :
            continuer = enter
        else:
            print('Veuiller choisir une lettre valide !!')
        
game()"""
