from colors_analysis import analyze_colors
from database import save_to_database
from fibonacci import sum_fibonacci
from random_number import generate_random_number


def main():
    colors = analyze_colors("python_class_question.html")

    if colors:
        save_to_database(colors)
    else:
        print("No colors to save to the database.")

    fibonacci_sum = sum_fibonacci()
    print(f"The sum of the first 50 Fibonacci numbers: {fibonacci_sum}")

    random_number = generate_random_number()
    print(f"Generated random number: {random_number}")


if __name__ == "__main__":
    main()
