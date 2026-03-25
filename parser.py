import re


def normalize_value(raw_value):
    raw_value = raw_value.strip()

    if raw_value.startswith("'") and raw_value.endswith("'"):
        return raw_value[1:-1]


    if raw_value.isdigit():
        return int(raw_value)

    return raw_value


def parse_create(query):
    pattern = r"^\s*CREATE\s+TABLE\s+(\w+)\s*\(([^)]+)\)\s*;?\s*$"
    match = re.match(pattern, query, re.IGNORECASE)

    if not match:
        raise ValueError("Invalid CREATE TABLE syntax")

    table_name = match.group(1)
    columns_raw = match.group(2)
    columns = [col.strip() for col in columns_raw.split(",")]

    return {
        "type": "create",
        "table": table_name,
        "columns": columns
    }


def parse_insert(query):
    pattern = r"^\s*INSERT\s+INTO\s+(\w+)\s+VALUES\s*\(([^)]+)\)\s*;?\s*$"
    match = re.match(pattern, query, re.IGNORECASE)

    if not match:
        raise ValueError("Invalid INSERT syntax")

    table_name = match.group(1)
    values_raw = match.group(2)
    values = [normalize_value(val) for val in values_raw.split(",")]

    return {
        "type": "insert",
        "table": table_name,
        "values": values
    }


def parse_select(query):
    pattern = r"^\s*SELECT\s+(.+?)\s+FROM\s+(\w+)(?:\s+WHERE\s+(\w+)\s*=\s*('[^']*'|\d+|\w+))?\s*;?\s*$"
    match = re.match(pattern, query, re.IGNORECASE)

    if not match:
        raise ValueError("Invalid SELECT syntax")

    columns_raw = match.group(1).strip()
    table_name = match.group(2)
    where_column = match.group(3)
    where_value = match.group(4)
    print("Where value:", where_value)

    if columns_raw == "*":
        columns = "*"
    else:
        columns = [col.strip() for col in columns_raw.split(",")]

    where = None
    if where_column and where_value is not None:
        where = {
            "column": where_column,
            "value": normalize_value(where_value)
        }

    return {
        "type": "select",
        "table": table_name,
        "columns": columns,
        "where": where
    }


def parse_sql(query):
    stripped = query.strip().lower()

    if stripped.startswith("create table"):
        return parse_create(query)

    if stripped.startswith("insert into"):
        return parse_insert(query)

    if stripped.startswith("select"):
        return parse_select(query)

    raise ValueError("Unsupported SQL command")
