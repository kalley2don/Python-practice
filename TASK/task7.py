#create a fuction greet(name,message="Welcome!") that prints; "hello,<name>!<message>"
#call the fuction with and without the message argument 
def greet(name, message="Welcome!"):
    print(f"Hello, {name}! {message}") 

greet("sushan")  # Calls with default message
greet("anish", "How are you today?")  # Calls with custom message

#create a fuction total(*numbers) that takes any number of numeric arguments and returns their sum
#example: total(5,10,15)should return 30   
def total(*numbers):
    return sum(numbers)

#create fucntion display_info(**details) that prints key value pairs like
#name:sushan
#age:25
#city:kathmandu
def display_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

#create a fuction repeat_words(*words,times=2) that repeats each word the given number of times
#example: repeat_words("hello","world",times=3) should print "hellohellohello" and "worldworldworld"
def repeat_words(*words, times=2):
    for word in words:
        print(word * times)

#create a fucntion user_profile(name,age=18,*hobbies,**extra_info) that
#prints the name and age
#prints all hobbies(if any)
#prints any additional info passed via **kwargs
def user_profile(name, age=18, *hobbies, **extra_info):
    print(f"Name: {name}")
    print(f"Age: {age}")
    
    if hobbies:
        print("Hobbies:")
        for hobby in hobbies:
            print(f"- {hobby}")
    
    if extra_info:
        print("Additional Information:")
        for key, value in extra_info.items():
            print(f"{key}: {value}")



