def statistics() -> tuple[float, float, float, float, float, float]:
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