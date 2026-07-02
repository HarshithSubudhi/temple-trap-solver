import itertools
import heapq
from .config import TILES_DEF
from .engine import GameState, get_open_sides

def manhattan(idx1, idx2):
    r1, c1 = divmod(idx1, 3)
    r2, c2 = divmod(idx2, 3)
    return abs(r1 - r2) + abs(c1 - c2)

def heuristic(gs: GameState):
    h_pawn = manhattan(gs.pawn, 0)
    
    # Retrieve the cached/computed distance map
    dist_map = gs.get_distances()
    reachable_indices = {idx for idx, layer in dist_map.keys()}
    
    # If cell 0 is reachable, no blank tile penalty is needed
    if 0 in reachable_indices:
        return h_pawn
        
    # Blank Tile Penalty: Manhattan distance from blank tile to closest reachable cell
    blank_penalty = min(manhattan(gs.blank, r) for r in reachable_indices)
    return h_pawn + blank_penalty

def is_goal(gs: GameState):
    dist_map = gs.get_distances()
    
    # Rule 2.E: The exit of the maze is located on the top floor (Top layer)
    if (0, "Top") in dist_map:
        tile0 = gs.tile_at(0)
        if "IV" in get_open_sides(tile0, "Top", gs.rotations[0]):
            cost = dist_map[(0, "Top")]
            return "Top", cost + 1

    return None

def astar_solver(start_gs: GameState, max_steps=1000000):
    counter = itertools.count()
    open_heap = []
    # Heap stores: (f, count, g, state)
    heapq.heappush(open_heap, (heuristic(start_gs), next(counter), 0, start_gs))
    
    # visited map stores: state -> g_cost
    visited = {start_gs: 0}
    
    # parent_map stores: state -> (parent_state, action_tuple)
    parent_map = {}

    best_solution = None
    best_cost = None

    while open_heap:
        f, _, g, gs = heapq.heappop(open_heap)

        # If the smallest f on the heap is >= our best cost, we are guaranteed to have found the optimum!
        if best_cost is not None and f >= best_cost:
            break

        goal = is_goal(gs)
        if goal is not None:
            goal_layer, walk_cost = goal
            total_cost = g + walk_cost
            if best_cost is None or total_cost < best_cost:
                best_cost = total_cost
                # Reconstruct the path from goal state to start state
                path = [("walk", (0, goal_layer, walk_cost))]
                curr = gs
                while curr in parent_map:
                    parent, action = parent_map[curr]
                    path.append(action)
                    curr = parent
                path.reverse()
                best_solution = path

        if len(visited) > max_steps:
            break

        dist_map = gs.get_distances()

        # Try pawn walks to other resting locations
        for (dest_idx, dest_layer), walk_cost in dist_map.items():
            if dest_idx == gs.pawn and dest_layer == gs.layer:
                continue
            dest_tile = gs.tile_at(dest_idx)
            if dest_tile == " ":
                continue

            # Pawn can only rest on Ground of tiles with holes OR on Top of staircases (D, E)
            is_valid_rest = False
            if dest_layer == "Ground":
                if TILES_DEF[dest_tile][2]:  # Has hole (D, E, F, G, H)
                    is_valid_rest = True
            elif dest_layer == "Top":
                if TILES_DEF[dest_tile][3]:  # Contains stairs (D, E)
                    is_valid_rest = True

            if not is_valid_rest:
                continue

            new_g = g + walk_cost
            new_gs = GameState(gs.tiles, gs.rotations, dest_idx, dest_layer)
            if new_gs not in visited or new_g < visited[new_gs]:
                visited[new_gs] = new_g
                parent_map[new_gs] = (gs, ("walk", (dest_idx, dest_layer, walk_cost)))
                h = heuristic(new_gs)
                heapq.heappush(open_heap, (new_g + h, next(counter), new_g, new_gs))

        # Try sliding tiles into the blank space
        r_blank, c_blank = divmod(gs.blank, 3)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r_blank + dr, c_blank + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                nidx = nr * 3 + nc
                if gs.can_slide(nidx):
                    new_gs = gs.slide(nidx)
                    new_g = g + 1
                    if new_gs not in visited or new_g < visited[new_gs]:
                        visited[new_gs] = new_g
                        parent_map[new_gs] = (gs, ("slide", nidx))
                        h = heuristic(new_gs)
                        heapq.heappush(open_heap, (new_g + h, next(counter), new_g, new_gs))

    return best_solution, best_cost if best_cost is not None else -1