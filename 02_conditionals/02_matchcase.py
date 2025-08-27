#matchcase is a switchcase in other languages

first_num= int(input("Enter first number: "))
second_num= int(input("Enter second number: "))

print()
choice= int(input("Select an operation [1-4]:\n\n" 
                   "1- Add \n2- Subract \n3- Multiply \n4- Divide \n"
                   "Enter choice: "))

print()
match choice:
    case 1:
        result= first_num + second_num
        print(f"Result: {first_num} + {second_num} = {result}")
    case 2:
        result= first_num - second_num
        print(f"Result: {first_num} - {second_num} = {result}") 
    case 3:
        result= first_num * second_num
        print(f"Result: {first_num} * {second_num} = {result}")
    case 4:
        if second_num == 0:
            print("Error: Division by 0 is not allowed.")
        else:
            result= first_num / second_num
            print(f"Result: {first_num} / {second_num} = {result: .2f}")
    case _: 
        print("Invalid input! Please input from 1-4 only.") 
