##Task: Decide how you'll store tables in a Python structure (hint: dict of tables).
# Each table should keep:
# List of column names
# List of rows (each row as a dict or tuple).


database = {}
database = {
    "users" : {
        "column" : ["id", "name"],
        "rows" : [
            {"id": 1, "name": "Naveen"},
            {"id": 2, "name": "Varsha"}
            ]
        }
    }

print(database["users"]["rows"][0]["name"])