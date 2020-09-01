# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

n = int(input('Укажите целое положительное число = '))

maxdigit = 0

while True:
    digit = n % 10
    if digit > maxdigit:
        maxdigit = digit
    n = n // 10
    if n == 0:
        break

print(maxdigit)