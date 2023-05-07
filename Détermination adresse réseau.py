import time
adresseIP = []
masque = []
rang = ["premier", "deuxième", "troisième", "quatrième"]
print ("Pour commencer vous allez saisir les 4 nombres de l'adresse IP de l'ordinateur.")
for i in range (4) :
    question = "Donner le " + rang[i] + " nombre de l'adresse IP v4 de l'ordinateur : "
    x = input (question)
    x = int (x)
    adresseIP = adresseIP + [x]
print ("Ensuite vous allez saisir les 4 nombres du masque de sous réseau.")
for i in range (4) :
    question = "Donner le " + rang[i] + " nombre du masque de sous réseau : "
    x = input (question)
    x = int (x)
    masque = masque + [x]
print ("C'est parfait.")
print ("Voici l'adresse du réseau de l'ordinateur :")
time.sleep (2.5)
for i in range (3) :
        print (adresseIP[i] & masque[i], end = "")
        time.sleep (2.5)
        print (".", end = "")
        time.sleep (2.5)
print (adresseIP[3] & masque[3])
time.sleep (2.5)
print ("Programme terminé !")