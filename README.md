# Temple Trap Puzzle Solver & Interactive Visualizer

An elegant, modular Python implementation that solves the **Temple Trap** sliding-block puzzle using the **$A^*$ Search Algorithm** and provides a step-by-step graphical playback simulation built with **Pygame**.

---

## 📄 Project Documentation
The complete formal mathematical formulation, layout constraints, rules, and assignment specifications of the puzzle can be viewed directly in the [Docs Folder](./docs/details%20of%20 temple%20trap.pdf).

---

## 🧩 The Puzzle & Mechanics Overview

The puzzle is modeled as a $3 \times 3$ grid containing 8 unique sliding tile blocks (labeled A through H) and exactly one empty grid space `""`. The objective is to navigate an explorer pawn from its initial starting block safe-haven to the ultimate escape exit located explicitly on the **left boundary of Cell 0**.

### Core Constraints & Features Implemented:
* **Two-Layer Elevation Architecture:** The game state distinguishes seamlessly between a **Ground** floor and a **Top** corridor layer.
* **Stairs & Vertical Traversal:** Elevation transitions occur dynamically only when the pawn passes through specific tile paths containing staircases (Tiles D and E).
* **The Lock Rule:** A tile containing a hole can slide into the empty spot if and only if the pawn is *not* currently occupying that specific tile.
* **Algorithmic Path Optimization:** Individual block slides cost `1`, and each single-cell node pawn walk step costs `1`. The program calculates the minimal cumulative cost path.

---

## 📝 Algorithmic Implementation Details

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
├── docs/                     # Assignment Specifications
│   └── details_of_temple_trap.pdf
│
├── main.py                   # Interactive Project CLI Command Line Entrypoint
└── requirements.txt          # Package framework dependency file
