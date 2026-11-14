"""
Fonctions de création et d'affichage des grilles

Une grille est une liste de listes : chaque élément de la liste principale
est une ligne (elle-même une liste de symboles)
"""

from constantes import N_ROWS, N_COLS, EMPTY_SYMBOL


def create_grid() -> list[list[str]]:
    """
    Crée et retourne une grille vide de N_ROWS lignes et N_COLS colonnes

    Chaque case est initialisée avec le symbole EMPTY_SYMBOL ('.')

    Returns:
        list[list[str]]: une grille 2D remplie de '.'
    """
    grid = []

    # On répète N_ROWS fois la création d'une ligne
    for _ in range(N_ROWS):
        # On crée une nouvelle ligne vide (N_COLS cases)
        row = []
        for _ in range(N_COLS):
            row.append(EMPTY_SYMBOL)
        # On ajoute cette ligne à la grille
        grid.append(row)

    return grid


def display_grid(grid: list[list[str]]) -> None:
    """
    Affiche une grille dans la console

    Les lignes et les colonnes sont numérotées de 1 à N_ROWS / N_COLS 
    pour que le joueur puisse saisir des coordonnées entre 1 et 10.

    Args:
        grid (list[list[str]]): la grille à afficher.
    """
    # ------------------------------------------------------------------
    # 1) En-tête des colonnes
    # ------------------------------------------------------------------
    # On commence par 3 espaces pour s'aligner sous les numéros de ligne
    # Puis on affiche "1 2 3 ... 10" séparés par des espaces
    header = "   "
    for col in range(1, N_COLS + 1):
        header = header + str(col) + " "
    print(header)

    # ------------------------------------------------------------------
    # 2) Ligne de séparation
    # ------------------------------------------------------------------
    print(" " + "-" * (2 * N_COLS + 1))

    # ------------------------------------------------------------------
    # 3) Chaque ligne de la grille
    # ------------------------------------------------------------------
    for row_index in range(N_ROWS):
        # On construit le contenu de la ligne : chaque case suivie d'un espace
        line_content = ""
        for col_index in range(N_COLS):
            line_content = line_content + grid[row_index][col_index] + " "

        # On affiche le numéro de ligne (aligné sur 2 caractères)
        # puis " | ", puis le contenu, puis " |"
        print(f"{row_index + 1:2d} | {line_content}|")