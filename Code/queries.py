import sqlite3 as sl3
import os

currentPath = os.path.dirname(__file__)
file = "..\\SQL\\SQL.sql"

new_path = os.path.relpath(file, currentPath)

