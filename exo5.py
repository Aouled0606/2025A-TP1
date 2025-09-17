# Exercice 05 – Répartition optimale des titres (gabarit)
"""
Objectif :
- DEMANDER n (int), le nombre total de trajets.
- Trouver une combinaison EXACTE minimal coût en utilisant :
    30 trajets -> 75.00$
    10 trajets -> 30.00$
     1 trajet  ->  3.75$
- Afficher EXACTEMENT :
    Carnets de 30 billets - Xx
    Carnets de 10 billets - Y
    Billets simples - Z
    Prix total - TTT.TT$

BONUS (optionnel mais recommandé) :
- Si une SUR-COUVERTURE (acheter un peu plus de trajets) est moins chère,
  afficher en plus :
  "Il existe une combinaison sur-couvrante moins chère : A, B, C : PPP.PP$ (surplus : S trajet(s))"

Prompt EXACT à utiliser quand vous implémenterez input :
"Entrez le nombre total de trajets à effectuer : "
"""
x = int(input("Entrez le nombre total de trajets à effectuer :"))

carnet_trente = x // 30
reste = x % 30
carnet_dix = reste // 10
reste = reste % 10
billets_simples = reste

total = carnet_trente * 75 + carnet_dix * 30 + billets_simples * 3.75

print(f"Carnets de 30 billets - {carnet_trente}")
print(f"Carnets de 10 billets - {carnet_dix}")
print(f"Billets simples - {billets_simples}")
print(f"Prix total - {total:.2f}$")















# TODO: Lire n via input (prompt EXACT) et convertir en int


# TODO: calculer la répartition exacte (30 -> 10 -> 1)


# TODO: Calcul prix total


# TODO: Affichage des résultats de la répartition exacte (4 lignes)


# TODO: BONUS (optionnel)

