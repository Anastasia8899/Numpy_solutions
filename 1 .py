
#Импортируйте библиотеку NumPy
#Создайте массив
import numpy as np
array=np.zeros(10)
print("An array of 10 zeros:")
print(array)
array=np.ones(10)
print("An array of 10 ones:")
print(array)
array=np.ones(10)*5
print("An array of 10 fives:")
print(array)

#Создать массив из целых чисел от 10 до 50
import numpy as np
array=np.arange(10,51)
print("Array of the integers from 10 to 50")
print(array)

#Создать массив из четных чисел от 10 до 50
import numpy as np
array=np.arange(10,51,2)
print("Array of all the even integers from 10 to 50")
print(array) 

#Создать матрицу 3х3 с числами от 0 до 8
matrix = np.arange(9).reshape(3,3)
print(matrix)

#Создать единичную матрицу 3x3
matrix = np.eye(3)
print(matrix)

#Используйте NumPy для генерации случайного числа от 0 до 1
a = np.random.random()
print(a)

#Используйте NumPy для генерации массива из 25 случайных чисел
a=np.random.randn(25)
print(a)

#Создайте следующую матрицу используя функции библиотеки NumPy
a= np. linspace (0,1,100)
print (a)

# это наша стартовая матрица
mat = np.arange(1,26).reshape(5,5)
print(mat)

mat = np.arange(1,26).reshape(5,5)
print(mat[2:5])

###Написать код обращения к элементу который вернет значение  20 из стартовой матрицы задачи l
mat = np.arange(1,26).reshape(5,5)
print(mat[3:4, 4:5])

#Написать код к стартовой матрице задачи l , который воспроизводит вывод, показанный ниже
mat = np.arange(1,26).reshape(5,5)
print(mat[0:3, 1:2])

#Написать код к стартовой матрице задачи l , который воспроизводит вывод, показанный ниже
mat = np.arange(1,26).reshape(5,5)
print(mat[4:5])
print(mat[3:5])

#Получить сумму всех значений в стартовой матрице mat
mat = np.arange(1,26).reshape(5,5)
np.sum([mat])

#Получить стандартное отклонение в стартовой матрице mat
np.std([mat])

import numpy as np
#Получить сумму значений в колонках в стартовой матрице mat
mat = np.arange(1,26).reshape(5,5)
print (mat)
print(mat.sum(axis=0))
