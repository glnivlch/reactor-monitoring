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

    # История измерений и статистика при завершении мониторинга
    if program_termination:
        print(f"{'История измерений':-^75}")
        print(f"{'№':^5}{'Дата и время замера реактора':^40}{'Температура':^15}{'Давление':^15}")

        # Фиксация первых измерений, как экстремумов
        max_temperature = history[0][1]
        max_pressure = history[0][2]
        min_temperature = history[0][1]
        min_pressure = history[0][2]

        for number, measurement_saved in enumerate(history, start=1):
            print(
                f"{number:^5}"
                f"{measurement_saved[0].strftime('%d.%m.%Y %H:%M:%S'):^40}"  # Дата и время
                f"{measurement_saved[1]:^15}"  # Температура
                f"{measurement_saved[2]:^15}"  # Давление
            )
            # Поиск экстремумов температуры среди всех измерений
            if measurement_saved[1] > max_temperature:
                max_temperature = measurement_saved[1]
            if measurement_saved[1] < min_temperature:
                min_temperature = measurement_saved[1]

            # Поиск экстремумов давления среди всех измерений
            if measurement_saved[2] > max_pressure:
                max_pressure = measurement_saved[2]
            if measurement_saved[2] < min_pressure:
                min_pressure = measurement_saved[2]

        print(f"Максимальная температура за время мониторинга составила {max_temperature} градусов Цельсия.")
        print(f"Максимальное давление за время мониторинга составило {max_pressure} бар.")
        print(f"Минимальная температура за время мониторинга составила {min_temperature} градусов Цельсия.")
        print(f"Минимальное давление за время мониторинга составило {min_pressure} бар.")
        print(f"Мониторинг завершен. До свидания, {name_user}!")
        break

    time.sleep(5)