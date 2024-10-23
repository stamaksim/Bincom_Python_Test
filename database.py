import os
import psycopg2
from typing import List
from dotenv import load_dotenv


load_dotenv()


def save_to_database(colors: List[str]) -> None:
    # Read database connection parameters from environment variables
    dbname = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")

    try:
        with psycopg2.connect(
            dbname=dbname, user=user, password=password, host=host, port=port
        ) as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "CREATE TABLE IF NOT EXISTS colors ("
                    "color VARCHAR PRIMARY KEY, count INT"
                    ")"
                )
                print("Table 'colors' created or already exists.")

                for color in set(colors):
                    cursor.execute(
                        "INSERT INTO colors (color, count) VALUES (%s, %s) "
                        "ON CONFLICT (color) "
                        "DO UPDATE SET count = colors.count + EXCLUDED.count",
                        (color, colors.count(color)),
                    )
                print("Colors inserted or updated successfully.")
            conn.commit()
    except psycopg2.OperationalError as e:
        print(f"Operational error: {e}")
    except Exception as e:
        print(f"An error occurred while saving to the database: {e}")
