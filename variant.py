RANKS = 9
FILES = 9
SQUARES = RANKS * FILES
PIECE_TYPES = 10
PIECES = 2 * PIECE_TYPES
USE_POCKETS = True
POCKETS = 2 * FILES if USE_POCKETS else 0

PIECE_VALUES = {
    1: 425,
    2: 676,
    3: 360,
    4: 900,
    5: 50,
    6: 200,
    7: 220,
    8: 360,
    9: 750,
}