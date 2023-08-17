# maze-kata

![CI Checks](https://github.com/tgroshon/maze-kata/actions/workflows/python-ci.yml/badge.svg)

Quickstart:

1. Install python requirements: `pip install -r pip-requirements.dev.txt`
2. Run CLI: `python3 cli.py <file>`
3. Run tests: `pytest`

```
$ python3 cli.py --help
Usage: cli.py [OPTIONS] FILE

  Analyze an image of a maze grid and output a solution image.

Options:
  --output TEXT  Override path of solution: defaults 'solution.png'
  --help         Show this message and exit.

```

## Kata and Goals

You are going to be building a maze solver for simple mazes such as the
following. Don’t get started yet -- make sure to read the background and the
user stories first.

Don’t worry about building the perfect solution. (Gold-plating is not a plus.)

Instead, your solution prioritize the following items, in this order:

- Demonstrated approach to testing and validation best practices (unit,
integration, end-to-end, etc)
- Software craftsmanship including, but not limited to, clean code practices,
SOLID principles, KISS, refactoring, and maintainability
- Solving each user story incrementally instead of attempting to solve the whole
problem in one go (preference is 1+ commit per user story)
- Demonstration of problem solving approach, for example, through commit
  comments
- Algorithmic approach

### User Stories

#### User Story 1

Find the “empty” space in a single-row input such as the following:

![single row](./assets/us1_single_row.png)

#### User Story 2

Walk through a “hallway” maze such as:

![hallway](./assets/us2_hallway.png)

#### User Story 3

Find a way into and out of rooms such as:

![simple room](./assets/us3_room.png)

#### User Story 4

Follow winding paths:

![winding path](./assets/us4_winding.png)

#### User Story 5

Bypass deadends:

![deadends](./assets/us5_simple.png)

#### User Story 6

Put it all together and solve a large complex maze:

![complex maze](./assets/us6_complex.png)

## Reflection/Analysis

At it's core, my approach is a depth-first search of a graph constructed of
adjacent spaces, with heuristics prioritizing downward motion. This means that
the time complexity _of the traversal_ grows with the complexity of the maze:
O(Vertices + Edges) in graph speak while the space complexity is O(Vertices).
However, the process of building the Maze's intermediate representation is
O(rows*columns) in both time and space. Then, adding in my enhancement of
dead-end filling, it's the same complexity as the primary DFS traversal.

This solution is a general-purpose solver for mazes of the supplied format, with
ability to solve both perfect and imperfect mazes.

My solver does expect to (a) start from outside rather than inside and (b) know
the whole maze upfront (specifically for the dead-end filling enhancement).

Additionally, my tool reads and writes _actual PNG image files_, of the format
given in the user stories: fixed-sized grids of 88x64 pixel rectangles.

While the core of the algorithm, the DFS traversal, can be re-purposed to work
for starting inside of an unknown maze and finding an exit, the rest of the
program (especially the digitizer and maze utilities) would need rewritten.

See more discussion about the assumptions and constraints of my solution in the
narrative walkthrough.

See my solution outputs:

**User Story 1**: Single Row, find space

![user story 1 solution](./assets/solutions/us1_single_solution.png)

**User Story 2**: Walk down a hallway

![user story 2 solution](./assets/solutions/us2_hallway_solution.png)

**User Story 3**: Escape a room

![user story 3 solution](./assets/solutions/us3_room_solution.png)

**User Story 4**: follow a winding path

![user story 4 solution](./assets/solutions/us4_winding_solution.png)

**User Story 5**: Beware dead-ends

![user story 5 solution](./assets/solutions/us5_simple_solution.png)

**Final**: Solve a complex maze with many dead-ends

![user story 6 solution](./assets/solutions/us6_complex_solution.png)

## Testing Stats

Latest coverage report for command: `pytest --cov=maze_kata.lib --cov-branch --cov-report term-missing`

```
----------- coverage: platform linux, python 3.9.5-final-0 -----------
Name                         Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------------------
maze_kata/lib/__init__.py        0      0      0      0   100%
maze_kata/lib/digitizer.py      36      7      4      0    78%   14-16, 21-26
maze_kata/lib/maze.py           64      0     16      0   100%
maze_kata/lib/solver.py         35      0     24      2    97%   37->51, 40->43
------------------------------------------------------------------------
TOTAL                          135      7     44      2    94%
```

Complex maze benchmark:

```
$ python3 benchmark.py
Solver with DefaultStrategy benchmark 100x:  0.0322987970002941
Full pipeline Load->Solve->Output 100x:      1.4854517479998322

$ time python3 cli.py assets/us6_complex.png
Parsed a 10x10 maze.
Solution found! Outputting solved maze to solution.png
Done.

real    0m0.123s
user    0m0.291s
sys     0m0.563s
```

## Appendix: Approach Walkthrough

When I first read the kata, I decided to make a list of questions I needed to
answer:

1. Which cells are spaces?
    - white cells are spaces; black cells are walls
2. What spaces are a valid move target?
    - non-diagonal adjacent spaces
3. How do I identify a decision (branch) point?
    - 2 unvisited move targets
4. How can I choose the next step?
    - random?
    - wall following (put your right hand on the wall and follow it)
5. How do I identify a deadend?
    - only 1 adjacent space
6. When reaching a deadend, what do I do?
    - move to the prior decision point
    - could suggest a stack of branch points
        - 'put' when reaching a new decision point
        - 'peek' when backtracking
        - 'pop' when all decision paths exhausted
7. How do I parse an image?
    - maze grid cells are uniform sizes, but small pixel variations are possible
    - use OpenCV to sample centerpoints of each grid cell and make matrix of
      "spaces" or "walls"
8. How do I output a solution?
    - a solution is an ordered list of cell addresses
    - overlay markings for each solution address on a copy of the original image

I decided I wanted the solution to be runnable from the beginning, both for
debugging and in case a time constraint occurred I would be able to submit a
working solution for whatever user stories I had accomplished to that point.

For this reason, I decided to start by building the infrastructural code first:
- CLI runner
- OpenCV image reading
- parsing image data into intermediate representation of spaces and walls
- OpenCV to overlay a solution to maze image

And after the infrastructural shell was in place, I focused on the actual maze
solving logic. In this way, I could use unit tests to verify discrete pieces but
also verify end-to-end behavior with automated tests or by running the CLI tool.
Once the shell of the program was in-place, I implemented the first User Story
with no difficulty as the verification. Then, I moved on to the "logic" portion.

I have never written a "maze-solving algorithm" before, and I chose to avoid too
much algorithm research until I had a chance to try a solution myself. This way,
I would develop some intuition on the problem space: potential pitfalls,
language-specific considerations, etc. After messing with a "wall following"
algorithm by hand, I realized that the code I wrote reminded me of a Graph
search and things clicked into place from there: my intermediate representation
was almost an adjacency list (but not really) and the code was doing node
traversal. I rewrote the code to be an explicit "Depth-first search" (DFS) for
the end node and started solving the additional user stories! Winding paths,
dead-ends, rooms, all worked (sort-of; coming back to that :wink:).

I chose DFS over "breadth-first search" because DFS is better if the solution is
known to be far away (many nodes deep), and I knew upfront as a simple heuristic
that all the mazes in the sample had start and end points at opposite ends of
the graph.

After a few dozen runs and refactors, I pushed that depth heuristic further:
because the start was always the top, and the finish was always the bottom, by
prioritizing downward movement when choosing neighbors to visit, the algorithm
consistently found shorter paths, faster.

So, at this point a naive DFS "worked", but it didn't _really work_. Because I
was lazy and naively returning my "visited" data structure as my "solution", it
included my failed paths as well as the correct path. So, after backtracking
from a dead-end, I wasn't dropping the bad path of visited nodes from my
solution. This meant that if the maze was laid out just right, the neighbor
visiting heuristics would fail and the solver would visit every (or close to
every) space in the maze. FAIL!

Before addressing, I decided to spend time researching formal "maze-solving
algorithms". This helped me (a) codify more of my assumptions, (b) identify
gaps, and (c) try out other approaches.

My current solution makes a lot of assumptions, and has some clear constraints.
Here are some of them:

- Entire maze is known upfront
- One entrance at the top, one exit at the bottom
- Maze images are standardized to grids of fixed-size cells about 88x64 pixels
- Mazes must be smaller than 32 x 44 because of naive digitizer which accumulates sizing errors as the maze grows
- Only finds one solution path if multiple are available
- Does not guarantee the shortest path
- Time complexity grows with the complexity of the maze: O(Vertices + Edges) in graph speak
- And of course ... the reports-every-failed-path "problem" :smirk:

Now, because the entire maze is known, that provides several opportunities for
alternative strategies. One such strategy I chose to implement from my research
was dead-end filling.
1. Identify all dead-ends
2. Fill the dead-end path backwards to the next junction
3. Repeat

This enhancement paired well with the DFS graph search because ... it eliminated
all bad paths, leaving only correct paths :D

JACKPOT!

I could keep my lazy, naive DFS solution if I first filled in the dead-ends,
leaving only one path for a perfect maze with no loops, or several correct paths
if loops existed. And no matter which way the algorithm chose, it wouldn't
backtrack. One, nice, straight line.

The cost ... not much ... just traverse the graph a few ADDITIONAL TIMES to find
and then fill in the dead-spaces. NBD. /sarcasm

But, the time-complexity should still be about the same. From near as I can
tell, my dead-end filling algorithm is essentially just another graph traversal
with O(V+E) but I'll have to think on it.
