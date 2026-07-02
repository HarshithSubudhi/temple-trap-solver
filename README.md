# Temple Trap Puzzle Solver & Interactive Visualizer

An elegant, modular Python implementation that solves the **Temple Trap** sliding-block puzzle using the **$A^*$ Search Algorithm** and provides a step-by-step graphical playback simulation built with **Pygame**.

---

## Project Documentation
* **Challenge Rules & Formulation:** The detailed puzzle rules, mathematics, and layout specifications can be viewed in the [Professor's Assignment Document](https://github.com/HarshithSubudhi/temple-trap-solver/blob/main/docs/details%20of%20temple%20trap.pdf).
* **Full Puzzle Booklet (1-60):** The complete challenge booklet containing all 60 levels can be viewed in the [Challenge Booklet PDF](https://github.com/HarshithSubudhi/temple-trap-solver/blob/main/docs/temple_trap_booklet.pdf).

---

## The Puzzle & Mechanics Overview

The puzzle is modeled as a $3 \times 3$ grid containing 8 unique sliding tile blocks (labeled A through H) and exactly one empty grid space `""`. The objective is to navigate an explorer pawn from its initial starting block safe-haven to the ultimate escape exit located explicitly on the **left boundary of Cell 0**.

### Core Constraints & Features Implemented:
* **Two-Layer Elevation Architecture:** The game state distinguishes seamlessly between a **Ground** floor and a **Top** corridor layer.
* **Stairs & Vertical Traversal:** Elevation transitions occur dynamically only when the pawn passes through specific tile paths containing staircases (Tiles D and E).
* **The Lock Rule:** A tile containing a hole can slide into the empty spot if and only if the pawn is *not* currently occupying that specific tile.
* **Algorithmic Path Optimization:** Individual block slides cost `1`, and each single-cell node pawn walk step costs `1`. The program calculates the minimal cumulative cost path.

---

## Algorithmic Implementation Details

### 1. State Space Representation
The game configuration is tracked dynamically using a dedicated state machine layout:
* **Board Matrix:** Represented as a flat list of 9 elements mapping the $3 \times 3$ grid in row-major order (`0` to `8`).
* **Rotational Constraints:** An array tracking orientation offsets (`0`, `1`, `2`, `3`) corresponding to a clockwise transformation from its base identification mark.
* **Pawn State Space:** Tracks both the tile index position (`0` to `8`) and an elevation layer string status (`Ground` or `Top`).

### 2. Action Space & Connectivity
* **Slide Actions (Cost = 1):** Moves a non-pawn occupied tile orthogonally into the empty grid spot `""`.
* **Walk Actions (Cost = 1 per step):** Explores all valid pathway links across matching open tile sides using a Breadth-First Search (BFS) grid computation.
* **Vertical Layer Escalation:** Modifies layer state bounds securely when moving into corridor stair spaces (Tiles D and E).

### 3. Heuristic Function
To optimize node selection and accelerate path discovery within the $A^*$ search queue, the solver uses **Manhattan Distance** tracking:

$$h(n) = |r_{\text{pawn}} - 0| + |c_{\text{pawn}} - 0|$$

This computes the absolute geometric steps required for the pawn to transition from its current grid coordinate $(r, c)$ straight to the target escape exit cell at index `0`. By combining this heuristic estimate with the true accumulated step cost $g(n)$, the solver evaluates the ideal path profile using $f(n) = g(n) + h(n)$.

---

## Features & Verification

* **Full 60-Level Challenge Coverage:** Solves and verifies every level in the booklet (Starter 1-12, Junior 13-24, Expert 25-36, Master 37-48, Wizard 49-60) matching their optimal move counts exactly.
* **Dual-Engine Search Pipeline:** Accelerates solve times with a high-performance, slot-optimized A* Search algorithm, falling back seamlessly to Breadth-First Search (BFS) for extremely deep state spaces (up to 189 moves in Level 60).
* **Cross-Platform CLI Compatibility:** Normalized console output streams to guarantee clean, robust execution outputs across all platform terminals.

---

## 📁 Repository Structure

```text
temple-trap-solver/
│
├── temple_trap/              # Main Core Package Modules
│   ├── assets/               # Tight-cropped custom tile images (A-H)
│   ├── __init__.py           # Package namespace initialization
│   ├── config.py             # Map definitions, tiles layouts, & configurations
│   ├── engine.py             # Physical game rules & connectivity mechanics
│   ├── solver.py             # Heuristic functions & A* state space tracking
│   └── visualizer.py         # Pygame window canvas rendering pipeline
│
├── docs/                     # Assignment Specifications & Challenge Booklet
│   ├── details of temple trap.pdf
│   └── temple_trap_booklet.pdf
│
├── main.py                   # Interactive Project CLI Command Line Entrypoint
└── requirements.txt          # Package framework dependency file
```
