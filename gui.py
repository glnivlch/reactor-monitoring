from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton


def save_measurement() -> None:
    name = name_input.text()

    try:
        temperature = temperature_input.text()
        temperature = float(temperature)
        pressure = pressure_input.text()
        pressure = float(pressure)
    except ValueError:
        label_status.setText("Ошибка! Введите корректные числовые значения!")
        return

    temperature_input.clear()
    pressure_input.clear()

    label_status.setText("Измерение сохранено.")
    print(f"Температура реактора: {temperature}°C, давление реактора: {pressure} бар.")


app = QApplication([])

# создание окна
window = QWidget()
window.setWindowTitle("Reactor Monitor")
window.resize(800, 600)

title_label = QLabel("Новое измерение", window)
title_label.move(30, 40)

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
save_button.clicked.connect(save_measurement)

# ответ после ввода параметров
label_status = QLabel("", window)
label_status.move(30, 320)
label_status.resize(400, 30)


window.show()  # вызываем окно

app.exec()