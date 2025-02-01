def total_bill(bill_amount, tip_percentage):
    total = bill_amount * (1 + 0.01 * tip_percentage)
    total = round(total, 2)
    return total

user_bill = float(input("Enter the bill amount: "))
tip = float(input("Enter the tip percentage: "))

#final_amount = total_bill(user_bill, tip)
# print(f"Please pay ${final_amount:}")


print(total_bill(user_bill,tip))