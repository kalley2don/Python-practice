##Create three variables: one integer, one float, and one complex number##
my_int = 42
my_float = 3.14
my_complex = 1 + 2j

if __name__ == "__main__":
    print("my_int:", my_int)
    print("my_float:", my_float)
    print("my_complex:", my_complex)
##print each variable and use the type() function to confirm their data types.
    print("Type of my_int:", type(my_int))
    print("Type of my_float:", type(my_float))
    print("Type of my_complex:", type(my_complex))

    #Create one int variable (a) and one float variable (b)
#Print the sum, difference, product, and quotient of a and b	
#Print the type() of each result (notice how types may change).
    a = 10
    b = 3.0
    print("Sum:", a + b, "Type:", type(a + b))
    print("Difference:", a - b, "Type:", type(a - b))
    print("Product:", a * b, "Type:", type(a * b))
    print("Quotient:", a / b, "Type:", type(a / b))

# Let x = 10 and y = 7.
#Print the results of x > y, x < y, x == y, and x != y.
#After observing the output, explain why each result is True or False in comments.
    x = 10
    y = 7
    print("x > y:", x > y)  # True because 10 is greater than 7
    print("x < y:", x < y)  # False because 10 is not less than 7
    print("x == y:", x == y)  # False because 10 is not equal to 7
    print("x != y:", x != y)  # True because 10 is not equal to 7

#Define a variable status = True.
#Print the value of status and confirm it is a boolean using type(status).
#Reassign status to False and confirm its type again.
status = True
print("Status:", status, "Type:", type(status))  # Status: True Type: <class 'bool'>
status = False
print("Status:", status, "Type:", type(status))  # Status: False Type: <class 'bool'>

#Create a string variable, for example text = "Hello World".
#Use len(text) to print its length.
#Use type(text) to verify it is a string.
text = "Hello World"
print("Text:", text)    
print("Length of text:", len(text))  # Length of text: 11
print("Type of text:", type(text))  # Type of text: <class 'str'>

#With the string s = "Python", print each character. Then print just the first and last characters using negative indexing.
s = "Python"
print("Each character in s:")
for char in s:
    print(char)
print("First character:", s[0])  # First character: P
print("Last character:", s[-1])  # Last character: n

#Let lang = "Programming".
#Print the substring from index 0 to index 4.
#Print the substring from index 3 to the end.
#Print the substring that omits the first 2 and last 2 characters
lang = "Programming"
print("Substring from index 0 to 4:", lang[0:5])  # Substring from index 0 to 4: Program
print("Substring from index 3 to the end:", lang[3:])  # Substring from index 3 to the end: gramming
print("Substring that omits the first 2 and last 2 characters:", lang[2:-2])  # Substring that omits the first 2 and last 2 characters: ogrammin


#Continue using lang = "Programming".
#Slice lang to get "Program" and store it in a variable part1.
#Print len(part1) and comment how it differs from len(lang).
part1 = lang[0:7]
print("part1:", part1)  # part1: Program
print("Length of part1:", len(part1))  # Length of part1: 7
print("Length of lang:", len(lang))  # Length of lang: 11
# The length of part1 is 7, which is less than the length of lang (11), because part1 only contains the first 7 characters of lang.

#Let phrase = "Hello, Python!".
#Print phrase.upper() and phrase.lower().
#Print the original phrase to show it remains unchanged (strings are immutable).
phrase = "Hello, Python!"
print("Uppercase:", phrase.upper())  # Uppercase: HELLO, PYTHON!
print("Lowercase:", phrase.lower())  # Lowercase: hello, python!
print("Original phrase:", phrase)  # Original phrase: Hello, Python!

#Create two strings, str1 = "Data" and str2 = "Science".
#Combine them into a single string with a space in between and print it.
#Print the length of the combined string.
str1 = "Data"
str2 = "Science"
combined = str1 + " " + str2
print("Combined string:", combined)  # Combined string: Data Science
print("Length of combined string:", len(combined))  # Length of combined string: 11

#Let word = "example".
#Call word.upper() but do not store it, then print word.
#Now set word = word.upper(), then print word.
#Comment on why the second print is different from the first.
word = "example"
print("Original word:", word)  # Original word: example
word.upper()  # This call does not change the value of word because strings are immutable
print("Word after calling upper() without storing:", word)  # Word after calling upper() without storing: example
word = word.upper()  # This assigns the uppercase version of word to itself
print("Word after reassigning with uppercase:", word)  # Word after reassigning with uppercase: EXAMPLE

#Define a = 5, b = 3, c = 2.
#Print the result of the expression a + b * c.
#Print the result of (a + b) * c.
#In comments, explain how operator precedence affects the outcome.
a = 5
b = 3
c = 2
print("Result of a + b * c:", a + b * c)  # Result of a + b * c: 11 (multiplication is done first due to operator precedence)
print("Result of (a + b) * c:", (a + b) * c)  # Result of (a + b) * c: 16 (parentheses override operator precedence, so addition is done first)

#Let text = "Hello".
#Attempt to access an index that doesn’t exist, like text[10].
#Observe the error message (IndexError) and explain why it happens in comments.
text = "Hello"
try:
    print(text[10])  # This will raise an IndexError because index 10 is out of range for the string "Hello" which has indices 0-4.
except IndexError as e:
    print("Error:", e)  # Error: string index out of range

#Create two variables with the same string value, s1 = "test" and s2 = "test".
#Use the == operator to compare them, then use the is operator.
#Explain in comments what each comparison checks
s1 = "test"
s2 = "test"
print("s1 == s2:", s1 == s2)  # s1 == s2: True (compares the values of the strings)
print("s1 is s2:", s1 is s2)  # s1 is s2: True (compares the identity of the strings, i.e., whether they refer to the same object in memory)

#Define z = 3 + 4j.
#Print the real part (z.real) and the imaginary part (z.imag).
#Confirm that its type is complex using type(z).
z = 3 + 4j
print("Real part of z:", z.real)  # Real part of z: 3.0
print("Imaginary part of z:", z.imag)  # Imaginary part of z: 4.0
print("Type of z:", type(z))  # Type of z: <class 'complex'>

#Let f1 = 0.1 + 0.2 and f2 = 0.3.
#Print f1 == f2.
#Print the actual values of f1 and f2 to explain any difference in the comparison outcome (floating-point precision).
f1 = 0.1 + 0.2
f2 = 0.3
print("f1 == f2:", f1 == f2)  # f1 == f2: False (due to floating-point precision errors)
print("f1:", f1)  # f1: 0.30000000000000004
print("f2:", f2)  # f2: 0.3

