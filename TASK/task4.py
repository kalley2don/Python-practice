# Write a program that prompts the user for an integer.
#Use if/else to check whether the number is even or odd.
#Print "Even" or "Odd" accordingly
number = int(input("Enter an integer: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

#Write a program that prompts the user for a number.
#Use if/elif/else to determine if the number is positive, negative, or zero.
#Print a message such as "The number is positive.".
number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#Prompt the user for a number between 0 and 100 (the score).
#Use if/elif/else to categorize the score:
#90–100: "Grade A"
#80–89: "Grade B"
#70–79: "Grade C"
#< 70: "Fail"
score = float(input("Enter a score between 0 and 100: "))
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Fail")

#Prompt the user for a single integer n.
# Use a for loop to iterate from 1 up to n (inclusive).
# For each value i, print:
# "Multiple of both" if i is divisible by 3 and 5.
# "Multiple of 3" if i is divisible by 3 but not 5.
# "Multiple of 5" if i is divisible by 5 but not 3.
# The number i itself otherwise   
n = int(input("Enter a positive integer n: "))
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("Multiple of both")
    elif i % 3 == 0:
        print("Multiple of 3")
    elif i % 5 == 0:
        print("Multiple of 5")
    else:
        print(i)

#Prompt the user for a password (e.g., "secret").
#Use if to check if the user’s input matches the correct password.
#If correct, print "Access granted", otherwise print "Access denied".
password = input("Enter the password: ")
if password == "secret":
    print("Access granted")
else:
    print("Access denied")

#Ask the user for a string.
#Use a for loop to iterate over each character.
#Use if conditions to check if it’s a vowel ("a", "e", "i", "o", "u").
#Count the total number of vowels and print the result.
string = input("Enter a string: ")
vowel_count = 0
vowels = "aeiouAEIOU"
for char in string:
    if char in vowels:
        vowel_count += 1
print(f"Total number of vowels: {vowel_count}")

#Prompt the user for three different numbers.
#Use if/elif/else to find and print which one is smallest
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if num1 <= num2 and num1 <= num3:
    print(f"The smallest number is {num1}")
elif num2 <= num1 and num2 <= num3:
    print(f"The smallest number is {num2}")
else:
    print(f"The smallest number is {num3}")

#Prompt the user to choose an option (e.g., 1 for "Start", 2 for "Settings", 3 for "Exit").
#Use if/elif/else to print a response based on which option is chosen.
#Example:
#If user enters 1: print "Game starting..."
#If user enters 2: print "Opening settings..."
#If user enters 3 or any other: print "Exiting..."
option = int(input("Choose an option (1 for Start, 2 for Settings, 3 for Exit): "))
if option == 1:
    print("Game starting...")
elif option == 2:
    print("Opening settings...")
else:
    print("Exiting...")

#Use a for loop to print the numbers from 1 to 10, each on a new line.
for i in range(1, 11):
    print(i) 

#Ask the user for a string.
#Use a for loop to print each character of the string on a new line.
string = input("Enter a string: ")
for char in string:
    print(char)

#Use a for loop to print all even numbers from 1 to 50 (inclusive).
for i in range(2, 51, 2):
    print(i)

#Have a list of scores, e.g., scores = [85, 42, 78, 99, 65].
#Use a for loop to iterate over each score.
#Use if/elif/else inside the loop to categorize each score as "Pass" (>= 60) or "Fail" (< 60).
#Print each score with its category.
scores = [85, 42, 78, 99, 65]
for score in scores:
    if score >= 60:
        print(f"{score}: Pass")
    else:
        print(f"{score}: Fail")

#Ask the user to enter their name.
#Use a for loop to print their name 3 times        
name = input("Enter your name: ")
for _ in range(3):
    print(name)


a = 25
b = 65
print(" The sum of a and b is:", a + b)
