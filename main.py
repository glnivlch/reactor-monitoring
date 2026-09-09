name_user = input("Введите Ваше имя: ")
print(f"Добро пожаловать, {name_user}!")

temperature = float(input("Введите значение температуры реактора в градусах Цельсия: "))
pressure = float(input("Введите значение давления реактора в бар: "))  # добавить фичу с переводом ед. изм. давления

optimal_temperature = False
optimal_pressure = False

if 70 <= temperature <= 90:
    optimal_temperature = True
    print("Температура реактора в норме, продолжайте работать.")
elif temperature > 90:
    print("Температура реактора превысила норму, охладите реактор!")
else:
    print("Температура реактора низка, повысьте температуру!")

if 2 <= pressure <= 5:
    optimal_pressure = True
    print("Давление реактора в норме, продолжайте работать.")
elif pressure > 5:
    print("Давление реактора превысило норму, сбросьте давление!")
else:
    print("Давление реактора низко, необходимо повысить давление!")

if optimal_temperature and optimal_pressure:
    print(f"Реактор работает в штатном режиме. Продолжайте следить за процессом, {name_user}.")
else:
    print("Внимание! Параметры реактора требуют проверки.")