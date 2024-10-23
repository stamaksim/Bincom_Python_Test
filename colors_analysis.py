import os
import statistics
from collections import Counter
from color_extraction import extract_colors
import psycopg2  # Importing psycopg2 for PostgreSQL database connection
from typing import Tuple


def analyze_colors(file_path: str) -> None:
    # Extract colors from the given file path
    colors = extract_colors(file_path)

    # Count the occurrences of each color
    color_counts: Counter = Counter(colors)

    # 1. Calculate the mean color frequency
    mean_color = sum(color_counts.values()) / len(color_counts)
    mean_color = round(mean_color, 2)  # Round to 2 decimal places

    # 2. Find the most common color
    most_common_color: Tuple[str, int] = color_counts.most_common(1)[0]

    # 3. Calculate the median color frequency
    median_color = statistics.median(color_counts.values())
    median_color = round(median_color, 2)  # Round to 2 decimal places

    print(f'Mean color frequency: {mean_color}')
    print(f'Most common color: {most_common_color}')
    print(f'Median color frequency: {median_color}')

    # Bonuses
    # 4. Calculate variance of color frequencies
    variance = statistics.variance(color_counts.values())
    variance = round(variance, 2)  # Round to 2 decimal places
    print(f'Color variance: {variance}')

    # 5. Calculate probability of choosing red color
    probability_red = color_counts['red'] / sum(color_counts.values())
    probability_red = round(probability_red, 4)  # Round to 4 decimal places
    print(f'Probability of selecting red color: {probability_red}')

    # 6. Save colors to the database
    save_colors_to_db(color_counts)


def save_colors_to_db(color_counts: Counter) -> None:
    # Read database connection parameters from environment variables
    dbname = os.getenv('DB_NAME')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')

    # Connect to the PostgreSQL database
    try:
        # Using a context manager to automatically handle closing the connection
        with psycopg2.connect(
            dbname=dbname, user=user, password=password, host=host, port=port
        ) as conn:
            with conn.cursor() as cur:
                # Insert colors into the database
                for color, count in color_counts.items():
                    cur.execute(
                        'INSERT INTO colors (color, count) VALUES (%s, %s) '
                        'ON CONFLICT (color)'
                        ' DO UPDATE SET count = colors.count + EXCLUDED.count',
                        (color, count),
                    )
            # Commit the transaction
            conn.commit()
    except Exception as e:
        # Print any errors that occur during the process
        print(f'An error occurred while saving to the database: {e}')
