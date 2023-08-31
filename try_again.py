"""
while True:
    chiffre = input("Entrez le chiffre 3: ")
    if int(chiffre) != 3:
        print("Incorrect")
    else:
        print("Super")
        break
"""


chiffre = 0
choix = "oui"

# Boucle 1
while choix != "non":
    # 1ere instruction
    while int(chiffre) != 3: # Boucle 2
        chiffre = input("Entrez le chiffre 3: ")
        if int(chiffre) != 3:
            print("Incorrect")
        else:
            print("Super")
        
            choix = input("Voulez-vous recommencer ? (oui ou non): ")

    # 2e instruction
    chiffre = 0
#    print("première boucle")




