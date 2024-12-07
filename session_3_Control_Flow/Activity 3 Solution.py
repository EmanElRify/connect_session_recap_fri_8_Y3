import random


# Create a list of 12 random integers
random_integers = [random.randint(-100, 100) for _ in range(12)]


# Loop over numbers and perform checks
for num in random_integers:
   print(f"Number: {num}")
  
   # Check if the number is even or odd
   if num % 2 == 0:
       print("  - This number is even")
   else:
       print("  - This number is odd")
  
   # Check if the number is positive or negative
   if num > 0:
       print("  - This number is positive")
   elif num < 0:
       print("  - This number is negative")
   else:
       print("  - This number is zero")
  
   # Check if the number matches a specific number in mind (e.g., 10)
   specific_number = 10
   if num == specific_number:
       print("  - This number matches the specific number in mind")
  
   # Arithmetic operations based on conditions
   if num > 0:
       squared_num = num ** 2
       print(f"  - Square of this number: {squared_num}")
   elif num < 0:
       absolute_num = abs(num)
       print(f"  - Absolute value of this number: {absolute_num}")


# Calculator Simulator
var1 = 0
var2 = 0
var3 = 0


while True:
   print("\nCalculator Simulator")
   print(f"Current value in var3: {var3}")
   user_input = input("Enter variable 1, operator (+, -, *, /), variable 2, = (e.g., 5 + 3 =): ")


   if user_input.lower() == 'c':
       var3 = 0
       print("Variable 3 has been reset to zero.")
       continue
   elif user_input.lower() == 'exit':
       break


   parts = user_input.split()
   if len(parts) != 4 or parts[3] != '=':
       print("Invalid input format. Please follow the format: variable 1, operator, variable 2, =")
       continue


   var1 = float(parts[0])
   operator = parts[1]
   var2 = float(parts[2])


   if operator == '+':
       var3 += var1 + var2
   elif operator == '-':
       var3 += var1 - var2
   elif operator == '*':
       var3 += var1 * var2
   elif operator == '/':
       if var2 != 0:
           var3 += var1 / var2
       else:
           print("Cannot divide by zero!")
           continue
   else:
       print("Invalid operator. Please enter a valid operator (+, -, *, /) or 'C' to reset.")