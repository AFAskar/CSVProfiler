import csv
import json
from pathlib import Path
from collections import Counter


# list to avoid empty values
def infer_type(values: list[str]) -> str:
    try:
        for v in values:
            if v is None or v.strip() == "":
                continue
            float(v)
        return "Number"
    except ValueError:
        return "String"


# Return Column Names and Data as a List of Dictionaries
def read_csv(file:Path) -> dict:
    output = {"column_names": [], "data": []}
    with open(file, "r", newline="", encoding="utf-8") as f:
        # get Colun Names from CSV Header
        reader = csv.DictReader(f)
        output["column_names"] = reader.fieldnames
        output["data"] = [row for row in reader]
    output["source"]=file.name
    return output


#   Compute row count, and missing values per column. also top value per column
def profiler(data: dict) -> dict:

    profiled_data = {
        "source":data["source"],
        "summary":{
            "Row Count": 0,
            "Columns":0
        },
        "columns": {},
    }
    # Construct Columns schema and get data type of columns
    for col in data["column_names"]:
        col_values_raw = [row.get(col) for row in data["data"]]
        col_values = [
            val for val in col_values_raw if val is not None and val.strip() != ""
        ]
        # For numeric columns, convert to float
        type_of_col = infer_type(col_values)
        if type_of_col == "Number":
            col_values = [float(val) for val in col_values]
        top_values = Counter(col_values).most_common(1)
        unique_values = set(col_values)
        profiled_data["columns"][col] = {
            "type": type_of_col,
            "missing_values": 0,
            "unique":len(unique_values),
            "top_value": dict(top_values),
        }
        # calculate max and min, mean and median
        if type_of_col == "Number" and col_values:
            profiled_data["columns"][col]["max"] = max(col_values)
            profiled_data["columns"][col]["min"] = min(col_values)
            profiled_data["columns"][col]["mean"] = round(sum(col_values) / len(col_values), 2)
            profiled_data["columns"][col]["median"] = round(
                sorted(col_values)[len(col_values) // 2], 2
            )

    # Compute missing values

    for row in data["data"]:
        for col in data["column_names"]:
            value = row.get(col)
            if value is None or value.strip() == "":
                profiled_data["columns"][col]["missing_values"] += 1

    profiled_data["summary"]["Row Count"] = len(data["data"])
    profiled_data["summary"]["Columns"]=len(profiled_data["columns"])

    return profiled_data



def createJsonReport(data: dict):
    text = json.dumps(data, indent=4)
    return text