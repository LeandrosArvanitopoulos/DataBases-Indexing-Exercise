import sqlite3 as sl3
import timeit

times = []


# This wrapper is used to calculate the time taken by a function to execute
def timeit_wrapper(func):
    def wrapper(*args, **kwargs):
        start = timeit.default_timer()
        result = func(*args, **kwargs)
        end = timeit.default_timer()
        if func.__name__ == "executeQuery":
            print("-" * len(f"{func.__name__} took {end - start} seconds"))
            print(f"{func.__name__} took {end - start} seconds")
            print("-" * len(f"{func.__name__} took {end - start} seconds"))
            times.append(end - start)
        else:
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
    if record != [] and record != None:
        print(f"The result of the {query}\n\tis\n\t", record)
    else:
        print(f"For the query {query}")


@timeit_wrapper
def executeQueryWithIndex(
    cursor,
    connection,
    query="""
        SELECT name, max(latitude_deg), iso_country
        FROM airports WITH((idx_airports_lat_deg))
        WHERE continent = 'EU';
        """,
):
    # execute query
    cursor.execute(query)

    connection.commit()
    record = cursor.fetchall()
    if record != [] and record != None:
        print(f"The result of the {query}\n\tis\n\t", record)
    else:
        print(f"For the query {query}")


@timeit_wrapper
def proccess():
    # create database
    connection, cursor = createConnection()
    print("\n")

    # execute query
    executeQuery(cursor, connection)
    print("\n")

    # close connection
    cursor.close()
    connection.close()
    print("SQLite connection is closed")


@timeit_wrapper
def proccessWithIndex():
    # create database
    connection, cursor = createConnection()
    print("\n")

    # execute query
    executeQuery(
        cursor,
        connection,
        query="""CREATE INDEX IF NOT EXISTS idx_airports_lat_deg ON airports(latitude_deg);""",
    )
    executeQuery(cursor, connection)
    executeQuery(cursor, connection, query="""PRAGMA index_list('airports');""")
    print("\n")

    # close connection
    cursor.close()
    connection.close()
    print("SQLite connection is closed")


if __name__ == "__main__":
    print("Running without index..")
    print("\n")
    proccess()
    print("\n")
    print("Done!")
    print("\n")

    print("Running with index..")
    print("\n")
    proccessWithIndex()
    print("\n")
    print("Done!")
    print("\n")

    print(
        "Time taken to execute query without index:"
        + " " * (50 - len("Time taken to execute query without index:")),
        times[0],
    )
    print(
        "Time taken to execute query with index: "
        + " " * (50 - len("Time taken to execute query with index: ")),
        times[1] + times[2],
    )

    print(
        "The acceleration is" + " " * (50 - len("The acceleration is")),
        times[0] / (times[1] + times[2]),
    )
