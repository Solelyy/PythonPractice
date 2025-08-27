#Set a secret number then let the user guess it. Keep looping until the user guess it correctly.

secret_num= 13
user_ans = int(input("Guess the secret number between 1 and 20: "))

while user_ans!=secret_num:
    if user_ans < 10:
        print("Too low!")
        user_ans= int(input("Guess again: "))
    elif user_ans <=12:
        print("So close...")
        user_ans= int(input("Guess again: "))
    else:
        print("Guess between 1 and 20 only!")
        user_ans= int(input("Guess again: "))

if user_ans == secret_num:
    print(f"Congrats! You guess the secret number: {secret_num}")
