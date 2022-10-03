# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

num = int(input('Введите число больше 2: '))
list1 = [0, 1]
list2 = []
list3 = []
for i in range(2, num+1):
    list1.append(list1[i-2]+list1[i-1])
for i in range(1, len(list1)):
    list2.append(-list1[i])
list2.reverse()
list3 = list2 + list1
print(list3)