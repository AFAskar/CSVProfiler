
from datetime import datetime
from pathlib import Path
def md_report_header(source:str) -> list[str]:
    timestamp= datetime.now().isoformat()
    lines = []
    lines.append("# Project Report")
    lines.append("")
    lines.append(f"**Source File**: {source}")
    lines.append("")
    lines.append(f"**Generated on**: {timestamp}")
    lines.append("")
    return lines
def md_report_csv_summary(row_count:int, column_count:int) -> list[str]:
    lines = []
    lines.append("## CSV Summary\n")
    lines.append(f"- Total Rows: {row_count}\n")
    lines.append(f"- Total Columns: {column_count}\n")
    lines.append("\n")
    return lines
def md_table_header() -> list[str]:
    lines = []
    lines.append("| Column Name | Type | Missing Values | Top Value | Non-empty Counts | Max | Min | Mean | Median | unique |")
    lines.append("|-------------|------|----------------|-----------|------------------|----|-----|------|--------|--------|")
    return lines
def md_table_row(col_name: str, col_data: dict, row_count: int) -> str:
    non_empty_counts = row_count - col_data["missing_values"]
    max_val = col_data.get("max", "N/A")
    min_val = col_data.get("min", "N/A")
    top_value_str = ", ".join(f"{k}: {v}" for k, v in col_data["top_value"].items())
    mean_val = col_data.get("mean", "N/A")
    median_val = col_data.get("median", "N/A")
    return f"| {col_name} | {col_data['type']} | {col_data['missing_values']} | {top_value_str} | {non_empty_counts} | {max_val} | {min_val} | {mean_val} | {median_val} | {col_data['unique']} |"
# Create Human Readable Report
def createMD(data: dict):
    lines=[]
    lines.extend(md_report_header(data["source"]))
    lines.extend(md_report_csv_summary(data["summary"]["Row Count"], data["summary"]["Columns"]))
    lines.append("### Columns Overview\n")
    lines.extend(md_table_header())
    for col in data["columns"]:
        col_data = data["columns"][col]
        lines.append(md_table_row(col, col_data, data["summary"]["Row Count"]))
    lines.append("")
    text="\n".join(lines)
    return text