# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

print("Введите числа через пробел: ")
numbers = [float(i) for i in input().split()]

def calculon(listNum):

    listDouble=[]

    for x in listNum:
        # Если дробной части нет то пропускаем
        if x%1:
            listDouble.append(round(x%1,2))
    listDouble.sort()

    print(listDouble[-1]-listDouble[0])

calculon(numbers)


