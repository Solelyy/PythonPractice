#Build a simple Mini-ATM Simulator
"""
1. Ask the user for a PIN code (4 digits), 
if the pin is wrong keep asking (max 3 attempts -> then exit),
2. Once logged in, show a menu:
    1. Check Balance
    2. Deposit Money
    3. Withdraw Money
    4. Exit
3. User chooses an option:
    Check balance -> Show current balance
    Deposit → Ask how much, add to balance.
    Withdraw → Ask how much, subtract if enough balance, else show "Insufficient funds".
    Exit → Break loop, say “Thank you!”.
4. After each operation (except Exit), go back to the menu.
"""

pin_code= 1234
attempt= 0
max_attempt= 3
logged_in= False

user_balance = 0

while attempt < max_attempt:
    user_pin= int(input("Enter PIN: "))
    if user_pin == pin_code:
        print("Welcome!")
        logged_in= True
        break
    else:
        attempt +=1
        print(f"Incorrect PIN. Attempts left: {max_attempt- attempt}")

if logged_in:
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check balance \n2. Deposit Money \n3. Withdraw \n4. Exit")
        user_choice= int(input("Enter choice [1-4]: "))
            
        match user_choice:
            case 1:
                print(f"Balance: {user_balance: .2f}")
                continue
            case 2:
                deposit= float(input("Deposit amount: "))
                if deposit > 0:
                    user_balance += deposit
                    print(f"New Balance: ₱{user_balance:,.2f}")
                else:
                    print("Invalid deposit amount!")
                continue
            case 3:
                print(f"Balance: {user_balance: .2f}")
                withdrawal = float(input("Withdraw amount: "))
                if withdrawal <= user_balance:
                    user_balance -= withdrawal
                    print(f"New balance: ₱{user_balance:,.2f}")
                    continue
                else:
                    print("Insufficient balance!")
                    continue
            case 4:
                print("Thank you! Exiting...")
                break
            case _:
                print("Enter between 1 and 4 only.")
        break
else:
    print("Too many attempts! Access denied.")