#Here the second exercice
with open("exercice1.txt", "r") as my_file:
    text = my_file.read()
print(text)
print(len(text))


#Here The third exercice
"""def exercice_3(lettre):
    if lettre in text:
        print("True")
    else:
        print("False")
    
exercice_3("S")"""

#Here the fourth execice
def exercice_4(lettre):
    if lettre in text:
        print("La ",lettre,"se situe dans la positon :",text.index(lettre),"\n Et dans la colone : ")
    else:
        print('La lettre ', lettre, ' est introuvable dans la chaine text')
exercice_4("M")
