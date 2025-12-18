from .profiler import read_csv, profiler
from .render import createMD, createJsonReport
from pathlib import Path
import typer
import click
from rich import print

app = typer.Typer()


@app.command()
def cli(
    input: Path = typer.Argument(..., exists=True, file_okay=True, dir_okay=False),
    output: Path | None = typer.Option(
        Path("outputs"),
        "-o",
        "--out-dir",
        help="Output report directory path. If not provided, defaults to 'outputs'",
    ),
    format: str = typer.Option(
        "both",
        "-f",
        "--format",
        help="Output report format. Supported formats are 'md' 'json', and both. Defaults to 'both'",
    ),
):
    if input.suffix.lower() != ".csv":
        raise click.ClickException("Input file must be a CSV file.")
    csvfile = read_csv(input)
    data = profiler(csvfile)
    output.mkdir(parents=True, exist_ok=True)
    output_ext = format.lower()

    if output_ext == "both":
        md_path = output / "report.md"
        json_path = output / "report.json"
        md_text = createMD(data)
        json_text = createJsonReport(data)
        md_path.write_text(md_text)
        json_path.write_text(json_text)
        print(f"[bold green]Reports generated:[/bold green] {md_path}, {json_path}")
    if output_ext == "md":
        md_path = output / "report.md"
        text = createMD(data)
        md_path.write_text(text)
        print(f"[bold green]Markdown report generated:[/bold green] {md_path}")
    if output_ext == "json":
        json_path = output / "report.json"
        text = createJsonReport(data)
        json_path.write_text(text)
        print(f"[bold green]JSON report generated:[/bold green] {json_path}")

    else:
        raise click.ClickException(
            "Unsupported output file format. Please use 'md', 'json', or 'both'"
        )

    return


if __name__ == "__main__":
    app()
