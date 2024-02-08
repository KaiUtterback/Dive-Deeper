# 1 Decisions at the Crossroad
# Question 1 Task 1 Code Correction
print( )
print("-" * 50)

number = int(input("Enter a number: "))

if number > 0:
    print("The Number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative")

# Question 2 Task 1 Code Correction
print("-" * 50)
    
choice = input("Do you choose the path to the left or right? ")

if choice == "left":
    print("You find a treasure chest!")
elif choice == "right":
    print("You encounter a dragon!")
else: 
    print("Invalid choice!")

# Question 3
print("-" * 50)
    
""" 
Task 1 Identify the Greatest:L
Write a Python program that prompts the user to enter three numbers.
The program should then identify and print out the largest number of the three.
"""

print("Please enter 3 numbers below.")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

largest = 0

if num1 >= largest:
    largest = num1
if num2 >= largest:
    largest = num2
if num3 >= largest:
    largest = num3

print("The largest number is ", largest)

# Task 2

smallest = 0

if num1 <= largest:
    smallest = num1
if num2 <= smallest:
    smallest = num2
if num3 <= smallest:
    smallest = num3 
    
print("The smallest is", smallest)