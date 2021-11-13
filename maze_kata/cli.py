import click
from maze_kata import solve


@click.command()
@click.argument("file")
def main(**kwarg):
    """Begin solving process."""
    filepath = kwarg.get("file")
    solve(filepath)
    click.echo("Done.")


if __name__ == "__main__":
    main()
