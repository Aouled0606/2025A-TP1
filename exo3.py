# Exercice 03 – Marcher ou attendre le bus ? (gabarit)
"""
Objectif :
- DEMANDER distance (km, float) et attente (min, float/int)
- Temps marche (min) = distance * 60 / 5
- Temps bus (min) = attente + distance * 60 / 20
- Afficher EXACTEMENT UNE des phrases :
    "Il est plus rapide de marcher."
    "Il est plus rapide de prendre le bus."
    "Les deux options prennent le même temps."

Prompts EXACTS à utiliser quand vous implémenterez input :
1) "Entrez la distance jusqu'à la destination (en kilomètres) : "
2) "Entrez le temps d'attente avant le prochain bus (en minutes) : "
"""




x=input("Entrez la distance jusqu'à la destination (en kilomètres) : ")
x=float(x)
y=input("Entrez le temps d'attente avant le prochain bus (en minutes) :")
y=int(y)
bustime = y + x/20 * 60
marchetime= x/5 * 60
if bustime<marchetime:
    print("Il est plus rapide de prendre le bus.")
if bustime>marchetime:
    print("Il est plus rapide de marcher.")
if bustime==marchetime:
    print("Les deux options prennent le même temps.")





    

