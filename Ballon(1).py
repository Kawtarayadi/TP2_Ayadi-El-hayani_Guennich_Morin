import csv
import matplotlib.pyplot as plt
donnees=[]
with open('Donnees(1).csv',newline='') as csvfile:
    reader=csv.reader(csvfile, delimiter=',')
    for row in reader:
        donnees.append(row)

del donnees[0]
#on import les données du fichier dans une liste puis on supprime la premiere ligne.

haut=[]
for ligne in donnees :
    valeur1=ligne[3]
    haut.append(float(valeur1))

#ici on met dans une liste toutes les valeur d'altitude du ballon
tempE=[]
for ligne in donnees :
    valeur1=ligne[6]
    tempE.append(float(valeur1))

#on fait de même avec la température exterieur
tempI=[]
for ligne in donnees :
    valeur1=ligne[5]
    tempI.append(float(valeur1))
#et avec la température interieur


plt.scatter(haut,tempE,s=1,color="r",label='Température Extérieure')
plt.ylabel('Température en °c / Humidité en g/m³')
plt.xlabel('altitude en m')
plt.scatter(haut,tempI,s=1,color="b",label="Température Intérieure")
#maintenant on recupere l'humidité exterieur
Hum=[]
for ligne in donnees :
    valeur1=ligne[7]
    Hum.append(float(valeur1))

plt.scatter(haut,Hum,s=1,color="g",label='Humidité Extérieure')
plt.title("Humidité et température Intérieure/Extérieur en fonction de l'altitude")
plt.legend()
plt.show
#on obtient alors un graphique avec l'Humidité et température Intérieure/Extérieur en fonction de l'altitude