"""
Fonctions liées aux tirs et à la détection des navires coulés.

Ce fichier contient :
 is_valid_shot : vérifie si un tir est possible
 shoot : exécute un tir et retourne le symbole obtenu
 is_ship_sunk : indique si au moins un navire est entièrement coulé
 count_sunk_ships : compte le nombre de navires coulés
 is_fleet_destroyed : indique si toute la flotte est détruite
"""

from constantes import (
    N_ROWS,
    N_COLS,
    SHIP_SYMBOL,
    HIT_SYMBOL,
    MISS_SYMBOL,
)


def is_valid_shot(grid: list[list[str]], row: int, col: int) -> bool:
    """
    Vérifie si un tir est possible sur la grille donnée.

    Un tir est valide si :
    - les coordonnées sont dans les limites de la grille,
    - la case n'a pas déjà été visée (ni 'X' ni 'O').

    Args:
        grid (list[list[str]]): la grille de tir (mémorise les tirs déjà faits).
        row (int): indice de ligne (0 à N_ROWS-1).
        col (int): indice de colonne (0 à N_COLS-1).

    Returns:
        bool: True si le tir est valide, False sinon.
    """
    # Limites
    if row < 0 or row >= N_ROWS:
        return False
    if col < 0 or col >= N_COLS:
        return False

    # Case déjà visée ?
    if grid[row][col] == HIT_SYMBOL or grid[row][col] == MISS_SYMBOL:
        return False

    return True


def shoot(grid: list[list[str]], row: int, col: int) -> str:
    """
    Exécute un tir sur la grille adverse

     Si la case contient un navire ('N'), elle devient 'X' et on retourne 'X'
     Si la case est vide ('.'), elle devient 'O' et on retourne 'O'
     Si le tir est invalide (déjà visé), rien n'est modifié et on retourne ''


        grid (list[list[str]]): la grille adverse
        row (int): indice de ligne
        col (int): indice de colonne

    Returns:
        str: HIT_SYMBOL si touché, MISS_SYMBOL si à l'eau, '' sinon
    """
    if not is_valid_shot(grid, row, col):
        return ""

    if grid[row][col] == SHIP_SYMBOL:
        grid[row][col] = HIT_SYMBOL
        return HIT_SYMBOL
    else:
        grid[row][col] = MISS_SYMBOL
        return MISS_SYMBOL


def _is_ship_cell(value: str) -> bool:
    """
    Indique si une case fait partie d'un navire (intact ou touché)

   
        value (str): symbole d'une case

    Returns:
        bool: True si la case est 'N' ou 'X'
    """
    return value == SHIP_SYMBOL or value == HIT_SYMBOL


def _find_ship_cells(grid: list[list[str]], start_row: int, start_col: int) -> list[tuple[int, int]]:
    """
    Retourne la liste des cases (row, col) d'un navire à partir de son début

    On suppose que (start_row, start_col) est le DÉBUT d'un navire
    (c'est-à-dire qu'aucune case du navire n'est à gauche ou au-dessus)

   
        grid (list[list[str]]): la grille
        start_row (int): ligne du début du navire
        start_col (int): colonne du début du navire

    Returns:
        list[tuple[int, int]]: les cases occupées par le navire
    """
    cells = [(start_row, start_col)]

    # Cas horizontal : la case à droite fait partie du navire
    if start_col + 1 < N_COLS and _is_ship_cell(grid[start_row][start_col + 1]):
        c = start_col + 1
        while c < N_COLS and _is_ship_cell(grid[start_row][c]):
            cells.append((start_row, c))
            c += 1
    # Cas vertical : la case en dessous fait partie du navire
    elif start_row + 1 < N_ROWS and _is_ship_cell(grid[start_row + 1][start_col]):
        r = start_row + 1
        while r < N_ROWS and _is_ship_cell(grid[r][start_col]):
            cells.append((r, start_col))
            r += 1

    return cells


def _list_all_ships(grid: list[list[str]]) -> list[list[tuple[int, int]]]:
    """
    Liste tous les navires présents sur la grille

    Chaque navire est représenté par la liste de ses cases (row, col)

   
        grid (list[list[str]]): la grille

    Returns:
        list[list[tuple[int, int]]]: la liste des navires
    """
    ships = []

    for r in range(N_ROWS):
        for c in range(N_COLS):
            if not _is_ship_cell(grid[r][c]):
                continue

            # Est-ce le DÉBUT d'un navire ?
            left_is_ship = (c > 0) and _is_ship_cell(grid[r][c - 1])
            above_is_ship = (r > 0) and _is_ship_cell(grid[r - 1][c])
            if left_is_ship or above_is_ship:
                continue   # pas le début, on l'a déjà vu

            ships.append(_find_ship_cells(grid, r, c))

    return ships


def is_ship_sunk(grid: list[list[str]]) -> bool:
    """
    Indique si AU MOINS un navire de la grille est entièrement coulé

    Un navire est coulé si toutes ses cases valent 'X'

        grid (list[list[str]]): la grille
    Returns:
        bool: True si au moins un navire est entièrement coulé, False sinon
    """
    ships = _list_all_ships(grid)
    for ship in ships:
        all_hit = True
        for (r, c) in ship:
            if grid[r][c] != HIT_SYMBOL:
                all_hit = False
                break
        if all_hit:
            return True
    return False


def count_sunk_ships(grid: list[list[str]]) -> int:
    """
    Compte le nombre de navires entièrement coulés sur la grille

    
        grid (list[list[str]]): la grille

    Returns:
        int: nombre de navires coulés
    """
    count = 0
    ships = _list_all_ships(grid)
    for ship in ships:
        all_hit = True
        for (r, c) in ship:
            if grid[r][c] != HIT_SYMBOL:
                all_hit = False
                break
        if all_hit:
            count += 1
    return count


def is_fleet_destroyed(grid: list[list[str]]) -> bool:
    """
    Indique si TOUS les navires de la grille sont détruits

    Autrement dit : plus aucune case 'N' sur la grille
    
        grid (list[list[str]]): la grille

    Returns:
        bool: True si la flotte est entièrement détruite, False sinon
    """
    for r in range(N_ROWS):
        for c in range(N_COLS):
            if grid[r][c] == SHIP_SYMBOL:
                return False
    return True