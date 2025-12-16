# Project 1 - csv profiler

- Profiles csv using the csv library
- creates a report which has these metrics (Column Name , Type , Missing Values , Top Value , Non-empty Counts , Max , Min , Mean , Median , unique)
- outputs the report as a json or markdown
- has both a CLI(typer) and a Web Gui(gradio)

## Installation

```sh
pip install git+https://github.com/afaskar/CSVProfiler.git
```

## Run CLI

```sh
python -m csv_profiler data/data.csv -o report.json
```

or

```sh
python -m csv_profiler.cli data.csv -o report.json
```

## run Gradio Gui

```sh
python -m csv_profiler.webgui
```
