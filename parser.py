# =====================
# Database (from Phase 1)
# =====================
# Input: table name + list of column names.
# Output: new empty table stored in your database dict.
# Check: error if table already exists.


database = {}
# columns1 = []

def create_table(database,tableName,col=[]):
    r = []
    database[tableName] = {
        "columns": col,
        "rows": r
    }
    #print(database[tableName])

def insert(database,tableName,r):
    database[tableName]["rows"] = r
    #print(database[tableName])

def print_table(database,tableName):
    table = database[tableName]
    cols = table["columns"]
    rows = table["rows"]
    print("\t".join(cols))
    for row in rows:
        print("\t".join(str(row.get(col,"")) for col in cols))

def select(database, tableName,where,value):
    for row in database[tableName]["rows"]:
        if row.get(where) == value:
            #table = database[tableName][row]
            #print_table(database,table)
            print(row)

create_table(database,"users",["id","name"])
create_table(database,"students",["id","course"])
insert(database,"users",[{"id":1,"name":"Naveen"}])
insert(database,"students",[{"id":1,"course":"CS"}])
#print_table(database,"users")
select(database,"students","id",1)


# =====================
# SQL Parsing
# =====================
def parse_create(query):
    """
    Example:
    CREATE TABLE users (id, name);
    Return -> {"type": "create", "table": "users", "columns": ["id", "name"]}
    """
    # TODO: Extract table name + columns
    return {"type": "create", "table": None, "columns": []}


def parse_insert(query):
    """
    Example:
    INSERT INTO users VALUES (1, 'Alice');
    Return -> {"type": "insert", "table": "users", "values": [1, "Alice"]}
    """
    # TODO: Extract table name + values
    return {"type": "insert", "table": None, "values": []}


def parse_select(query):
    """
    Example:
    SELECT name FROM users WHERE id=2;
    Return -> {
      "type": "select",
      "table": "users",
      "columns": ["name"],
      "where": {"id": 2}
    }
    """
    # TODO: Extract columns, table, and WHERE clause (if any)
    return {"type": "select", "table": None, "columns": [], "where": None}


def parse_sql(query):
    """
    Dispatch parser based on SQL keyword.
    """
    q = query.strip().lower()
    if q.startswith("create table"):
        return parse_create(query)
    elif q.startswith("insert into"):
        return parse_insert(query)
    elif q.startswith("select"):
        return parse_select(query)
    else:
        raise ValueError("Unsupported SQL command")


# =====================
# Execution Engine
# =====================
def execute(query, db):
    parsed = parse_sql(query)

    if parsed["type"] == "create":
        return create_table(db, parsed["table"], parsed["columns"])

    elif parsed["type"] == "insert":
        return insert_into(db, parsed["table"], parsed["values"])

    elif parsed["type"] == "select":
        return select_from(db, parsed["table"], parsed["columns"], parsed["where"])

    else:
        raise ValueError("Unknown query type")


# =====================
# Example Run (once implemented)
# =====================
if __name__ == "__main__":
    execute("CREATE TABLE users (id, name);", database)
    execute("INSERT INTO users VALUES (1, 'Alice');", database)
    execute("INSERT INTO users VALUES (2, 'Bob');", database)
    result = execute("SELECT name FROM users WHERE id=2;", database)
    print(result)  # Expected: [{'name': 'Bob'}]