import timeit
import tempfile
import os
from maze_kata.lib import digitizer, core


INPUT_IMG_PATH = os.path.join("assets", "us6_complex.png")


def run_full_pipeline():
    with tempfile.NamedTemporaryFile(suffix="-benchmark-output.png") as fp:
        maze = digitizer.parse_maze_image(INPUT_IMG_PATH)
        solution = core.solve(maze)
        digitizer.output_solution_image(INPUT_IMG_PATH, fp.name, solution)


def get_callable_for_solver():
    maze = digitizer.parse_maze_image(INPUT_IMG_PATH)

    def run_solver():
        core.solve(maze)

    return run_solver


def get_callable_for_improved_strategy_solver():
    maze = digitizer.parse_maze_image(INPUT_IMG_PATH)

    def run_solver():
        core.solve(maze, core.SelfPruningStrategy())

    return run_solver


if __name__ == "__main__":
    print("Running benchmarks...\n")
    print("-" * 47)
    result = timeit.timeit(get_callable_for_solver(), number=100)
    print("| {:<20} | {:<20} |".format("DefaultStrategy", result))
    print("-" * 47)

    result = timeit.timeit(get_callable_for_improved_strategy_solver(), number=100)
    print("| {:<20} | {:<20} |".format("SelfPruningStrategy", result))
    print("-" * 47)

    result = timeit.timeit(run_full_pipeline, number=100)
    print("| {:<20} | {:<20} |".format("Full Pipeline", result))
    print("-" * 47)

    print("\nDone.")
