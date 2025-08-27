#practice of computation in python and type conversion
#Objective: Ask for length and width, then give the area and perimeter

length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width
perimeter= 2 * (length + width)

print()
print(f"Area: {area:.2f}")
print(f"Perimeter: {perimeter:.2f}")