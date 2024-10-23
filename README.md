"# Bincom_Python_Test" 

# Color Analysis and Database Integration Project

This project consists of several tasks aimed at analyzing colors from images and saving the results to a PostgreSQL database. It utilizes Python and libraries such as `psycopg2` for database interaction and `collections` for counting colors.

## Tasks

### 1. Color Analysis
The function `analyze_colors(file_path)`:
- Extracts colors from the specified file using the `extract_colors` function.
- Counts the occurrences of each color.
- Calculates the mean, median, and variance of color frequencies.
- Determines the probability of selecting the color red.
- Outputs the analysis results to the console.

### 2. Saving Colors to the Database
The function `save_colors_to_db(color_counts)`:
- Saves colors and their counts in the `colors` table of the PostgreSQL database.
- Uses an SQL query to insert data, updating the count in case of a conflict.

## Requirements

- Python 3.6 or higher
- Libraries:
  - `psycopg2`
  - `statistics`
  - `collections`

## Installation

1. Clone this repository:
   ```bash
   git clone <REPOSITORY_URL>
   cd color_analysis_project
