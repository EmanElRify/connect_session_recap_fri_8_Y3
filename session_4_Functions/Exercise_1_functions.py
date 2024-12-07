#Write a Python function called multiply_numbers that takes two arguments
# , num1 and num2. 
# Inside the function, calculate the product of these two numbers 
# and return the result.
def multiply_numbers(num1, num2):
    if num2 == 0:
        return "Please enter a non-zero value"
    print ("Thank you for using my calculator")
    return num1*num2

print(multiply_numbers(3, 0))

# print(f"The result is {multiply_numbers(3, 3)}")

def multiply_number(x , y):
    return x * y
print(multiply_number)

def greet(name):
    message = "Hello, " + name + "!"
    return message
print(greet("Eyad"))
#"Hello, Eyad!"