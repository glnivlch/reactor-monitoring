from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
import main


def save_measurement() -> None:
    name = name_input.text()

    label_status2.clear()
    label_status3.clear()
    label_status4.clear()

    try:
        temperature = temperature_input.text()
        temperature = float(temperature)
        pressure = pressure_input.text()
        pressure = float(pressure)
    except ValueError:
        label_status1.setText("Ошибка! Введите корректные числовые значения!")
        return

    # сохранение параметров в историю измерений
    temperature_status, pressure_status = main.add_measurement(temperature, pressure)

    temperature_input.clear()
    pressure_input.clear()

    label_status1.setText("Измерение сохранено.")
    if temperature_status == "normal" and pressure_status == "normal":
        label_status2.setText("Реактор работает в штатном режиме! Продолжайте мониторинг.")
    else:
        label_status2.setText("Внимание! Обнаружены отклонения от нормального режима!")

        if temperature_status == "high":
            label_status3.setText("Температура реактора превышает норму! Необходимо понизить температуру.")
        elif temperature_status == "low":
            label_status3.setText("Температура реактора ниже нормы! Необходимо повысить температуру.")

        if pressure_status == "high":
            label_status4.setText("Давление реактора превышает норму! Необходимо понизить давление.")
        elif pressure_status == "low":
            label_status4.setText("Давление реактора ниже нормы! Необходимо повысить давление.")


def show_history() -> None:
    history_table.setRowCount(len(main.history))
    history_window.show()

    for number, measurement_saved in enumerate(main.history):
        number_item = QTableWidgetItem(str(number + 1))
        history_table.setItem(number, 0, number_item)

        date = measurement_saved[0].strftime("%d.%m.%Y %H:%M:%S")
        date_item = QTableWidgetItem(date)
        history_table.setItem(number, 1, date_item)


        temperature_item = QTableWidgetItem(str(measurement_saved[1]))
        history_table.setItem(number, 2, temperature_item)

        pressure_item = QTableWidgetItem(str(measurement_saved[2]))
        history_table.setItem(number, 3, pressure_item)

    if len(main.history) == 0:
        statistics_label.setText("Измерений на данный момент нет")
    else:
        statistics_label.setText("Статистика:")
        max_temperature, min_temperature, average_temperature, max_pressure, min_pressure, average_pressure = main.statistics()
        max_temperature_label.setText(f"Максимальная температура: {max_temperature}°C")
        min_temperature_label.setText(f"Минимальная температура: {min_temperature}°C")
        average_temperature_label.setText(f"Средняя температура: {average_temperature}°C")
        max_pressure_label.setText(f"Максимальное давление: {max_pressure} бар")
        min_pressure_label.setText(f"Минимальное давление: {min_pressure} бар")
        average_pressure_label.setText(f"Среднее давление: {average_pressure} бар")


app = QApplication([])

# создание окна
window = QWidget()
window.setWindowTitle("Reactor Monitor")
window.resize(800, 600)

title_label = QLabel("Новое измерение", window)
title_label.move(30, 40)
title_label.setStyleSheet("font-size: 22px; font-weight: bold; color: #2563EB")

# ввод имени
label_name = QLabel("Введите свое имя", window)
label_name.move(30, 80)

name_input = QLineEdit(window)
name_input.move(30, 100)
name_input.setPlaceholderText("Имя оператора")
name_input.resize(250, 30)

# ввод параметров реактора
label_temperature = QLabel("Введите температуру реактора,°C", window)
label_temperature.move(30, 140)
temperature_input = QLineEdit(window)
temperature_input.move(30, 160)

label_pressure = QLabel("Введите давление реактора, бар", window)
label_pressure.move(30, 200)
pressure_input = QLineEdit(window)
pressure_input.move(30, 220)

# кнопка сохранить
save_button = QPushButton("Сохранить", window)
save_button.move(30, 270)
save_button.resize(80, 30)

save_button.setStyleSheet("""
    QPushButton {
        background-color: #2563EB;
        color: white;
        border-radius: 8px;
    }
    QPushButton:hover {
        background-color: #1D4ED8;
    }
    QPushButton:pressed {
        background-color: #1E40AF;
    }
""")

save_button.clicked.connect(save_measurement)

# ответ после ввода параметров
label_status1 = QLabel("", window)
label_status1.move(30, 320)
label_status1.resize(720, 30)

label_status2 = QLabel("", window)
label_status2.move(30, 360)
label_status2.resize(720, 30)

label_status3 = QLabel("", window)
label_status3.move(30, 400)
label_status3.resize(720, 30)

label_status4 = QLabel("", window)
label_status4.move(30, 440)
label_status4.resize(720, 30)

# кнопка история измерений
history_button = QPushButton("История измерений", window)
history_button.move(30, 510)
history_button.resize(160, 35)
history_button.setStyleSheet(save_button.styleSheet())

# окно истории измерений
history_window = QWidget()
history_window.setWindowTitle("История измерений")
history_window.resize(700, 500)
history_button.clicked.connect(show_history)

# таблица с историей
history_table = QTableWidget(0, 4, history_window)
history_table.setHorizontalHeaderLabels(["№", "Дата и время", "Температура,°C", "Давление, бар"])
history_table.move(20, 20)
history_table.resize(660, 330)

history_table.setColumnWidth(0, 60)
history_table.setColumnWidth(1, 220)
history_table.setColumnWidth(2, 170)
history_table.setColumnWidth(3, 170)

history_table.verticalHeader().hide()

# статистика параметров
statistics_label = QLabel("", history_window)
statistics_label.move(20, 370)
statistics_label.resize(650, 30)

max_temperature_label = QLabel("", history_window)
max_temperature_label.move(20, 405)
max_temperature_label.resize(650, 30)

min_temperature_label = QLabel("", history_window)
min_temperature_label.move(20, 425)
min_temperature_label.resize(650, 30)

average_temperature_label = QLabel("", history_window)
average_temperature_label.move(20, 445)
average_temperature_label.resize(650, 30)

max_pressure_label = QLabel("", history_window)
max_pressure_label.move(350, 405)
max_pressure_label.resize(650, 30)

min_pressure_label = QLabel("", history_window)
min_pressure_label.move(350, 425)
min_pressure_label.resize(650, 30)

average_pressure_label = QLabel("", history_window)
average_pressure_label.move(350, 445)
average_pressure_label.resize(650, 30)

exit_button = QPushButton("Выход", window)
exit_button.move(210, 510)
exit_button.resize(100, 35)

exit_button.setStyleSheet("""
    QPushButton {
        background-color: #DC2626;
        color: white;
        border-radius: 8px;
    }
    QPushButton:hover {
        background-color: #B91C1C;
    }
    QPushButton:pressed {
        background-color: #991B1B;
    }
""")

exit_button.clicked.connect(app.quit)

window.show()  # вызываем окно

app.exec()