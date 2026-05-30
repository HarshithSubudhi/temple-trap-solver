import pytest
from temple_trap.config import LEVELS
from temple_trap.engine import GameState
from temple_trap.solver import astar_solver

@pytest.mark.parametrize("level_name", list(LEVELS.keys()))
def test_all_preset_levels(level_name):
    lvl = LEVELS[level_name]
    state = GameState(lvl['board'].copy(), lvl['pawn_pos'], "Ground", lvl['orientation'].copy())
    path, cost = astar_solver(state)
    assert path is not None, f"Level {level_name} should return a valid solution."
    assert cost > 0