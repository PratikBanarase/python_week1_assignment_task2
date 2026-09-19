# Expense Tracker

# Project Overview

The Expense Tracker is a console-based Python application developed as part of the Python Week 1 Assignment.
The application allows users to record, view, and analyze daily expenses. It demonstrates Python file handling, CSV operations, exception handling, user input validation, and basic reporting.

# Objective
The main objective of this project is to build a practical expense management application using Python.
The project focuses on:
- File handling
- CSV data storage
- Reading and writing files
- User input handling
- Exception handling
- Data validation
- Calculating totals
- Generating summary reports

# Features

# 1. Add Expense
Users can add a new expense by entering:
- Date
- Category
- Description
- Amount

# 2. View Expenses
Displays previously recorded expenses in a readable format.

# 3. Calculate Total Expenses
Calculates the total amount spent across all recorded expenses.

# 4. Summary Report
Generates a simple report containing:
- Total number of expenses
- Total amount spent
- Highest expense

# 5. Persistent File Storage
Expense records are stored in a CSV file so that data can be loaded again when the application starts.

# 6. Exception Handling
The application handles common errors such as:
- Invalid amount
- Missing file
- Non-numeric values
- Empty fields
- Invalid user input

# Technologies Used
- Python 3
- CSV module
- File Handling
- Exception Handling
- Lists and Dictionaries
- Functions
- Conditional Statements
- Loops

# Project Structure
main.py
expenses.csv
file_handler.py
README.md

# File Description

File , Description 
 `main.py` , Contains the main menu and application logic 
 `file_handler.py` , Handles reading and writing expense data 
 `expenses.csv` , Stores expense records 
 `README.md` , Project documentation 

# CSV Data Format

The expense file uses the following columns:
Date, Category, Description, Amount
Example:
2026-09-19,Food,Lunch,250
2026-09-19,Travel,Bus,100
2026-09-19,Shopping,Clothes,1200

# How to Run

# Step 1: Install Python
Check that Python is installed:
python --version

# Step 2: Open the project folder
Open the terminal inside the `expense_tracker` folder.

# Step 3: Run the application
python main.py

# Main Menu
===== Expense Tracker =====
1. Add Expense
2. View Expenses
3. Total Expenses
4. Summary Report
5. Exit
Enter your choice:

# Sample Input
Enter your choice: 1

Enter date: 2026-09-19
Enter category: Food
Enter description: Lunch
Enter amount: 250

# Sample Output
Expense added successfully.

# View Expenses Example
===== All Expenses =====

Date         Category     Description       Amount
2026-09-19   Food         Lunch             250.00
2026-09-19   Travel       Bus               100.00
2026-09-19   Shopping     Clothes           1200.00

# Total Expense Example
===== Total Expenses =====
Total Spent: 1550.00

# Summary Report Example
===== Expense Summary =====
Total Entries: 3
Total Spent: 1550.00
Highest Expense: Shopping - 1200.00

# Exception Handling
The application handles common errors gracefully.
Example:
Enter amount: abc
Invalid amount. Please enter a numeric value.
If the expense file does not exist during the first run, the application handles the missing file and starts with empty records.

# Optional Enhancements
The following features can be added as extensions:
- Search expenses by category
- Monthly expense summary
- Sort expenses by amount
- Category-wise totals
- Export summary to a separate file

# Learning Outcomes
This project provides practice with:
- File handling
- CSV files
- Reading and writing data
- Append mode
- Exception handling
- Input validation
- Data processing
- Summary report generation

# Author
Tanvi Bramhankar