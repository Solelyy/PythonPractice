#ask a user for a number and print its multiplication table up to 10.

number= int(input("Enter a number: "))

for i in range (1, 11):
    ans = number * i
    print(f"{number} x {i} = {ans}")

#this is the countdown, ex: 5 x 10 = 50, 5 x 9 = 45...
'''for i in range (10, 0, -1):
    ans = number * i
    print(f"{number} x {i} = {ans}") '''

