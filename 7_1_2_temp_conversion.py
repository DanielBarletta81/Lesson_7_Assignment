#Task 2: Temperature Conversion
# Write a function that converts the Fahrenheit temperature to Celsius. 
# Remember that the formula is (Fahrenheit - 32) * 5/9.

# Use a try block to catch any potential errors during the conversion process, 
# such as division by zero or overflow errors.

while True:
    
    try:
        user_temp = int(input("What is today's temperature in Fahrenheit? "))
        print(f"You have entered {user_temp} degrees Fahrenheit.")
        break
    except ValueError:
        print("Please enter only numerical characters for your input.")

def convert_to_celsius():
        try:
            converted_temp = round((user_temp - 32) * 5/9)
            print(f"The temperature entered is {converted_temp} degrees Celsius.")
        except ZeroDivisionError as zde:
             print(zde)
        except OverflowError as oe:
             print(oe)
             
convert_to_celsius()