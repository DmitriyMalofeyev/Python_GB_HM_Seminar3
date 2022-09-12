# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.(Доп)

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]


n = int(input("Введите число n: "))


def fib(n):
    if n in [1,2]:
        return 1
    else:
        return fib(n-1)+fib(n-2)

list=[0]

for e in range(1,9):
    list.append(fib(e))
    if not e%2:
        list.insert(0,list[-1]*(-1))
    else:
        list.insert(0,list[-1])
    
print(list)