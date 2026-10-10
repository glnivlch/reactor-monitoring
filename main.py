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
    parameter: float,
    lower_limit: float,
    upper_limit: float
) -> str:
    if lower_limit <= parameter <= upper_limit:
        return "normal"
    elif parameter > upper_limit:
        return "high"
    else:
        return "low"


# Расчет статистики параметров
def statistics() -> tuple[float, float, float, float, float, float]:
    # Фиксация первых измерений, как экстремумов
    max_temperature = history[0][1]
    min_temperature = history[0][1]
    max_pressure = history[0][2]
    min_pressure = history[0][2]

    total_temperature = 0
    total_pressure = 0

    # Поиск экстремумов параметров среди всех измерений
    for measurement_saved in history:
        if measurement_saved[1] > max_temperature:
            max_temperature = measurement_saved[1]
        if measurement_saved[1] < min_temperature:
            min_temperature = measurement_saved[1]

        if measurement_saved[2] > max_pressure:
            max_pressure = measurement_saved[2]
        if measurement_saved[2] < min_pressure:
            min_pressure = measurement_saved[2]

        total_temperature += measurement_saved[1]
        total_pressure += measurement_saved[2]

    average_temperature = total_temperature / len(history)
    average_pressure = total_pressure / len(history)

    return (max_temperature, min_temperature, average_temperature,
            max_pressure, min_pressure, average_pressure)


# Главная программа
history = []

def run_console() -> None:
    name_user = input("Введите Ваше имя: ")
    print(f"Добро пожаловать, {name_user}!")

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
        temperature_status = check_parameter(
            temperature,
            TEMPERATURE_MIN,
            TEMPERATURE_MAX
        )

        # Проверка оптимальности давления реактора
        pressure_status = check_parameter(
            pressure,
            PRESSURE_MIN,
            PRESSURE_MAX
        )

        if temperature_status == "normal" and pressure_status == "normal":
            print(f"Реактор работает в штатном режиме. Продолжайте следить за процессом, {name_user}.")
        else:
            if temperature_status == "high":
                print("Внимание! Температура реактора выше нормы. Охладите реактор")
            elif temperature_status == "low":
                print("Внимание! Температура реактора ниже нормы. Нагрейте реактор")

            if pressure_status == "high":
                print("Внимание! Давление реактора выше нормы. Понизьте давление реактора")
            elif pressure_status == "low":
                print("Внимание! Давление реактора ниже нормы. Повысьте давление реактора")

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

            for number, measurement_saved in enumerate(history, start=1):
                print(
                    f"{number:^5}"
                    f"{measurement_saved[0].strftime('%d.%m.%Y %H:%M:%S'):^40}"  # Дата и время
                    f"{measurement_saved[1]:^15}"  # Температура
                    f"{measurement_saved[2]:^15}"  # Давление
                )

            max_temperature, min_temperature, average_temperature, max_pressure, min_pressure, average_pressure = statistics()

            print(f"Максимальная температура за время мониторинга составила {max_temperature} градусов Цельсия.")
            print(f"Максимальное давление за время мониторинга составило {max_pressure} бар.")
            print(f"Минимальная температура за время мониторинга составила {min_temperature} градусов Цельсия.")
            print(f"Минимальное давление за время мониторинга составило {min_pressure} бар.")
            print(f"Средняя температура составила {average_temperature} градусов Цельсия.")
            print(f"Среднее давление составило {average_pressure} бар.")
            print(f"Мониторинг завершен. До свидания, {name_user}!")
            break

        time.sleep(5)


if __name__ == "__main__":
    run_console()