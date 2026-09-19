import csv
import os
def save_expense(expense):
    file_exists = os.path.exists("expenses.csv")

    with open("expenses.csv", "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(
                ["Date", "Category", "Description", "Amount"]
            )

        writer.writerow(expense)
def load_expenses():

    expenses = []

    try:
        with open("expenses.csv", "r") as file:

            reader = csv.DictReader(file)

            for row in reader:
                expenses.append(row)

    except FileNotFoundError:
        print("Expense file not found. Starting with empty records.")

    return expenses        