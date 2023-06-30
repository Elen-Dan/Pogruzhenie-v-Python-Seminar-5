'''
Создайте функцию генератор чисел Фибоначчи (см. Википедию).
'''

def num_fibo(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


x = int(input("Введите целое число: "))

for i in num_fibo(x):
    print(i)