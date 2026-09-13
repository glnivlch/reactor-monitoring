def parameter_input(message: str) -> float:
    while True:
        try:
            parameter = float(input(message))
            return parameter
        except ValueError:
            print("Введите корректное значение через точку. Например, 00.0")