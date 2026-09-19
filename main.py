while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Summary Report")
    print("5. Search by category")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        date = input("Enter date: ")
        category = input("Enter category: ")
        description = input("Enter description: ")

        try:
            amount = float(input("Enter amount: "))
        except ValueError:
            print("Invalid amount.")
            continue

        print("Expense added successfully.")

    elif choice == "2":
        try:
            with open("expenses.csv", "r") as file:
                lines = file.readlines()

            for line in lines:
                print(line.strip())

        except FileNotFoundError:
            print("expenses.csv file not found.")

    elif choice == "3":
        import csv

        try:
            with open("expenses.csv", "r") as file:
                expenses = csv.DictReader(file)

                total = 0

                for expense in expenses:
                    total += float(expense["Amount"])

            print(f"Total Spent: {total:.2f}")

        except FileNotFoundError:
            print("expenses.csv file not found.")

        except ValueError:
            print("Invalid amount found in expenses.csv.")

    elif choice == "4":
        import csv

        try:
            with open("expenses.csv", "r") as file:
              expenses = list(csv.DictReader(file))

            if not expenses:
               print("No expenses found.")
               continue

            total_entries = len(expenses)

            total_spent = 0
            for expense in expenses:
               total_spent += float(expense["Amount"])

            highest = max(
               expenses,
               key=lambda x: float(x["Amount"])
            )

            print("\n===== Expense Summary =====")
            print(f"Total Entries: {total_entries}")
            print(f"Total Spent: {total_spent:.2f}")
            print(
            f"Highest Expense: {highest['Category']} - "
            f"{float(highest['Amount']):.2f}"
            )

        except FileNotFoundError:
           print("expenses.csv file not found.")

        except ValueError:
           print("Invalid amount found in expenses.csv.")

    elif choice == "5":
        import csv
        category = input("Enter category: ")
        try:
            with open("expenses.csv", "r") as file:
                expenses = list(csv.DictReader(file))
            found = False
            for expense in expenses:
                if expense["Category"].lower() == category.lower():
                  print(expense)
                  found = True

            if not found:
                print("No expenses found for this category.")

        except FileNotFoundError:
            print("expenses.csv file not found.")
            
    elif choice == "6":
        print("Exiting Expense Tracker...")
        break

    else:
        print("Invalid choice. Please try again.")