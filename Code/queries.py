import sqlite3 as sl3
import pandas as pd

# create database
connection = sl3.connect("SQL\database.db")
cursor = connection.cursor()
print("Database created and Successfully Connected to SQLite")

# paths of the files
sqlFilePath = "SQL\SQL.sql"
csvFilePath = "SQL\\airports.csv"

# execute query
with open(sqlFilePath, "r") as f:
    sqlFile = f.read()
cursor.executescript(sqlFile)

# read csv file
mainColumns = [
    "id",
    "ident",
    "type",
    "name",
    "latitude_deg",
    "longitude_deg",
    "elevation_ft",
    "continent",
    "iso_country",
]
airports = pd.read_csv(csvFilePath, encoding_errors="ignore", usecols=mainColumns)

# insert data into table
# airports.to_sql("airports", connection, if_exists="append", index=False)
for _, row in airports.iterrows():
    cursor.execute("INSERT INTO airports VALUES (?,?,?,?,?,?,?,?,?);", row)

connection.commit()
record = cursor.fetchall()
print("SQLite Database Version is: ", record)
cursor.close()

connection.close()
print("SQLite connection is closed")
