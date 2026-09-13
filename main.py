# добавить фичу с переводом ед. изм. давления
def parameter_input(message: str) -> float:
    while True:
        try:
            parameter = float(input(message))
            return parameter
        except ValueError:
            print("Введите корректное значение через точку. Например, 85.5")


name_user = input("Введите Ваше имя: ")
print(f"Добро пожаловать, {name_user}!")

temperature = parameter_input("Введите значение температуры реактора в градусах Цельсия: ")
pressure = parameter_input("Введите значение давления реактора в бар: ")

is_temperature_normal = False
is_pressure_normal = False

# Проверка оптимальности температуры реактора
if 70 <= temperature <= 90:
    is_temperature_normal = True
    print("Температура реактора в норме, продолжайте работать.")
elif temperature > 90:
    print("Температура реактора превысила норму, охладите реактор!")
else:
    print("Температура реактора низка, повысьте температуру!")

# Проверка оптимальности давления реактора
if 2 <= pressure <= 5:
    is_pressure_normal = True
    print("Давление реактора в норме, продолжайте работать.")
elif pressure > 5:
    print("Давление реактора превысило норму, сбросьте давление!")
else:
    print("Давление реактора низко, необходимо повысить давление!")

if is_temperature_normal and is_pressure_normal:
    print(f"Реактор работает в штатном режиме. Продолжайте следить за процессом, {name_user}.")
else:
    print("Внимание! Параметры реактора требуют проверки.")