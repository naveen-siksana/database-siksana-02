import re
from db_operations import create_table, insert, select
from parser import parse_sql
import json, os

DB_FILE = "database.json"

def load_database():
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, "w") as f:
            db = json.dump({}, f)
    with open(DB_FILE, "r") as f:
        db = json.load(f)
    return db

def save_database(db):
    with open(DB_FILE, "w") as f:
        json.dump(db, f, indent=4)