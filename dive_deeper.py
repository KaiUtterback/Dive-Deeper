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
# Task 1
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

# Task 3

if num1 == num2 and num2 == num3:
    print("All numbers are equal!")
if num1 == num2 and num1 == largest:
    print("the first two numbers are equal and the largest")
if num1 == num3 and num1 == largest: 
    print("the first and third numbers are equal and largest")
if num2 == num3 and num2 == largest:
    print("the second and third numbers are equal and largest")
    
# Question 4
# Task 1
# Write a Python Program that prompts the user to input a year. 
# The program should determine if the given year is a leap year or not. And display a message.

print("-" * 50)

import datetime

# Prompting the user to input a year
year = int(input("Enter a year: "))

# Getting the current year
current_year = datetime.datetime.now().year

# Checking if the given year is a leap year or not
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# Checking if the given year is a century year
if year % 100 == 0:
    print(f"{year} is a century year.")

# Comparing the given year with the current year
if year > current_year:
    print(f"{year} is in the future.")
elif year < current_year:
    print(f"{year} is in the past.")
else:
    print(f"{year} is the current year.")
    
# I had to do a lot of googling to figure out this datetime module. 
# It may be beneficial to go over that some more, or even modules in general
# in the future for other students.
