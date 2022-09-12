# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

print("Введите числа через пробел: ")
numbers = [int (i) for i in input().split()]

j = -1
for i in range (len(numbers)):
    if len(numbers)%2 != 0 and i <= len(numbers)/2:
        print(numbers[i] * numbers[j])
        j -= 1
    elif len(numbers)%2 == 0 and (i + 1) <= len(numbers)/2:
        print(numbers[i] * numbers[j])
        j -= 1

