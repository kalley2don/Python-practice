#use a while loop to print the numbers from 1 to 30
number = 1
while number <= 30:
    print(number)
    number += 1

#use a while loop to print all odd numbers from 1 to 20
number = 1
while number <= 20:
    if number % 2 != 0:
        print(number)
    number += 1

#use a while loop to print the word "hello" 5 times
count = 0  
while count < 5:
    print("hello")
    count += 1

#use a while loop to print numbers from 5 to 1
number = 5
while number >= 1:
    print(number)
    number -= 1

#use a while loop to print 3,6,9, ... upto 30
number = 3
while number <= 30:
    print(number)
    number += 3 

#keep asking the use to enter a number until they enter a positive number
while True:
    number = float(input("Enter a positive number: "))
    if number > 0:
        print("Thank you for entering a positive number.")
        break
    else:
        print("That's not a positive number. Please try again.")

#secret number is 7 
#ask the user to guess the number until its correct
secret_number = 7
while True:
    guess = int(input("Guess the secret number (between 1 and 10): "))
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print("Incorrect guess. Try again.")

#creat a fuction add (a,b) that returns the sum
def add(a, b):
    return a + b

#create a fuction multiply (a,b) that returns the product
def multiply(a,b):
    return a * b

#create a fuction check_even(numb)  that prints "even" or "odd" depending on the number
def check_even(numb):  
    if numb % 2 == 0:
        print("even")
    else:
        print("odd")
        
