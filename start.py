import click
import app

@click.command()
@click.argument("namefile")
@click.option("--output", "-o", default=None, help="Output directory of the permutated usernames")
@click.option("--quiet", "-q", default=False, help="Weither or not to include errors in the stdout", is_flag=True)
def start(namefile, output, quiet):
    permutator = app.Permutator(nameFile=namefile,
                                outFile=output,
                                quiet=quiet)
    permutator.start()


if __name__ == "__main__":
    start()