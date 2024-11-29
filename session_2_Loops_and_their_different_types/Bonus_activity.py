# Create a program that would receive a two dimensional matrix as one row at a time 
# and print their accumulative summation after each row, and the final accumulative summation.
# قم بإنشاء برنامج يستقبل مصفوفة ثنائية الأبعاد حيث يقوم باستقبال صف واحد في المرة 
# وطباعة المجموع التراكمي لكل صف والمجموع التراكمي النهائي

n = int(input("To enter a matrix (n x m) please enter n: ")) #number of rows عدد الصفوف
m = int(input("Please enter m: ")) #number of columns عدد الأعمدة
matrix = []
accumulative_sum = []  #accumulative summation  المجموع التراكمي بعد كل صف
sum_row = 0  #مجموع الصف لحساب المجموع التراكمي 
for i in range(n):
    row = input(f"Enter row {i+1} as integers separated with white spaces: ").split()
    row = [int(x) for x in row]
    while len(row) < m:   #اذا كان عدد الارقام المدخلة اصغر من عدد الاعمدة 
        row.append(0)   #نقوم باضافة اصفار
    if len(row) > m:  #اذا كان عدد الارقام المدخلة اكبر من عدد الاعمدة
        row = row[:m]  #نأخذ اول ارقام حتى يتطابق العدد مع عدد الاعمدة
    matrix.append(row) #نضيف الصف إلى المصفوفة لنظهرها فيما بعد
    sum_row += sum(row)  #نقوم بحساب المجموع التراكمي بعد كل صف
    accumulative_sum.append(sum_row) #نضيف المجاميع التراكمية غلى قائمة لنعرضها لاحقا 
print(matrix) #نطبع المصفوفة التي قمنا بادخالها
for row_num in range(1, n+1):
    print(f"Accumulative summation after row {row_num} is : {accumulative_sum[row_num - 1]} ")
print( f"the final accumulative summation is {accumulative_sum[-1]}")
