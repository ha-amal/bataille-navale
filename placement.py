"""
Fonctions de placement des navires sur une grille.

Ce fichier contient :
 is_valid_placement : vérifie si un navire peut être placé
 place_ship : place un navire si le placement est valide
 place_fleet : laisse le joueur placer toute sa flotte
"""

from constantes import (
    N_ROWS, N_COLS,  EMPTY_SYMBOL,
    SHIP_SYMBOL,
    FLEET,
)
from grille import display_grid


def is_valid_placement(
    grid: list[list[str]],
    row: int,
    col: int,
    size: int,
    orientation: str
) -> bool:
    """
    Vérifie si un navire peut être placé sur la grille

    
        grid (list[list[str]]): la grille sur laquelle on veut placer
        row (int): indice de ligne de départ (0 à N_ROWS-1)
        col (int): indice de colonne de départ (0 à N_COLS-1)
        size (int): taille du navire.
        orientation (str): 'H' pour horizontal, 'V' pour vertical

    Returns:
        bool: True si le placement est valide, False sinon
    """
    # ------------------------------------------------------------------
    # 1) Vérifier que l'orientation est valide
    # ------------------------------------------------------------------
    if orientation != 'H' and orientation != 'V':
        return False

    # ------------------------------------------------------------------
    # 2) Vérifier les limites de la grille
    # ------------------------------------------------------------------
    if row < 0 or col < 0:
        return False

    if orientation == 'H':
        # En horizontal, on ajoute size-1 à la colonne
        if col + size > N_COLS:
            return False
    else:
        # En vertical, on ajoute size-1 à la ligne
        if row + size > N_ROWS:
            return False

    # ------------------------------------------------------------------
    # 3) Vérifier que toutes les cases sont libres
    # ------------------------------------------------------------------
    for i in range(size):
        if orientation == 'H':
            current_row = row
            current_col = col + i
        else:
            current_row = row + i
            current_col = col

        # Si la case n'est pas vide, le placement est invalide
        if grid[current_row][current_col] != EMPTY_SYMBOL:
            return False

    # Si on arrive ici, tout est bon
    return True


def place_ship(
    grid: list[list[str]],
    row: int,
    col: int,
    size: int,
    orientation: str
) -> bool:
    """
    Place un navire sur la grille si le placement est valide

    
        grid (list[list[str]]): la grille sur laquelle placer
        row (int): indice de ligne de départ (0 à N_ROWS-1)
        col (int): indice de colonne de départ (0 à N_COLS-1)
        size (int): taille du navire
        orientation (str): 'H' ou 'V'

    Returns:
        bool: True si le navire a été placé, False sinon
    """
    # On vérifie d'abord grâce à is_valid_placement
    if not is_valid_placement(grid, row, col, size, orientation):
        return False

    # Le placement est valide : on pose les cases 'N'
    for i in range(size):
        if orientation == 'H':
            grid[row][col + i] = SHIP_SYMBOL
        else:
            grid[row + i][col] = SHIP_SYMBOL

    return True


def ask_coordinate(message: str) -> int:
    """
    Demande à l'utilisateur de saisir un entier entre 1 et N_ROWS (ou N_COLS)

    Tant que la saisie est invalide (pas un nombre, ou hors limites)
    la fonction redemande Ne plante jamais le programme

    
        message (str): message à afficher pour guider l'utilisateur

    Returns:
        int: un entier valide entre 1 et 10 (inclus)
    """
    while True:
        saisie = input(message)

        try:
            valeur = int(saisie)
        except ValueError:
            print("Erreur : ce n'est pas un nombre entier \nRéessayez.")
            continue

        if valeur < 1 or valeur > N_ROWS:
            print(f"Erreur : le nombre doit être entre 1 et {N_ROWS}.")
            continue

        return valeur


def ask_orientation() -> str:
    """
    Demande à l'utilisateur de choisir une orientation ('H' ou 'V')

    Tant que la saisie n'est pas 'H' ou 'V' (majuscule ou minuscule)
    la fonction redemande

    Returns:
        str: 'H' ou 'V' (toujours en majuscule)
    """
    while True:
        saisie = input("Orientation (H = horizontal, V = vertical) : ")
        saisie = saisie.strip().upper()   # enlève les espaces (strip) et met en majuscule (upper)

        if saisie == 'H' or saisie == 'V':
            return saisie

        print("Erreur : tapez H ou V.")


def place_fleet(grid: list[list[str]]) -> None:
    """
    Permet au joueur de placer tous les navires de sa flotte

    Pour chaque navire, on demande la ligne, la colonne et l'orientation
    Tant que le placement est invalide, on redemande
    La grille est affichée avant chaque navire pour aider le joueur

  
        grid (list[list[str]]): la grille du joueur
    """
    for nom, taille in FLEET:
        placement_ok = False

        while not placement_ok:
            print()
            print(f"=== Placement du navire : {nom} ({taille} cases) ===")
            display_grid(grid)
            print()

            ligne = ask_coordinate("Numéro de ligne (1-10) : ")
            colonne = ask_coordinate("Numéro de colonne (1-10) : ")
            orientation = ask_orientation()

            # Conversion en indices Python (0 à 9)
            row = ligne - 1
            col = colonne - 1

            if place_ship(grid, row, col, taille, orientation):
                print(f"Le {nom} a bien été placé !")
                placement_ok = True
            else:
                print("Placement impossible : le navire dépasse ou se superpose.")
                print("Veuillez réessayer.")

    # Afficher la grille finale du joueur
    print()
    print("=== Votre flotte finale ===")
    display_grid(grid)