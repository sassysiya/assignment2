a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

if a+b>c and a+c>b and b+c>a:
    print(f"Yes , it is possible to make a triangle using {a},{b},{c} as the sides of a triangle.")
else:
    print(f"No, triangle cannot be formed using {a},{b},{c} as the sides")


