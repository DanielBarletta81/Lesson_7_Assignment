#Task 3: User Experience
# Implement an else block that prints the converted temperature in a user-friendly format.

# Add a finally block that thanks the user for using the weather forecast application, ensuring that 
# this message is displayed regardless of whether an exception was caught or not.

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
            
        except ZeroDivisionError as zde:
             print(zde)
        except OverflowError as oe:
             print(oe)
        else:
             print(f"The temperature you entered is {converted_temp} degrees Celsius.")
        finally:
             print("Thank you for using our weather forecast app, your input helps us provide a better user experience!")
             
convert_to_celsius()