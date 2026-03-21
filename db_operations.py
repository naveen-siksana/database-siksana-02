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
