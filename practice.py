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