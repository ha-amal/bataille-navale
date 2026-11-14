"""
Constantes globales du jeu de bataille navale

Ce fichier regroupe toutes les valeurs fixes du jeu :
 les dimensions des grilles
 les symboles utilisés sur les grilles
 la composition de la flotte

Centraliser ces valeurs ici évite de les répéter dans les autres fichiers
et facilite les modifications futures
"""

# ---------------------------------------------------------------------------
# Dimensions des grilles
# ---------------------------------------------------------------------------
# La grille fait 10 lignes sur 10 colonnes
N_ROWS = 10
N_COLS = 10

# ---------------------------------------------------------------------------
# Symboles utilisés pour représenter les cases
# ---------------------------------------------------------------------------
# '.' : case vide (pas de navire, pas encore touchée)
EMPTY_SYMBOL: str = '.'

# 'N' : case occupée par un navire (intact)
SHIP_SYMBOL: str = 'N'

# 'X' : case d'un navire qui a été touchée
HIT_SYMBOL: str = 'X'

# 'O' : case vide qui a été visée (tir dans l'eau)
MISS_SYMBOL: str = 'O'

# ---------------------------------------------------------------------------
# Composition de la flotte
# ---------------------------------------------------------------------------
# Chaque navire est représenté par un couple (nom, taille)
# L'ordre de cette liste est l'ordre dans lequel les joueurs placeront
# leurs navires
FLEET: list[tuple[str, int]] = [
    ("Porte-avions", 5),
    ("Croiseur", 4),
    ("Contre-torpilleur", 3),
    ("Sous-marin", 3),
    ("Torpilleur", 2),
]

# ---------------------------------------------------------------------------
# Autres constantes utiles
# ---------------------------------------------------------------------------
# Nombre de joueurs dans la partie
N_PLAYERS = 2

# Nombre de lignes vides affichées pour "effacer" l'écran en console
SCREEN_CLEAR_LINES = 50