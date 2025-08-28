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