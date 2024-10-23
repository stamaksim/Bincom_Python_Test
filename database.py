import os
import psycopg2
from typing import List


def save_to_database(colors: List[str]) -> None:
    # Read database connection parameters from environment variables
    dbname = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")

    # Connect to the PostgreSQL database
    try:
        # Using a context manager to automatically handle closing the connection
        with psycopg2.connect(
            dbname=dbname, user=user, password=password, host=host, port=port
        ) as conn:
            # Creating a cursor object using a context manager
            with conn.cursor() as cursor:
                # Create the table if it does not exist
                cursor.execute(
                    "CREATE TABLE IF NOT EXISTS colors ("
                    "color VARCHAR PRIMARY KEY, count INT"
                    ")"
                )

                # Insert colors into the database, updating the count if the color already exists
                for color in set(colors):
                    cursor.execute(
                        "INSERT INTO colors (color, count) VALUES (%s, %s) "
                        "ON CONFLICT (color)"
                        " DO UPDATE SET count = colors.count + EXCLUDED.count",
                        (color, colors.count(color)),
                    )
            # Commit the transaction
            conn.commit()
    except Exception as e:
        # Print any errors that occur during the process
        print(f"An error occurred: {e}")
