# Objective: The aim of this assignment is to create a program that adjusts the quantities 
# of a recipe based on the number of servings, handling any type of arithmetic errors or user input exceptions.

# Task 1: Start
# Ask user the number of servings recipe is originally for
# and the number of servings they wish to make.

# Ensure that the user inputs are valid numbers and handle any ValueError from improper input.

omelet_recipe = {"eggs": 3, 
                  "milk": 1, 
                  "cheese": 2}

try:
    num_servings = int(input("How many servings does original recipe make? "))

    desired_servings = int(input("How many servings do you want to make today? "))

    adjustment_factor = int(desired_servings / num_servings)

   
    for ingredient, amount in omelet_recipe.items():
        new_amount = amount * adjustment_factor
    
        print(f"You will need to add {new_amount} {ingredient} to make the desired servings.")
        continue

except ValueError or ArithmeticError:
        if ValueError:
             print("Please make sure to enter valid numbers only.")
        else:
            print(ArithmeticError)

finally:
    print("Enjoy cooking this wonderful recipe!")
      
# Task 2: Quantity Calculation
# Calculate the adjustment factor by dividing the desired servings by the original servings.

# Use a try block to catch any arithmetic errors that may occur during the calculation.
   
    

# Task 3: Serving Success
# If the calculation is successful, display the adjusted recipe quantities to the user.

# Use a finally block to print a message 
# encouraging the user to enjoy their cooking, regardless of the outcome of the calculation.
    