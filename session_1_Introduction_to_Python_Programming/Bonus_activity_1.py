import turtle 
import random

home = turtle.Turtle()  #القلم اللي هنرسم بيه البيت
star = turtle.Turtle()  # القلم اللي هنرسم بيه النجوم
star.speed(0) #هنرسم النجوم بسرعة عالية
star.color("white")  #لون النجوم هيكون ابيض 

turtle.Screen().bgcolor("blue")  #blue sky (background)  لون السما هيكون ازرق
#Let's draw random stars in the sky with random sizes يلا نرسم نجوم عشوائية باحجام مختلفة في السما الاول

# Set up the screen بنضبط حجم الشاشة عشان نحط النجوم في حدودها ومنطلعش برا
screen = turtle.Screen()  #هنا عرفنا الشاشة بتاعتنا 
width = screen.window_width()             #عرض الشاشة المصغرة
height = screen.window_height()           #طول الشاشة المصغرة
n = 50  #stars number عدد النجوم اللي هنرسمها
star.fillcolor("white")

for _ in range(n):   #بنعمل حلقة نحدد في كل لفة موقع عشوائي في الاسكرين وهنرسم في الموقع دا نجمة
    
    #لو عرض الشاشة 100 يبقا احداثيات الشاشة بتكون من -50 ل 50 
    #يعني بنقسم العرض على 2 بعدها ناخد من السالب للموجب دا اللي عملناه 
    #خد بالك ان دي الشاشة المصغرة مش المكبرة
    x = random.randint(-width//2, width//2)  

    #عملنا مع الطول نفس العرض 
    #تخيل خط اعداد طوله 10 هتقسمه 5 قيم موجبة و 5 قيم سالبة فهيبقا من -5 ل 5 
    y = random.randint(-80, height//2)
    
    size = random.randint(5, 25) #حجم النجمة هيبقا عشوائي من 5 ل 25 
    
    star.penup()
    star.goto(x, y)
    star.pendown()

    # Draw the star
    star.begin_fill()
    for i in range(5):
        star.forward(size)
        star.right(144)
    star.end_fill()


home.color("black")

#drawing the squared body  رسم شكل البيت المربع
home.fillcolor("brown")  #لونه النهائي بعد ما نقفل الشكل هيكون بني 
home.begin_fill() #بداية الشكل اللي هنلونه
for i in range(4):
    home.fd(100)    #fd = forward
    home.rt(90)     #rt = right
home.end_fill() #نهاية الشكل اللي هنلونه

#drawing the triangular ceiling
home.fillcolor("red") 
home.begin_fill() 
for i in range(3):
    home.fd(100)    #fd = forward (100 is a length) 
    home.lt(120)     #lt = left  (120 is an angle)
home.end_fill() 

#drawing the circular windows
home.fillcolor("white") 

home.begin_fill() 
home.penup()
home.goto(70,-25)
home.pendown()
home.circle(10)
home.end_fill() 

home.begin_fill() 
home.penup()
home.goto(25,-25)
home.pendown()
home.circle(10)
home.end_fill() 

#رسم الباب
home.fillcolor("yellow")   #لون الباب أصفر
home.begin_fill()
home.penup()
home.goto(25,-100)
home.pendown()
home.goto(25,-40)
home.goto(75,-40)
home.goto(75,-100)
home.goto(25,-100)
home.end_fill()

#رسم الارض
home.fillcolor("dark green")
home.begin_fill()
home.penup()
home.goto(-width,-100)
home.pendown()
home.goto(width,-100)
home.goto(width,-height)
home.goto(-width,-height)
home.goto(-width,-100)
home.end_fill()

#اضافة كتابة
home.color("white")
home.penup()
home.goto(-25,-130)
home.pendown()


home.write("As you see I am a house. NOT A CHICKEN \n I could be a chicken house though")



star.hideturtle()
home.hideturtle()


turtle.done()
