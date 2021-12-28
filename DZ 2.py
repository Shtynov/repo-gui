second = int(input("Введите время в  секундах: "))
hours = second // 3600
minutes = (second // 60) % 60
second2 = second % 60
print(f'Точное время: {hours:=02}:{minutes:=02}:{second2:=02}')
