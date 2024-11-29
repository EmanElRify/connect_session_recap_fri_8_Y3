# Create 2 types of python loops قم بإنشاء نوعين من حلقات بايثون 
# Create 1  incremental value اجعل حلقة منهم تزايدية  
# Check on the change for the value of the variable in the two different loops and conclude the differences 
# افحص التغير في قيمة المتغير في كل حلقة واستنتج الفرق 


#for loop 
i = 0 #a value to increment 
for count in range(5):
    i += 2    #icremental value
    print(i)

#while loop 
i = 0
while i <= 8:
    i += 2
    print(i)
    
# Create python lists   أنشأ قائمة 
my_list = [10, 20, 30, 40, 50, 60]

# Loop over the list while printing the list’s elements      
# قم بالمرور على عناصر القائمة باستخدام الحلقة مع طباعة قيم العناصر  
for element in my_list:
    print(element)
    
# Apply changes to the list’s elements and print them once again                                         
# قم بعمل بعض التغييرات على عناصر القائمة ثم اطبعهم مجددا 

#1- mutation 
my_list = [10, 20, 30, 40, 50, 60]
my_list[0] = 11
my_list[-1] -= 1
for element in my_list:
    print(element)
print(my_list)

#2- applying the same changes on all elements
my_list = [10, 20, 30, 40, 50, 60]
for n in range(len(my_list)):
    my_list[n] += 1
    print(my_list[n])
print(my_list)

# Duplicate a Syntax error and fix it         انسخ خطأ وقم بتصحيحه 
# 1-	message = "Hello, world!"
#       print(mesage)

# 2-	for i in range(5):
#       print(i)

# 3-	message = 'Hello, world!"
message = "Hello, world!"
print(message)  #error in the variable name  الخطأ في اسم المتغير

for i in range(5):
      print(i)     #it was indentation error خطأ في المسافات 
      
message = "Hello, world!"   #error was caused by the different quotations; use ' or "
# الخطأ بسبب علامات التنصيص المختلفة 


# [Bonus] Add condition to print only even numbers inside the loops 
# قم بإضافة شرط لطباعة الأرقام الزوجية فقط في الحلقة 
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
for number in number_list:
    if number % 2 == 0:
        print(number)


      