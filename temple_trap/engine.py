from collections import deque
from .config import ROWS, COLS, TILES_DEF

# Global cache for open sides of tiles
_OPEN_SIDES_CACHE = {}

def get_open_sides(tile_id, layer, rotation):
    key = (tile_id, layer, rotation)
    if key not in _OPEN_SIDES_CACHE:
        top_opens, ground_opens, _, _ = TILES_DEF[tile_id]
        order = ["I", "II", "III", "IV"]
        sides = top_opens if layer == "Top" else ground_opens
        _OPEN_SIDES_CACHE[key] = {order[(order.index(s) + rotation) % 4] for s in sides}
    return _OPEN_SIDES_CACHE[key]

class GameState:
    __slots__ = ('tiles', 'rotations', 'pawn', 'layer', 'blank', '_hash', '_dist_map')

    def __init__(self, tiles, rotations, pawn, layer):
        self.tiles = tuple(tiles)
        self.rotations = tuple(rotations)
        self.pawn = pawn
        self.layer = layer
        self.blank = self.tiles.index(" ")
        # Precompute the hash for fast O(1) state lookup
        self._hash = hash((self.tiles, self.rotations, self.pawn, self.layer))
        self._dist_map = None  # Lazily evaluated and cached

    def __hash__(self):
        return self._hash

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, GameState):
            return False
        return (self.pawn == other.pawn and
                self.layer == other.layer and
                self.tiles == other.tiles and
                self.rotations == other.rotations)

    def tile_at(self, idx):
        return self.tiles[idx]

    def get_distances(self):
        if self._dist_map is None:
            self._dist_map = self._compute_pawn_distances()
        return self._dist_map

    def can_slide(self, tile_idx):
        if tile_idx == self.blank or self.pawn == tile_idx:
            return False
        # Check if adjacent (Manhattan distance = 1 on 3x3 grid)
        r1, c1 = divmod(tile_idx, 3)
        r2, c2 = divmod(self.blank, 3)
        return abs(r1 - r2) + abs(c1 - c2) == 1

    def slide(self, tile_idx):
        # Returns a new GameState representing the slide transition
        new_tiles = list(self.tiles)
        new_rotations = list(self.rotations)
        new_tiles[self.blank], new_tiles[tile_idx] = new_tiles[tile_idx], new_tiles[self.blank]
        new_rotations[self.blank], new_rotations[tile_idx] = new_rotations[tile_idx], new_rotations[self.blank]
        return GameState(new_tiles, new_rotations, self.pawn, self.layer)

    def _compute_pawn_distances(self):
        # BFS traversal to find shortest path to all reachable (cell, layer) positions
        start = (self.pawn, self.layer)
        dq = deque([start])
        dist = {start: 0}

        while dq:
            idx, layer = dq.popleft()
            d = dist[(idx, layer)]

            # Handle stairs transition on the same cell (cost = 0)
            tile = self.tiles[idx]
            if TILES_DEF[tile][3]:  # If the tile contains stairs
                other = (idx, "Top" if layer == "Ground" else "Ground")
                if other not in dist:
                    dist[other] = d
                    dq.appendleft(other)  # 0-cost transition: process first

            # Neighbors (Up, Down, Left, Right)
            r, c = divmod(idx, 3)
            
            # Up
            if r > 0:
                nidx = idx - 3
                if self.tiles[nidx] != " ":
                    opens_from = get_open_sides(tile, layer, self.rotations[idx])
                    opens_to = get_open_sides(self.tiles[nidx], layer, self.rotations[nidx])
                    if ("I" in opens_from) and ("III" in opens_to):
                        nxt = (nidx, layer)
                        if nxt not in dist:
                            dist[nxt] = d + 1
                            dq.append(nxt)
            # Down
            if r < 2:
                nidx = idx + 3
                if self.tiles[nidx] != " ":
                    opens_from = get_open_sides(tile, layer, self.rotations[idx])
                    opens_to = get_open_sides(self.tiles[nidx], layer, self.rotations[nidx])
                    if ("III" in opens_from) and ("I" in opens_to):
                        nxt = (nidx, layer)
                        if nxt not in dist:
                            dist[nxt] = d + 1
                            dq.append(nxt)
            # Left
            if c > 0:
                nidx = idx - 1
                if self.tiles[nidx] != " ":
                    opens_from = get_open_sides(tile, layer, self.rotations[idx])
                    opens_to = get_open_sides(self.tiles[nidx], layer, self.rotations[nidx])
                    if ("IV" in opens_from) and ("II" in opens_to):
                        nxt = (nidx, layer)
                        if nxt not in dist:
                            dist[nxt] = d + 1
                            dq.append(nxt)
            # Right
            if c < 2:
                nidx = idx + 1
                if self.tiles[nidx] != " ":
                    opens_from = get_open_sides(tile, layer, self.rotations[idx])
                    opens_to = get_open_sides(self.tiles[nidx], layer, self.rotations[nidx])
                    if ("II" in opens_from) and ("IV" in opens_to):
                        nxt = (nidx, layer)
                        if nxt not in dist:
                            dist[nxt] = d + 1
                            dq.append(nxt)
        return dist

    def __str__(self):
        rows = []
        for r in range(ROWS):
            row = self.tiles[r*COLS:(r+1)*COLS]
            rows.append(" | ".join(row))
        return f"Board:\n" + "\n".join(rows) + f"\nPawn:{self.pawn} Layer:{self.layer} Blank:{self.blank}"