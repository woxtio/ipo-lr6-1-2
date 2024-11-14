#Написать программу, которая:
#- Создает двумерную матрицу произвольного размера от 4 до 8 во высоте и ширине, заполненную значениями из списка **[-3, -5, -2, -12, 0, 15, 4, 7, 2]**
#- Выводит данную матрицу в форматированном виде. Пример:
#- Выводит сумму всех четных элементов
import random  #Импортируем random для генерации случайных чисел
znachenia = [-3, -5, -2, -12, 0, 15, 4, 7, 2] #Список значений для заполнения матрицы
height = int(input("Введите высоту матрицы: ")) #Bысота матрицы
width = int(input("Введите ширину матрицы: ")) #Ширина матрицы
if height < 4 or height > 8 or width < 4 or width > 8: #Проверка правиоьно ли введены размеры
    print("Высота и ширина должны быть от 4 до 8") #Вывод
else: #При правильных условиях
 matrica = [[random.choice(znachenia) for _ in range(width)] for _ in range(height)] #Создаем двумерную матрицу с указанными размерами, заполняя ее случайными значениями из списка znachenia
sum = 0 #Инициализируем переменную для хранения суммы четных элементов
for row in matrica: #Форматируем вывод каждой строки матрицы, выравнивая числа по правому краю
        print(" | ".join(f"{str(num):>3}" for num in row))  #Форматированный вывод
for a in matrica: #Проходим по всем элементам матрицы
    for b in a:
        if b%2==0: #Проверяем, является ли элемент четным
            sum+=b #Если четный, добавляем его к сумме
print("Сумма всех четных элементов:", sum) #Вывод суммы четных элементов
