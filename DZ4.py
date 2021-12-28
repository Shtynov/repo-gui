number = int(input("Введите целое положительное число: "))
save = 0
num = number
while num > 0:
    new = num % 10
    if new > save:
        save = new
        if number == 9:
            break
    num = num // 10
print(f'Наибольшая цифра в числе {number} равна {save}')
