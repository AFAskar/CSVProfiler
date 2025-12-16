from .profiler import read_csv, profiler
from .render import createMD, createJsonReport
from pathlib import Path
import gradio as gr


def gui():
    gr.Interface(
        fn=gui_logic,
        inputs=[
            gr.File(label="Upload CSV File", file_types=[".csv"]),
            gr.Dropdown(
                choices=["markdown", "json"],
                label="Select Output Format",
                value="markdown",
            ),
        ],
        outputs=gr.Code(label="Generated Report", language="json"),
        title="CSV Profiler",
        description="Upload a CSV file to generate a profiling report in Markdown or JSON format.",
    ).launch()


def gui_logic(input_file: str, output_format: str) -> str:
    Path_input_file = Path(input_file)
    csvfile = read_csv(Path_input_file)
    data = profiler(csvfile)
    if input_file is None:
        return "Please upload a CSV file."
    if output_format == "markdown":
        return gr.update(value=createMD(data), language="markdown")
    if output_format == "json":
        return gr.update(value=createJsonReport(data), language="json")
    else:
        return gr.update(
            value="Unsupported output format. Please choose 'markdown' or 'json'.",
            language="text",
        )


if __name__ == "__main__":
    gui()
