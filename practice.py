from main import history, measurement

for measurement in history:
    print(f"Дата и время замера реактора: {measurement[0].strftime('%d.%m.%Y %H:%M:%S')}.")
    print(f"Температура: {measurement[1]}.")
    print(f"Давление: {measurement[2]}.")