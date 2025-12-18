# Project 1 - csv profiler

- Profiles csv using the csv library
- creates a report which has these metrics (Column Name , Type , Missing Values , Top Value , Non-empty Counts , Max , Min , Mean , Median , unique)
- outputs the report as a json or markdown
  - CLI infers output type through extension suffix
- has both a CLI(typer) and a Web Gui(gradio)

## Installation

```sh
pip install git+https://github.com/afaskar/CSVProfiler.git
```

## Run CLI

![CLI Animation](docs/cli-demo.gif)

```sh
csv-profiler cli data/data.csv -o outputs -f json
```

or

```sh
python -m csv_profiler cli data/data.csv -o outputs -f json
```

or

```sh
python -m csv_profiler.cli cli data.csv -o outputs -f json
```

## run Gradio Gui

```sh
csv-profiler web
```

or

```sh
python -m csv_profiler web

```

or

```sh
python -m csv_profiler.webgui
```
