import random
import main

generate_temperature = 0.0
generate_pressure = 0.0


def generate_measurement(generate_temperature: float, generate_pressure: float) -> tuple[float, float]:
    if generate_temperature < main.TEMPERATURE_MIN:
        generate_difference_temperature = random.uniform(0.10, 0.50)
    else:
        generate_difference_temperature = random.uniform(-0.20, 0.20)
    generate_temperature += generate_difference_temperature

    if generate_pressure < main.PRESSURE_MIN:
        generate_difference_pressure = random.uniform(0.01, 0.05)
    else:
        generate_difference_pressure = random.uniform(-0.20, 0.20)
    generate_pressure += generate_difference_pressure

    return (round(generate_temperature, 2), round(generate_pressure, 2))

for _ in range(50):
    generate_temperature, generate_pressure = generate_measurement(generate_temperature, generate_pressure)
    print(generate_temperature, generate_pressure)