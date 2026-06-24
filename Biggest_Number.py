# Biggest Number Project 🏆
# This project compares numbers to find the biggest one.

print("=== Biggest Number Finder ===")

# Ask the user for 3 numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Compare the numbers
if num1 > num2 and num1 > num3:
    print(num1, "is the biggest number!")

elif num2 > num1 and num2 > num3:
    print(num2, "is the biggest number!")

elif num3 > num1 and num3 > num2:
    print(num3, "is the biggest number!")

else:
    print("Some numbers are equal!")