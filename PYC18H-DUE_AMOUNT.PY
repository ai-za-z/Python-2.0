def calculate_due_amount():
    total_bill = float(input("Enter the total bill amount: "))
    amount_paid = float(input("Enter the amount paid: "))
    if amount_paid > total_bill:
        print("Error: Amount paid cannot exceed the total bill.")
    else:
        due_amount = total_bill - amount_paid
        print(f"The due amount is: {due_amount:.2f}")

calculate_due_amount()
