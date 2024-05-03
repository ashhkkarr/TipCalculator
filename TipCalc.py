def calculate_tip(amount, tip_percent):
    tip_amount = amount * (tip_percent / 100)
    return tip_amount

def total_bill_amount(amount, tip_percent):
    tip_amount = calculate_tip(amount, tip_percent)
    total_amount = amount + tip_amount
    return total_amount

bill_amount = float(input("Enter the bill amount: "))
tip_percentage = float(input("Enter the tip percentage: "))

tip = calculate_tip(bill_amount, tip_percentage)
total_bill = total_bill_amount(bill_amount, tip_percentage)

print(f"Tip amount: ${tip:.2f}")
print(f"Total bill amount: ${total_bill:.2f}")
