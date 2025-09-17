# Exercice 04 – Hauteur atteinte par un escalier mécanique (gabarit)
"""
Objectif :
- DEMANDER longueur (m, float) et angle (° en degrés, float)
- Valider : longueur >= 0 et 0 <= angle <= 90
    -> sinon afficher "Erreur - données invalides."
- Sinon : H = L * sin(radians(angle)) ; afficher avec 2 décimales : "{H:.2f} m"

Prompts EXACTS à utiliser quand vous implémenterez input :
1) "Entrez la longueur de l'escalier (en mètres) : "
2) "Entrez l'angle de l'escalier par rapport à l'horizontale (en degrés) : "
"""




import math

x = input("Entrez la longueur de l'escalier (en mètres) : ")
y = input("Entrez l'angle de l'escalier par rapport à l'horizontale (en degrés) : ")
x=float(x)
y=float(y)

if x<0 or not (0 <= y <= 90):
    print("Erreur - données invalides.")
else:
    hauteur = x * math.sin(math.radians(y))
  
    print(f"{hauteur:.2f} m")

 



                    

