#Task 1: Start
#Begin by setting up a simple user input loop that asks the user to enter the temperature in Fahrenheit.

#Ensure that your program only accepts numerical input and provides
# a friendly error message if the user enters something that can't be converted to a number.

while True:
    
    try:
        user_temp = int(input("What is today's temperature in Fahrenheit? "))
        print(f"You have entered {user_temp} degrees Fahrenheit.")
        break
    except ValueError:
        print("Please enter only numerical characters for your input.")