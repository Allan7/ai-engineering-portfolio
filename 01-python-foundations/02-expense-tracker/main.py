# Expense Tracker - Version 1
# Goal: Record multiple expenses and display a simple spending summary.


# SETUP
# Create somewhere to store all expenses entered by the user.
expenses = []

# MAIN PROGRAM LOOP
# Keep asking the user to enter expenses until they choose to stop.
add_expense = input('Do you need to add a new expense? ')

while add_expense == 'yes':
    new_expense = {}
    new_expense['expense'] = input('What is the expense?')

    while True:
        try:
            new_expense['amount'] = float(input('What is the amount?'))
            break
        except ValueError:
            print('That is not a valid number. Please try again.')

    new_expense['category'] = input('What category?')
    expenses.append(new_expense)

    add_expense = input('Do you need to add a new expense? ')

print("expense | category | amount")
for expense in expenses:
    print(f"{expense['expense']} | {expense['category']} | £{expense['amount']:.2f}")

total_amount = 0

for expense in expenses:
    total_amount = total_amount + expense['amount']

print(f"Total expense: £{total_amount:.2f}")
    # GET EXPENSE NAME
    # Ask the user what the expense was for.


    # GET EXPENSE AMOUNT
    # Ask the user how much the expense cost.
    # Convert the input into a suitable numeric type.
    # Handle invalid input so the program does not crash.


    # GET CATEGORY
    # Ask the user which category the expense belongs to.


    # CREATE EXPENSE
    # Store the name, amount, and category together as one expense.


    # STORE EXPENSE
    # Add the new expense to the collection of all expenses.


    # ADD ANOTHER?
    # Ask whether the user wants to enter another expense.
    # Validate the answer.
    # Continue entering expenses or leave the main loop.


# DISPLAY EXPENSES
# Show every expense the user entered.
# Display the name, category, and amount clearly.


# CALCULATE TOTAL
# Work through all stored expenses.
# Add their amounts together.
# Display the total amount spent.