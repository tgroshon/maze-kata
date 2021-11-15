import click
from image import digitize_maze_image, output_solution_image
from maze_solver import solve


@click.command()
@click.argument("file")
@click.option(
    "--output",
    default="solution.png",
    help="Override path for solution image: defaults to 'solution.png' in current directory.",
)
def main(**kwarg):
    """Begin solving process."""
    filepath = kwarg.get("file")
    output_path = kwarg.get("output")

    maze = digitize_maze_image(filepath)
    solution = solve(maze)
    # output_solution_image(output_path, maze, solution)

    click.echo("Done.")


if __name__ == "__main__":
    main()
