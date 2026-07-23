from database_connection import get_connection, close_connection


def test_database():

    connection = get_connection()

    if connection is None:
        print("Database Connection Failed")
        return

    print("===================================")
    print("Connected to MySQL Successfully")
    print("Database : healthcare_db")
    print("===================================")

    cursor = connection.cursor()

    cursor.execute("SELECT DATABASE();")

    db = cursor.fetchone()

    print("Current Database :", db[0])

    cursor.execute("SELECT VERSION();")

    version = cursor.fetchone()

    print("MySQL Version :", version[0])

    cursor.close()

    close_connection(connection)


if __name__ == "__main__":
    test_database()