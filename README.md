# CSV Profiler

Profile a CSV file and generate a simple summary report per column.

## What you get (per column)

- Column name
- Inferred type
- Missing values + non-empty counts
- Top (most frequent) value
- Numeric stats (when applicable): min, max, mean, median
- Unique count

## The project includes:

- A CLI built with Typer
- A Gradio web UI

## Run without installing (uvx)

If you have Astral's `uv` installed, you can run the tool without installing it into your environment.

CLI:

```sh
uvx git+https://github.com/afaskar/CSVProfiler.git cli data/data.csv
```

Web UI:

```sh
uvx git+https://github.com/afaskar/CSVProfiler.git csv-profiler web
```

## Installation

```sh
pip install git+https://github.com/afaskar/CSVProfiler.git
```

For local development:

```sh
pip install -e .
```

## Quickstart (CLI)

![CLI Animation](docs/cli-demo.gif)

```sh
csv-profiler cli data/data.csv
```

This generates the reports in `outputs/` by default:

- `outputs/report.md`
- `outputs/report.json`

### Choose output directory

```sh
csv-profiler cli data/data.csv --out-dir output
```

### Choose output format

Supported values for `--format` are: `md`, `json`, `both`.

```sh
csv-profiler cli data/data.csv --format md
```

```sh
csv-profiler cli data/data.csv --format json
```

```sh
csv-profiler cli data/data.csv --format both
```

### Run via Python module

```sh
python -m csv_profiler cli data/data.csv
```

You can also call the CLI app module directly:

```sh
python -m csv_profiler.cli cli data/data.csv
```

## Web UI (Gradio)

```sh
csv-profiler web
```

Or via module:

```sh
python -m csv_profiler web
```

Or run the web module directly:

```sh
python -m csv_profiler.webgui
```

## Output

- CLI output files are written as `report.md` and/or `report.json` inside the output directory.
- Web UI prints the generated report content directly (Markdown or JSON).

## License

MIT. See [LICENSE](LICENSE).
