import turtle


# Function to perform arithmetic operation and check odd/even
def calculator(x, y, operation):
   # Check if inputs are integers and string
   if not (isinstance(x, int) and isinstance(y, int) and isinstance(operation, str)):
       print("Invalid input types. Please enter two integers and one string.")
       return None
  
   result = None
  
   # Perform arithmetic operation based on the string input
   if operation == "add":
       result = x + y
   elif operation == "subtract":
       result = x - y
   elif operation == "multiply":
       result = x * y
   elif operation == "divide":
       if y != 0:
           result = x / y
       else:
           print("Cannot divide by zero.")
           return None
   else:
       print("Invalid operation. Choose among 'add', 'subtract', 'multiply', or 'divide'.")
       return None
  
   # Check if the result is odd or even
   if result is not None:
       if result % 2 == 0:
           print(f"The result {result} is an even number.")
       else:
           print(f"The result {result} is an odd number.")


   return result


# Function to draw a rectangle using Turtle
def draw_rectangle(length, width):
   window = turtle.Screen()
   rectangle = turtle.Turtle()


   for _ in range(2):
       rectangle.forward(length)
       rectangle.right(90)
       rectangle.forward(width)
       rectangle.right(90)


   window.mainloop()


# Function to draw a circle using Turtle
def draw_circle(radius):
   window = turtle.Screen()
   circle = turtle.Turtle()


   circle.circle(radius)


   window.mainloop()


# Function to draw a square using Turtle
def draw_square(side_length):
   window = turtle.Screen()
   square = turtle.Turtle()


   for _ in range(4):
       square.forward(side_length)
       square.right(90)


   window.mainloop()


# Function to draw a star using Turtle
def draw_star():
   window = turtle.Screen()
   star = turtle.Turtle()


   for _ in range(5):
       star.forward(100)
       star.right(144)


   window.mainloop()


# Function to draw a house using other drawing functions
def draw_house(body_length, window_radius, window_length, window_width):
   window = turtle.Screen()
   house = turtle.Turtle()


   draw_square(body_length)


   house.penup()
   house.goto(-30, 0)
   house.pendown()
   draw_circle(window_radius)


   house.penup()
   house.goto(20, 20)
   house.pendown()
   draw_rectangle(window_length, window_width)


   house.penup()
   house.goto(-50, -50)
   house.pendown()
   draw_star()


   window.mainloop()


# Input prompt for user to enter arguments
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
operation = input("Enter operation (add, subtract, multiply, or divide): ")


# Call the calculator function with user inputs
calculator_result = calculator(x, y, operation)


# Call the draw_house function with specified dimensions
draw_house(150, 40, 80, 60)