#To create an input لانشاء دخل 
n = input("Enter an input: ")
print(type(n))

#To make the input type integer لجعل نوع الدخل رقم صحيح
x = int(input("Enter an integer: "))
print(type(x))

#to enter a list لادخال قائمة 
input_string = input("Enter elements separated by spaces: ")
print(input_string)
user_list = input_string.split()
print(user_list)

#converting each element in the list into integer 
#تحويل كل عنصر من عناصر القائمة إلى رقم صحيح 
user_list = [int(x) for x in user_list] 

print(user_list)


