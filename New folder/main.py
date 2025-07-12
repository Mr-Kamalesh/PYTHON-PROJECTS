import os

# Function to add an expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Travel, etc.): ")
    amount = float(input("Enter amount: ₹"))
    description = input("Enter description: ")

    with open("expenses.txt", "a") as file:
        file.write(f"{date},{category},{amount},{description}\n")
    print("✅ Expense added successfully!\n")

# Function to view all expenses
def view_expenses():
    if not os.path.exists("expenses.txt"):
        print("⚠ No expenses found.")
        return

    print("\nAll Expenses:")
    print("-" * 50)
    with open("expenses.txt", "r") as file:
        for line in file:
            date, category, amount, description = line.strip().split(",")
            print(f"Date: {date}, Category: {category}, Amount: ₹{amount}, Description: {description}")
    print("-" * 50 + "\n")

# Function to search by date
def search_by_date():
    search_date = input("Enter date to search (YYYY-MM-DD): ")
    found = False
    print(f"\nExpenses on {search_date}:")
    print("-" * 50)
    with open("expenses.txt", "r") as file:
        for line in file:
            date, category, amount, description = line.strip().split(",")
            if date == search_date:
                print(f"Category: {category}, Amount: ₹{amount}, Description: {description}")
                found = True
    if not found:
        print("⚠ No expenses found on that date.")
    print("-" * 50 + "\n")

# Function to show total expenses
def total_expenses():
    total = 0
    with open("expenses.txt", "r") as file:
        for line in file:
            _, _, amount, _ = line.strip().split(",")
            total += float(amount)
    print(f"\n💰 Total Expenses: ₹{total}\n")

# Main program loop
def main():
    while True:
        print("📊 Expense Tracker Menu")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Search Expenses by Date")
        print("4. Show Total Expenses")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            search_by_date()
        elif choice == '4':
            total_expenses()
        elif choice == '5':
            print("👋 Exiting... Thank you for using Expense Tracker!")
            break
        else:
            print("❌ Invalid choice! Please select between 1 to 5.\n")

# Run the program
main()
