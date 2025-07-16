# EX1.PY Documentation

Ce script calcule le temps d'attente moyen pour une série de positions et compare différentes méthodes de tri de ces positions pour minimiser le temps d'attente. Il inclut des fonctions pour calculer le temps d'attente moyen, trier les positions et générer des ordres de nettoyage.

## Fonctions

### `average_waiting_time(positions)`
Calcule le temps d'attente moyen pour une liste donnée de positions.

- **Paramètres :**
    - `positions` (liste) : Une liste de positions (entiers ou flottants).

- **Retourne :**
    - `float` : Le temps d'attente moyen.

### `ex2func(positions)`
Compare différentes méthodes de tri des positions pour minimiser le temps d'attente moyen.

- **Paramètres :**
    - `positions` (liste) : Une liste de positions (entiers ou flottants).

- **Retourne :**
    - `dict` : Un dictionnaire contenant les temps d'attente moyens pour l'ordre trié, l'ordre du plus proche voisin et l'ordre original.

### `parcours(house_positions)`
Génère un ordre de nettoyage en triant les positions et en inversant l'ordre des positions négatives.

- **Paramètres :**
    - `house_positions` (liste) : Une liste de positions de maisons (entiers ou flottants).

- **Retourne :**
    - `liste` : L'ordre de nettoyage.

### `parcoursOnSQR(gL)`
Génère un ordre de nettoyage basé sur l'approche du plus proche voisin.

- **Paramètres :**
    - `gL` (liste) : Une liste de positions (entiers ou flottants).

- **Retourne :**
    - `liste` : L'ordre de nettoyage.

## Exécution Principale

Le script effectue les tâches suivantes :
1. Calcule et affiche le temps d'attente moyen pour des listes prédéfinies de positions (`positions_list` et `positions_list_b`).
2. Compare différentes méthodes de tri pour une liste d'exemple de positions (`positions_example`) et affiche les résultats.
3. Génère des tableaux aléatoires de positions, calcule le temps d'attente moyen pour différents ordres de nettoyage (`parcours` et `parcoursOnSQR`), et affiche les temps d'attente moyens sur 1000 itérations.