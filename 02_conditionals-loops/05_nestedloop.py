#Challenge: Multiplication Table with User Control
"""Ask the user for a number and print its multi table up to 10.
Ask if want to add another number again, if yes repeat the process. If no, exit."""

while True:
    num= int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

    choice= input("Do you want to see another table? (y/n): ")
    if choice.lower() != "y":
        print("Good bye!")
        break

#For multiple numbers: 
"""
while True:
    nums = input("Enter number(s), separated by commas: ")
    nums = [int(x.strip()) for x in nums.split(",")]

    for num in nums:
        print(f"\nMultiplication table for {num}")
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")

    choice = input("\nDo you want to see another table? (y/n): ")
    if choice.lower() != "y":
        print("Good bye!")
        break 
"""