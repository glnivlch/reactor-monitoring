while True:
    try:
        temperature = float(input("Введите значение температуры реактора в градусах Цельсия: "))
        break
    except ValueError:
        print("Введите корректное значение. Например, 00.0")

while True:
    try:
        pressure = float(input("Введите значение давления реактора в бар: "))
        break
    except ValueError:
        print("Введите корректное значение. Например, 00.0")