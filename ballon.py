import csv 
donnees=[]
with open('Donnees.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=';')
    for row in reader:
        donnees.append(row)
#print(donnees)
del donnees[0]
#print(len(donnees))
speed=[]
for ligne in donnees:
    valeur1=ligne[15]
    speed.append(float(valeur1))
print(speed)
temps=[]
for ligne in donnees:
    valeur2=ligne[0]
    temps.append(valeur2)
print(temps)
Datetime=[]
#on a convertir le temps en minutes
for t in temps:
    h, m, s = t.split(":")
    total_minutes = int(h) * 60 + int(m) + float(s) / 60
    Datetime.append(total_minutes)
print(Datetime)
#on va dessiner la courbe de l'acceleration en fonction du temps
import matplotlib.pyplot as plt
import numpy as np
plt.plot(Datetime, speed)
plt.xlabel("Temps (minutes)")
plt.ylabel("Acceleration")
plt.title("Acceleration en fonction du temps")
plt.show()
#réalisation d'un courbe de l'altitude du ballon en fonction du temps
altitude=[]
for ligne in donnees:
    valeur3=ligne[3]
    altitude.append(float(valeur3))
print(altitude)
plt.plot(Datetime, altitude)
plt.xlabel("Temps (minutes)")
plt.ylabel("Altitude")
plt.title("Altitude en fonction du temps")
plt.show()
#realisation d'un courbe du deplacement du ballon
latitude=[]
longitude=[]
rotation_z=[]
for ligne in donnees:
    valeur4=ligne[1]
    latitude.append(float(valeur4))
for ligne in donnees:
    valeur5=ligne[2]
    longitude.append(float(valeur5))
print(latitude)
print(longitude)
print(altitude)
from mpl_toolkits.mplot3d import axes3d
# Tracé du résultat en 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')  # Affichage en 3D
ax.plot(latitude, longitude, altitude)
plt.title("Deplecement du ballon dans l'espace")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.tight_layout()
plt.show()


