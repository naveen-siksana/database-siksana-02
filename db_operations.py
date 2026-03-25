#db = {} # Global in-memory database represented as a dictionary
col = [] # List to hold column names for a table
row = [] # List to hold row data and each row is a dictionary mapping column names to values
table = {} # Dictionary to hold table data

def create_table(db, table_name, columns):
    if table_name in db:
        raise ValueError(f"Table {table_name} already exists.")
    db[table_name] = {
        "columns": columns,
        "rows": []
    }
    return db

def insert(db, table_name, values):
    if table_name not in db:
        raise ValueError(f"Table {table_name} does not exist.")
    table = db[table_name]
    if len(values) != len(table["columns"]):
        raise ValueError("Column count does not match value count.")
    row = dict(zip(table["columns"], values))
    table["rows"].append(row)
    return db

def select(db, table_name, columns=None, where=None):
    if table_name not in db:
        raise ValueError(f"Table {table_name} does not exist.")
    table = db[table_name]
    if columns == None or columns == "*":
        columns = table["columns"]
        result = []
        for row in table["rows"]:
            if where is None or row[where["column"]] == where["value"]:
                result.append({col: row[col] for col in columns})
        return result
    else:
        result = []
        for row in table["rows"]:
            if where is None or row[where["column"]] == where["value"]:
                result.append({col: row[col] for col in columns})
        return result









