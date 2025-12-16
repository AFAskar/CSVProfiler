from .profiler import read_csv, profiler, createJsonReport
from .mdwriter import createMD
from pathlib import Path
import typer
import click
from rich import print

app = typer.Typer()


@app.command()
def cli(
    input: Path = typer.Argument(..., exists=True, file_okay=True, dir_okay=False),
    output: Path | None = typer.Option(
        None,
        "-o",
        "--output",
        help="Output report file path. If not provided, defaults to 'Report.md'",
    ),
):
    if input.suffix.lower() != ".csv":
        raise click.ClickException("Input file must be a CSV file.")
    csvfile = read_csv(input)
    data = profiler(csvfile)
    if output is None:
        output_path = Path("Report.md")
        print(f"No output path provided. Using default: {output_path}")
    else:
        output_path = output
    output_ext = Path(output_path).suffix.lower()
    if output_ext == ".md":
        text = createMD(data)
        output_path.write_text(text)
    elif output_ext == ".json":
        text = createJsonReport(data)
        output_path.write_text(text)
    else:
        raise click.ClickException(
            "Unsupported output file format. Please use .md or .json"
        )

    return


if __name__ == "__main__":
    app()
