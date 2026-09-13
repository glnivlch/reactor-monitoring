# Библиотеки
import time
from datetime import datetime

# Константы
TEMPERATURE_MIN = 70.0
TEMPERATURE_MAX = 90.0
PRESSURE_MIN = 2.0
PRESSURE_MAX = 5.0


# Функции
# Ввод числового параметра
def parameter_input(message: str) -> float:
    while True:
        try:
            parameter = float(input(message))
            return parameter
        except ValueError:
            print("Введите корректное значение через точку. Например, 85.5")


# Проверка параметра на допустимый диапазон
def check_parameter(
    parameter_name: str,
    parameter: float,
    lower_limit: float,
    upper_limit: float
) -> bool:
    if lower_limit <= parameter <= upper_limit:
        print(f"Параметр '{parameter_name}' в норме, продолжайте работу.")
        return True
    elif parameter > upper_limit:
        print(f"Параметр '{parameter_name}' выше нормы, понизьте параметр!")
        return False
    else:
        print(f"Параметр '{parameter_name}' ниже нормы, повысьте данный параметр!")
        return False


name_user = input("Введите Ваше имя: ")
print(f"Добро пожаловать, {name_user}!")
history = []

while True:
    temperature = parameter_input("Введите значение температуры реактора в градусах Цельсия: ")

    # добавить фичу с переводом ед. изм. давления
    pressure = parameter_input("Введите значение давления реактора в бар: ")

    measurement_time = datetime.now()
    print(f"Дата и время замера: {measurement_time.strftime('%d.%m.%Y %H:%M:%S')}")

    # Создание кортежа с данными параметров, сохранение его в историю измерений
    measurement = (measurement_time, temperature, pressure)
    history.append(measurement)

    # Проверка оптимальности температуры реактора
    is_temperature_normal = check_parameter(
        "Температура реактора",
        temperature,
        TEMPERATURE_MIN,
        TEMPERATURE_MAX
    )

    # Проверка оптимальности давления реактора
    is_pressure_normal = check_parameter(
        "Давление реактора",
        pressure,
        PRESSURE_MIN,
        PRESSURE_MAX
    )

    if is_temperature_normal and is_pressure_normal:
        print(f"Реактор работает в штатном режиме. Продолжайте следить за процессом, {name_user}.")
    else:
        print("Внимание! Параметры реактора требуют проверки.")

    print("Хотите продолжить мониторинг? Введите 'да' или 'нет'.")
    program_termination = False
    while True:
        answer = input().strip().lower()
        if answer == "нет":
            program_termination = True
            break
        elif answer == "да":
            break
        else:
            print("Введите строго 'да' или 'нет'.")

    if program_termination:
        print(f"Мониторинг завершен. До свидания, {name_user}!")
        break

    time.sleep(5)