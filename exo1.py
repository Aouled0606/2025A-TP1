# Exercice 01 – Usage hebdomadaire du métro (gabarit)
"""
Objectif :
- DEMANDER le nom complet et le nombre de déplacements par semaine (entier)
- Calculer le nombre de déplacements annuels
- Afficher EXACTEMENT :
    Bonjour {nom}
    Vous effectuez environ {nombre de déplacements annuels} déplacements par an sur le réseau STM.

Prompts (à utiliser quand vous implémenterez input) :
1) "Veuillez entrer votre nom complet : "
2) "Veuillez entrer le nombre de déplacements par semaine : "
"""


x=input("Veuillez entrer votre nom complet:")
x=str(x)
print("Bonjour",x)
y=input("Veuillez entrer le nombre de déplacements par semaine : ")
y=int(y)
deplacement= y * 52
print("Vous effectuez environ",deplacement,"déplacements par an sur le réseau STM.") 


