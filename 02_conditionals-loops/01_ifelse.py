#print what age category they are belong

age = int(input("Enter age: "))

if age <= 1:
    print("You're such a baby little cutie!")
elif age <=3:
    print("You're a toddler.")
elif age <= 12:
    print("You're a kiddo.")
elif age <= 17:
    print("You're a teen.")
elif age <= 25:
    print("You're already a young adult!")
elif age <= 64:
    print("Definitely an adult!")
else:
    print("Already a senior.")