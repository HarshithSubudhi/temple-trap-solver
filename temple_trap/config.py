ROWS, COLS = 3, 3

LEVELS = {
    # STARTER (1-12)
    'level-1': {
        'board': ['+', '◊', 'X', '◻', ' ', 'O', '=', '∗', '▷'],
        'pawn_pos': 8,
        'orientation': [0, 0, 2, 1, 0, 3, 0, 0, 2]
    },
    'level-2': {
        'board': ['=', '∗', 'X', '◻', ' ', '◊', 'O', '+', '▷'],
        'pawn_pos': 1,
        'orientation': [2, 3, 0, 0, 0, 0, 0, 2, 2]
    },
    'level-3': {
        'board': ['X', '∗', '◻', '◊', 'O', '▷', '=', ' ', '+'],
        'pawn_pos': 1,
        'orientation': [2, 1, 3, 0, 3, 0, 0, 0, 1]
    },
    'level-4': {
        'board': ['◻', '◊', 'O', '∗', 'X', '▷', ' ', '=', '+'],
        'pawn_pos': 3,
        'orientation': [1, 0, 2, 1, 0, 3, 0, 0, 0]
    },
    'level-5': {
        'board': ['◻', '+', '=', '∗', ' ', '◊', 'X', '▷', 'O'],
        'pawn_pos': 8,
        'orientation': [1, 0, 2, 1, 0, 1, 0, 3, 0]
    },
    'level-6': {
        'board': ['X', 'O', '∗', '◊', '▷', ' ', '=', '◻', '+'],
        'pawn_pos': 2,
        'orientation': [2, 1, 2, 0, 0, 0, 2, 3, 1]
    },
    'level-7': {
        'board': ['=', '◻', '+', '◊', 'O', ' ', '∗', 'X', '▷'],
        'pawn_pos': 8,
        'orientation': [2, 1, 0, 1, 1, 0, 1, 0, 3]
    },
    'level-8': {
        'board': [' ', 'O', '◊', '∗', '▷', '◻', '+', 'X', '='],
        'pawn_pos': 3,
        'orientation': [0, 1, 2, 0, 3, 1, 0, 1, 2]
    },
    'level-9': {
        'board': ['◊', 'X', '∗', '+', '▷', 'O', '◻', '=', ' '],
        'pawn_pos': 5,
        'orientation': [0, 1, 2, 0, 0, 3, 1, 0, 0]
    },
    'level-10': {
        'board': ['+', '=', '◻', 'O', '∗', '◊', 'X', '▷', ' '],
        'pawn_pos': 7,
        'orientation': [0, 0, 2, 1, 2, 0, 0, 2, 0]
    },
    'level-11': {
        'board': ['◊', '▷', '+', '∗', 'O', ' ', 'X', '◻', '='],
        'pawn_pos': 6,
        'orientation': [0, 2, 3, 0, 3, 0, 0, 1, 2]
    },
    'level-12': {
        'board': ['◻', '+', '◊', '=', ' ', 'X', '∗', '▷', 'O'],
        'pawn_pos': 8,
        'orientation': [1, 0, 0, 0, 0, 2, 3, 1, 3]
    },

    # JUNIOR (13-24)
    'level-13': {
        'board': ['∗', '▷', 'X', '=', '+', '◻', '◊', 'O', ' '],
        'pawn_pos': 2,
        'orientation': [0, 1, 3, 0, 0, 3, 1, 1, 0]
    },
    'level-14': {
        'board': ['▷', '+', '◻', '◊', ' ', 'X', '∗', '=', 'O'],
        'pawn_pos': 0,
        'orientation': [2, 1, 2, 3, 0, 3, 1, 2, 2]
    },
    'level-15': {
        'board': ['◊', '+', '◻', '∗', '▷', 'X', '=', 'O', ' '],
        'pawn_pos': 4,
        'orientation': [1, 0, 2, 0, 2, 2, 2, 0, 0]
    },
    'level-16': {
        'board': ['+', '◊', 'X', ' ', '◻', '=', '∗', '▷', 'O'],
        'pawn_pos': 1,
        'orientation': [0, 3, 3, 0, 3, 2, 2, 1, 2]
    },
    'level-17': {
        'board': ['X', '▷', '∗', '=', '◻', '+', 'O', ' ', '◊'],
        'pawn_pos': 6,
        'orientation': [2, 1, 3, 2, 1, 1, 0, 0, 1]
    },
    'level-18': {
        'board': ['+', '∗', 'X', '▷', ' ', '◊', 'O', '◻', '='],
        'pawn_pos': 5,
        'orientation': [0, 0, 1, 0, 0, 2, 0, 3, 1]
    },
    'level-19': {
        'board': ['+', '=', '◻', '◊', '∗', 'X', ' ', '▷', 'O'],
        'pawn_pos': 5,
        'orientation': [1, 0, 2, 2, 0, 2, 0, 2, 1]
    },
    'level-20': {
        'board': ['X', 'O', '+', '◻', ' ', '◊', '=', '∗', '▷'],
        'pawn_pos': 7,
        'orientation': [2, 0, 1, 1, 0, 0, 0, 0, 2]
    },
    'level-21': {
        'board': ['=', '◻', ' ', '∗', '◊', '+', 'X', 'O', '▷'],
        'pawn_pos': 3,
        'orientation': [1, 2, 0, 1, 1, 1, 0, 3, 0]
    },
    'level-22': {
        'board': ['=', '◻', ' ', '∗', '◊', 'X', '+', '▷', 'O'],
        'pawn_pos': 7,
        'orientation': [0, 2, 0, 2, 0, 2, 0, 0, 3]
    },
    'level-23': {
        'board': ['=', '◻', '∗', ' ', 'X', 'O', '◊', '▷', '+'],
        'pawn_pos': 6,
        'orientation': [0, 2, 1, 0, 1, 3, 0, 3, 1]
    },
    'level-24': {
        'board': ['X', '+', 'O', '▷', '◊', '◻', ' ', '=', '∗'],
        'pawn_pos': 0,
        'orientation': [1, 2, 3, 0, 2, 2, 0, 1, 1]
    },

    # EXPERT (25-36)
    'level-25': {
        'board': ['◊', '◻', '+', 'X', '▷', '=', 'O', '∗', ' '],
        'pawn_pos': 0,
        'orientation': [1, 2, 3, 0, 2, 3, 3, 1, 0]
    },
    'level-26': {
        'board': ['◻', '=', '◊', '+', '▷', 'X', ' ', 'O', '∗'],
        'pawn_pos': 4,
        'orientation': [2, 0, 1, 0, 2, 1, 0, 3, 3]
    },
    'level-27': {
        'board': ['+', '=', ' ', '◻', 'O', '◊', '∗', 'X', '▷'],
        'pawn_pos': 5,
        'orientation': [1, 2, 0, 0, 1, 2, 0, 0, 2]
    },
    'level-28': {
        'board': ['◻', '◊', '▷', '=', '∗', 'X', 'O', '+', ' '],
        'pawn_pos': 5,
        'orientation': [1, 0, 2, 0, 0, 2, 0, 1, 0]
    },
    'level-29': {
        'board': [' ', 'X', 'O', '◻', '◊', '▷', '=', '+', '∗'],
        'pawn_pos': 8,
        'orientation': [0, 0, 2, 1, 0, 3, 0, 0, 0]
    },
    'level-30': {
        'board': ['O', '◻', 'X', '∗', ' ', '▷', '=', '+', '◊'],
        'pawn_pos': 2,
        'orientation': [3, 2, 1, 3, 0, 0, 0, 2, 0]
    },
    'level-31': {
        'board': [' ', '◻', '=', '+', '∗', 'O', '◊', 'X', '▷'],
        'pawn_pos': 7,
        'orientation': [0, 3, 2, 0, 0, 2, 2, 1, 3]
    },
    'level-32': {
        'board': ['◻', ' ', 'X', '∗', '◊', '▷', '=', 'O', '+'],
        'pawn_pos': 7,
        'orientation': [2, 0, 2, 1, 1, 3, 1, 3, 2]
    },
    'level-33': {
        'board': ['+', '◻', ' ', '◊', '▷', 'X', '∗', 'O', '='],
        'pawn_pos': 7,
        'orientation': [1, 1, 0, 2, 0, 2, 0, 3, 3]
    },
    'level-34': {
        'board': ['+', '=', '◻', ' ', '∗', 'X', '▷', 'O', '◊'],
        'pawn_pos': 8,
        'orientation': [1, 2, 3, 0, 1, 2, 1, 0, 2]
    },
    'level-35': {
        'board': ['+', '∗', '=', '▷', 'X', 'O', ' ', '◊', '◻'],
        'pawn_pos': 7,
        'orientation': [3, 1, 2, 1, 2, 1, 0, 3, 0]
    },
    'level-36': {
        'board': ['◊', 'O', '▷', '∗', ' ', 'X', '=', '◻', '+'],
        'pawn_pos': 5,
        'orientation': [3, 1, 2, 1, 0, 0, 3, 2, 1]
    },

    # MASTER (37-48)
    'level-37': {
        'board': ['X', 'O', '+', ' ', '▷', '∗', '=', '◊', '◻'],
        'pawn_pos': 0,
        'orientation': [1, 2, 3, 0, 2, 3, 0, 0, 3]
    },
    'level-38': {
        'board': ['=', '+', '◻', '◊', 'O', 'X', '▷', ' ', '∗'],
        'pawn_pos': 6,
        'orientation': [0, 3, 2, 0, 3, 1, 0, 0, 3]
    },
    'level-39': {
        'board': ['∗', '◻', '=', '+', 'X', 'O', '◊', '▷', ' '],
        'pawn_pos': 6,
        'orientation': [1, 2, 1, 3, 1, 1, 0, 3, 0]
    },
    'level-40': {
        'board': ['◻', ' ', '=', 'X', '∗', 'O', '+', '▷', '◊'],
        'pawn_pos': 7,
        'orientation': [2, 0, 1, 1, 1, 3, 2, 0, 0]
    },
    'level-41': {
        'board': ['+', '◊', '◻', 'X', '▷', ' ', '=', '∗', 'O'],
        'pawn_pos': 3,
        'orientation': [2, 0, 2, 1, 3, 0, 0, 2, 0]
    },
    'level-42': {
        'board': ['▷', 'X', '◻', ' ', 'O', '∗', '◊', '+', '='],
        'pawn_pos': 0,
        'orientation': [1, 2, 2, 0, 0, 2, 2, 0, 3]
    },
    'level-43': {
        'board': ['=', '▷', '∗', '+', 'X', 'O', '◻', ' ', '◊'],
        'pawn_pos': 4,
        'orientation': [0, 2, 1, 0, 1, 2, 2, 0, 3]
    },
    'level-44': {
        'board': ['◻', '+', 'X', 'O', ' ', '=', '▷', '∗', '◊'],
        'pawn_pos': 3,
        'orientation': [0, 3, 3, 2, 0, 2, 0, 2, 0]
    },
    'level-45': {
        'board': ['X', '∗', '◊', '◻', ' ', '▷', '=', 'O', '+'],
        'pawn_pos': 7,
        'orientation': [1, 2, 0, 2, 0, 3, 0, 0, 3]
    },
    'level-46': {
        'board': ['∗', 'X', '▷', ' ', 'O', '◊', '=', '◻', '+'],
        'pawn_pos': 2,
        'orientation': [1, 1, 2, 0, 3, 3, 1, 2, 1]
    },
    'level-47': {
        'board': ['∗', '◻', 'X', ' ', '+', 'O', '▷', '=', '◊'],
        'pawn_pos': 8,
        'orientation': [2, 2, 2, 0, 1, 2, 2, 0, 0]
    },
    'level-48': {
        'board': [' ', '▷', '∗', 'X', '=', '+', 'O', '◊', '◻'],
        'pawn_pos': 7,
        'orientation': [0, 3, 0, 2, 1, 2, 3, 1, 0]
    },

    # WIZARD (49-60)
    'level-49': {
        'board': ['▷', 'X', ' ', '=', '+', '◻', '◊', '∗', 'O'],
        'pawn_pos': 6,
        'orientation': [1, 3, 0, 1, 2, 3, 1, 0, 0]
    },
    'level-50': {
        'board': ['+', 'X', '◻', '∗', '▷', ' ', 'O', '=', '◊'],
        'pawn_pos': 3,
        'orientation': [1, 1, 2, 0, 3, 0, 0, 0, 2]
    },
    'level-51': {
        'board': [' ', '=', '▷', 'O', '◻', 'X', '◊', '+', '∗'],
        'pawn_pos': 8,
        'orientation': [0, 2, 1, 0, 3, 3, 2, 2, 0]
    },
    'level-52': {
        'board': ['∗', '◻', ' ', 'X', '=', '◊', '+', 'O', '▷'],
        'pawn_pos': 8,
        'orientation': [2, 2, 0, 1, 0, 0, 2, 0, 3]
    },
    'level-53': {
        'board': ['X', 'O', '+', ' ', '=', '∗', '◊', '◻', '▷'],
        'pawn_pos': 5,
        'orientation': [3, 0, 2, 0, 1, 0, 2, 3, 1]
    },
    'level-54': {
        'board': ['+', '=', '◻', '◊', 'X', '▷', '∗', 'O', ' '],
        'pawn_pos': 4,
        'orientation': [1, 1, 2, 1, 1, 3, 1, 3, 0]
    },
    'level-55': {
        'board': ['=', 'X', '◻', '▷', '◊', '∗', ' ', '+', 'O'],
        'pawn_pos': 5,
        'orientation': [1, 1, 2, 1, 2, 0, 0, 2, 0]
    },
    'level-56': {
        'board': ['X', '◊', 'O', '+', '◻', '∗', '▷', ' ', '='],
        'pawn_pos': 5,
        'orientation': [2, 3, 1, 1, 0, 0, 1, 0, 1]
    },
    'level-57': {
        'board': ['◻', ' ', '+', '▷', '∗', '=', 'X', 'O', '◊'],
        'pawn_pos': 4,
        'orientation': [2, 0, 0, 1, 0, 0, 1, 0, 3]
    },
    'level-58': {
        'board': ['◻', '∗', 'O', '+', 'X', ' ', '=', '▷', '◊'],
        'pawn_pos': 4,
        'orientation': [3, 2, 0, 0, 3, 0, 2, 1, 2]
    },
    'level-59': {
        'board': ['◊', '▷', 'O', '◻', '+', '∗', 'X', '=', ' '],
        'pawn_pos': 5,
        'orientation': [2, 3, 2, 2, 1, 0, 3, 0, 0]
    },
    'level-60': {
        'board': ['▷', '=', ' ', 'O', '◻', '∗', '◊', '+', 'X'],
        'pawn_pos': 5,
        'orientation': [2, 1, 0, 2, 3, 0, 2, 1, 3]
    }
}

# Alias the old keys for backward compatibility
LEVELS['starter-1'] = LEVELS['level-1']
LEVELS['starter-2'] = LEVELS['level-2']
LEVELS['starter-3'] = LEVELS['level-3']
LEVELS['starter-4'] = LEVELS['level-4']
LEVELS['junior-1'] = LEVELS['level-17']
LEVELS['junior-2'] = LEVELS['level-18']
LEVELS['junior-3'] = LEVELS['level-19']
LEVELS['junior-4'] = LEVELS['level-20']
LEVELS['expert-1'] = LEVELS['level-25']
LEVELS['expert-2'] = LEVELS['level-26']
LEVELS['expert-3'] = LEVELS['level-27']
LEVELS['expert-4'] = LEVELS['level-28']

# Physical tiles structure definitions
TILES_DEF = {
    "=": ({"I", "II"}, set(), False, False),       # Tile A (Top opens = I, II; Ground = none; Hole: No; Stairs: No)
    "◻": ({"I", "II"}, set(), False, False),       # Tile B (Top opens = I, II; Ground = none; Hole: No; Stairs: No)
    "+": ({"II", "IV"}, set(), False, False),      # Tile C (Top opens = II, IV; Ground = none; Hole: No; Stairs: No)
    "◊": ({"IV"}, {"II"}, True, True),             # Tile D (Top opens = IV; Ground = II; Hole: Yes; Stairs: Yes)
    "∗": ({"IV"}, {"II"}, True, True),             # Tile E (Top opens = IV; Ground = II; Hole: Yes; Stairs: Yes)
    "▷": (set(), {"I", "II"}, True, False),        # Tile F (Top = none; Ground opens = I, II; Hole: Yes; Stairs: No)
    "X": (set(), {"I", "II"}, True, False),        # Tile G (Top = none; Ground opens = I, II; Hole: Yes; Stairs: No)
    "O": (set(), {"I", "II"}, True, False),        # Tile H (Top = none; Ground opens = I, II; Hole: Yes; Stairs: No)
    " ": (set(), set(), False, False),             # Empty space / water
}

ADJ_SIDES = {
    (-1, 0): ("I", "III"),
    (1, 0): ("III", "I"),
    (0, -1): ("IV", "II"),
    (0, 1): ("II", "IV"),
}