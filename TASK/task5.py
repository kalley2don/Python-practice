#Create a tuple with at least 5 different types of elements (int, float, string, bool, and complex).
#Use a for loop to iterate over the tuple and print each element along with its data type.
my_tuple = (42, 3.14, "Hello", True, 2+3j)
for element in my_tuple:
    print(f"Element: {element}, Type: {type(element)}")

#Create a list of 4 different city names.
#Use a for loop to print each city name followed by the phrase "is a great place"
cities = ["New York", "London", "Tokyo", "Paris"]
for city in cities:
    print(f"{city} is a great place")

#Ask the user to enter a word.
#Use a for loop and enumerate() to print each character of the string along with its index.
word = input("Enter a word: ")
for index, char in enumerate(word):
    print(f"Index: {index}, Character: {char}")

#Create a list of integers.
#Use a for loop to calculate the sum of all the elements and print the total
numbers = [8,9,12,36,100]
total_sum = 0
for num in numbers:
    total_sum += num
print(f"The total sum is: {total_sum}")

#Create a tuple containing different data types, including multiple True and False values.
#Use a for loop to count how many True values are present and print the count.
mixed_tuple = (42, 3.14, "Hello", True, False, 2+3j, True)
true_count = 0
for item in mixed_tuple:
    if item is True:
        true_count += 1
print(f"Number of True values in the tuple: {true_count}")

#Create a list with at least 6 elements of different types (int, float, str, bool, etc.).
#Use a for loop to iterate through the list and print the data type of each element.
mixed_list = [42, 3.14, "Hello", True, False, 2+3j]
for item in mixed_list:
    print(f"Element: {item}, Type: {type(item)}")

#Ask the user for a word.
#Use a for loop to check each character and print a message if it’s a vowel (a, e, i, o, u).
word = input("Enter a word: ")
vowels = "aeiouAEIOU"
for char in word:
    if char in vowels:
        print(f"{char} is a vowel.")

#Create a tuple of numbers from 1 to 5.
#Use a for loop to iterate through the tuple and print the square of each number
numbers_tuple = (1, 2, 3, 4, 5)
for num in numbers_tuple:
    print(f"Square of {num} is {num**2}")

#Create a list of 5 small letter containing words.
#Use a for loop to iterate over the list and print each word in lowercase.

words_list = ["apple", "banana", "cherry", "date", "elderberry"]
for word in words_list:
    print(word.lower())

#Create a list of integers.
#Use a for loop to count how many numbers in the list are greater than 10.
#Print the final count.
numbers = [8, 9, 12, 36, 100]
count_greater_than_10 = 0
for num in numbers:
    if num > 10:
        count_greater_than_10 += 1
print(f"Count of numbers greater than 10: {count_greater_than_10}")

