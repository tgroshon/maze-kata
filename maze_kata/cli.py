import click
from digitizer import digitize_maze_image, output_solution_image
from solver import solve


@click.command()
@click.argument("file")
@click.option(
    "--output",
    default="solution.png",
    help="Override path for solution image: defaults to 'solution.png' in current directory.",
)
def main(**kwarg):
    """Begin solving process."""
    img_filepath = kwarg.get("file")
    output_path = kwarg.get("output")

    maze = digitize_maze_image(img_filepath)
    click.echo(f"Parsed a {maze.shape.rows}x{maze.shape.columns} maze.")
    solution = solve(maze)

    if solution:
        click.echo(f"Solution found! Outputting solved maze to {output_path}")
        output_solution_image(img_filepath, output_path, maze, solution)
        click.echo("Done.")
    else:
        click.echo("No solution found.")


if __name__ == "__main__":
    main()
