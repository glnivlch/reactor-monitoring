from main import history, measurement

if program_termination:
    print(f"{'История измерений':-^70}")  # 70 символов, таблица будет на 30, 20 и 20 символов
    print(f"{'Дата и время замера реактора':^30}{'Температура':^20}{'Давление':^20}")
    for measurement_saved in history:
        print(f"{measurement_saved[0].strftime('%d.%m.%Y %H:%M:%S'):^30}{measurement_saved[1]:^20}{measurement_saved[2]:^20}")
    print(f"Мониторинг завершен. До свидания, {name_user}!")
    break