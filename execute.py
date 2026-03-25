import re
from db_operations import create_table, insert, select
from parser import parse_sql
from persist import load_database, save_database


def execute(query, database):
    parsed = parse_sql(query)
    database = load_database()

    if parsed["type"] == "create":
        result = create_table(database, parsed["table"], parsed["columns"])
        save_database(database)
        return result

    if parsed["type"] == "insert":
        result = insert(database, parsed["table"], parsed["values"])
        save_database(database)
        return result

    if parsed["type"] == "select":
        # pass columns and where dict (select signature: db, table_name, columns=None, where=None)
        return select(database, parsed["table"], parsed["columns"], parsed["where"])

    raise ValueError("Unknown query type")


if __name__ == "__main__":
    database = {}

    execute("CREATE TABLE users (id, name);", database)
    execute("INSERT INTO users VALUES (1, 'Alice');", database)
    execute("INSERT INTO users VALUES (2, 'Bob');", database)

    print(execute("SELECT * FROM users;", database))
    print(execute("SELECT name FROM users;", database))
    print(execute("SELECT name FROM users WHERE id=2;", database))
    print(execute("SELECT name FROM users WHERE id=1;", database))