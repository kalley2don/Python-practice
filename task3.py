#Create a Tuple:
#Create a tuple containing the numbers 1, 2, and 3. Print the tuple.
numbers = (1, 2, 3)
print("Tuple of numbers:", numbers) 

#Tuple of Strings:
#Create a tuple of three different color names and print it.
colors = ("red", "green", "blue")
print("Tuple of colors:", colors)

#Accessing Tuple Elements:
#Given the tuple (10, 20, 30, 40), print the second element.
tuple_elements = (10, 20, 30, 40)
print("Second element:", tuple_elements[1])

#Tuple Slicing:
#Using the tuple (0, 1, 2, 3, 4), print a slice that contains elements from index 1 to 3.
tuple_slice = (0, 1, 2, 3, 4)
print("Slice from index 1 to 3:", tuple_slice[1:4]) 

#Concatenating Tuples:
#Concatenate two tuples, e.g., (1, 2) and (3, 4), and print the result.
tuple1 = (1, 2)
tuple2 = (3, 4)
concatenated_tuple = tuple1 + tuple2
print("Concatenated tuple:", concatenated_tuple)

#Tuple Unpacking:
#Store the tuple ("Alice", 25, "New York") into three variables and print them.
person_tuple = ("Alice", 25, "New York")
name, age, city = person_tuple
print("Name:", name)
print("Age:", age)
print("City:", city)

#Convert List to Tuple:
#Convert the list [1, 2, 3, 4] into a tuple and print the tuple.
list_to_convert = [1, 2, 3, 4]
tuple_from_list = tuple(list_to_convert)
print("Tuple from list:", tuple_from_list)

# Counting Occurrences:
#Given the tuple (1, 2, 2, 3, 2), count how many times the number 2 appears.
tuple_with_duplicates = (1, 2, 2, 3, 2)
count_of_twos = tuple_with_duplicates.count(2)
print("Count of number 2:", count_of_twos)

#Finding an Index:
#In the tuple (10, 20, 30, 40), find the index of the element 30 and print it.
index_of_thirty = tuple_elements.index(30)
print("Index of element 30:", index_of_thirty)
