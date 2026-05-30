# Temple Trap Puzzle Solver & Interactive Visualizer

An elegant, modular Python implementation that solves the **Temple Trap** sliding-block puzzle using the **$A^*$ Search Algorithm** and provides a step-by-step graphical playback simulation built with **Pygame**.

---

## 🧩 The Puzzle & Mechanics Overview

The puzzle is modeled as a $3 \times 3$ grid containing 8 unique sliding tile blocks (labeled A through H) and exactly one empty grid space `""`. The objective is to navigate an explorer pawn from its initial starting block safe-haven to the ultimate escape exit located explicitly on the **left boundary of Cell 0**.

### Core Constraints & Features Implemented:
* **Two-Layer Elevation Architecture:** The game state distinguishes seamlessly between a **Ground** floor and a **Top** corridor layer.
* **Stairs & Vertical Traversal:** Elevation transitions occur dynamically only when the pawn passes through specific tile paths containing staircases (Tiles D and E).
* **The Lock Rule:** A tile containing a hole can slide into the empty spot if and only if the pawn is *not* currently occupying that specific tile.
* **Algorithmic Path Optimization:** Individual block slides cost `1`, and each single-cell node pawn walk step costs `1`. The program calculates the minimal cumulative cost path.

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
├── tests/                    # Verification Testing Framework
│   └── test_solver.py        # Automated test-suite executing over all presets
│
├── main.py                   # Interactive Project CLI Command Line Entrypoint
├── requirements.txt          # Package framework dependency file
└── README.md                 # Project documentation layout
