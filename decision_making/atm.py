"""
✅ 5. ATM Withdrawal

Task:
Ask for PIN.

If PIN is correct:

Ask for withdrawal amount

If amount ≤ balance → "Withdrawal successful"

Else → "Insufficient balance"

Else → "Incorrect PIN"

"""


db_pin = 1234

db_balance = 5000

pin = int (input("enter PIN "))

if db_pin == pin:

    amount =int( input("enter amount "))

    if amount < db_balance:

        print("trascation success")

    else:

        print("insufficient balance")
else:

    print("incorrect pin")

