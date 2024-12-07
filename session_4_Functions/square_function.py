import turtle


    
length = 150
pen = turtle.Turtle()

def square(length):
    length = 100
    for i in range(4):
        pen.forward(length)
        pen.right(90)

def main():
    square(50)
    pen.forward(500)
    pen.color("red")

# print(length)
main()
turtle.done()