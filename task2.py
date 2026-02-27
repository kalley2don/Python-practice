#Create a List:
#Create a list containing the numbers 1 through 15. Print the list.
numbers = list(range(1, 16))
print("List of numbers 1 through 15:", numbers)

#List of Strings:
# Create a list of your five favorite fruits. Print the list.
favorite_fruits = ["apple", "banana", "orange", "grape", "kiwi"]
print("Favorite fruits:", favorite_fruits)

#Accessing Elements:
#Given the list [10, 20, 30, 40, 50], print the first and last element using positive and negative indexing.
list1 = [10, 20, 30, 40, 50]
print("First element (positive indexing):", list1[0])
print("Last element (negative indexing):", list1[-1])

#List Length:
#Create a list of any 5 items and print its length using the len() function.
list2 = ["a", "b", "c", "d", "e"]
print("Length of list2:", len(list2))

#Appending Elements:
#Start with an empty list and append the numbers 1, 2, and 3. Print the list.
empty_list = []
empty_list.append(1)
empty_list.append(2)
empty_list.append(3)
print("List after appending 1, 2, and 3:", empty_list)

# Inserting an Element:
given_list = [1, 3, 4]
given_list.insert(1, 2)
print("List after inserting 2:", given_list)

# Removing an Element:
list3 = [1, 2, 3, 4, 5]
list3.remove(3)
print("List after removing 3:", list3)

# Popping an Element:
list4 = [10, 20, 30, 40]
popped_element = list4.pop()
print("Popped element:", popped_element)
print("Updated list:", list4)

# Slicing a List:
list5 = [0, 1, 2, 3, 4, 5]
slice_result = list5[2:5]
print("Slice from index 2 to 4:", slice_result)

# List Concatenation:
list6 = [1, 2, 3]
list7 = [4, 5, 6]
concatenated_list = list6 + list7
print("Concatenated list:", concatenated_list)

# Repeating a List:
list8 = [1, 2]
repeated_list = list8 * 3
print("Repeated list:", repeated_list)

#Copying a List:
#Create a copy of a given list and print both the original and the copy.
original_list = [1, 2, 3, 4, 5]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)

#Clearing a List:
#Given any list, use a method to clear all its elements and then print the empty list.
clear_list = [1, 2, 3, 4, 5]
print("Before clearing:", clear_list)
clear_list.clear()
print("After clearing:", clear_list)