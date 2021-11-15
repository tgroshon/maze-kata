import click
from image_parser import parse
from maze_kata import solve


@click.command()
@click.argument("file")
def main(**kwarg):
    """Begin solving process."""
    filepath = kwarg.get("file")
    mk_image = parse(filepath)
    solve(mk_image)
    click.echo("Done.")


if __name__ == "__main__":
    main()
