import sqlite3 as sl3
import timeit


def timeit_wrapper(func):
    def wrapper(*args, **kwargs):
        start = timeit.default_timer()
        result = func(*args, **kwargs)
        end = timeit.default_timer()
        print(f"{func.__name__} took {end - start} seconds")
        return result

    return wrapper


@timeit_wrapper
def createConnection():
    connection = sl3.connect("SQL\database.db")
    cursor = connection.cursor()
    print("Database created and Successfully Connected to SQLite")
    return connection, cursor


@timeit_wrapper
def executeQuery(
    cursor,
    connection,
    query="""
        SELECT name, max(latitude_deg), iso_country
        FROM airports
        WHERE continent = 'EU';
        """,
):
    # execute query
    cursor.execute(query)

    connection.commit()
    record = cursor.fetchall()
    print(f"The result of the {query}\n\tis\n\t", record)
    cursor.close()


@timeit_wrapper
def proccess():
    # create database
    connection, cursor = createConnection()
    print("\n")

    # execute query
    executeQuery(cursor, connection)
    print("\n")

    # close connection
    connection.close()
    print("SQLite connection is closed")


if __name__ == "__main__":
    print("Running without index..")
    print("\n")
    proccess()
    print("\n")
    print("Done!")

    print("Running with index..")
    print("\n")
    proccess()
    print("\n")
    print("Done!")
