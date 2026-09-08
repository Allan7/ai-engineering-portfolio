# Expense Tracker - Version 2
# Goal: Record multiple expenses and display a simple spending summary.


def get_expense():
    new_expense = {}
    new_expense['expense'] = input('What is the expense? ')

    while True:
        try:
            new_expense['amount'] = float(input('What is the amount? '))
            break
        except ValueError:
            print('That is not a valid number. Please try again.')

    new_expense['category'] = input('What category? ')

    return new_expense


def calculate_total_amount(expenses):
    total_amount = 0

    for expense in expenses:
        total_amount = total_amount + expense['amount']

    return total_amount


def calculate_category_totals(expenses):
    category_totals = {}

    for expense in expenses:
        category = expense['category']
        amount = expense['amount']

        if category not in category_totals:
            category_totals[category] = amount
        else:
            category_totals[category] = category_totals[category] + amount

    return category_totals


# SETUP
expenses = []

# MAIN PROGRAM LOOP
add_expense = input('Do you need to add a new expense? ')

while add_expense == 'yes':
    new_expense = get_expense()
    expenses.append(new_expense)

    add_expense = input('Do you need to add a new expense? ')


# DISPLAY EXPENSES
print("expense | category | amount")

for expense in expenses:
    print(f"{expense['expense']} | {expense['category']} | £{expense['amount']:.2f}")


# TOTAL SPEND
total_amount = calculate_total_amount(expenses)
print(f"Total expense: £{total_amount:.2f}")


# CATEGORY TOTALS
category_totals = calculate_category_totals(expenses)

for category, amount in category_totals.items():
    print(f"{category} | £{amount:.2f}")