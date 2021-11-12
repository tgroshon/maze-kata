# maze-kata

Quickstart:

1. Install MagickWand library: `apt install libmagickwand-dev`
2. Install python requirements: `pip install -r pip-requirements.txt`
3. Run: `python3 solver_practice.py`

Problems to solve:

1. What spaces are empty?
  - white spaces, black spaces
2. What spaces are a valid move target?
  - non-diagonal adjacent empty spaces
3. How do I identify a decision (branch) point?
  - multiple (unvisited?) valid move targets
4. How do I choose the next step?
  - keep left, move down, prioritize unvisited nodes
5. How do I identify a deadend?
  - no valid moves other than your previous location
6. When reacing a deadend, what do I do?
  - move to the prior decision point
  - suggests a stack of branch points
    - 'put' when reaching a new decision point
    - 'peek' when backtracking
    - 'pop' when all decision paths exhausted
