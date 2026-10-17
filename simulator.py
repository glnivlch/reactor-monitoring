import random

generate_temperature = 0.0
generate_pressure = 1.0

def heat_reactor(
        generate_temperature: float,
        generate_pressure: float
) -> tuple[float, float]:
    if generate_temperature < 85:
        generate_difference_temperature = random.uniform(0.50, 1.20)
        generate_temperature += generate_difference_temperature

    if generate_temperature >= 85:
        generate_temperature = 85

    if generate_pressure < 3:
        generate_difference_pressure = random.uniform(0.005, 0.01)
        generate_pressure += generate_difference_pressure

    if generate_pressure >= 3:
        generate_pressure = 3

    return (round(generate_temperature, 1), round(generate_pressure, 2))


def maintain_reactor(
        generate_temperature: float,
        generate_pressure: float
) -> tuple[float, float]:
    if 82 <= generate_temperature <= 88:
        generate_difference_temperature = random.uniform(-0.2, 0.2)
    elif generate_temperature < 82:
        generate_difference_temperature = random.uniform(0.05, 0.2)
    else:
        generate_difference_temperature = random.uniform(-0.2, -0.05)
    generate_temperature += generate_difference_temperature

    if 2.7 <= generate_pressure <= 3.3:
        generate_difference_pressure = random.uniform(-0.03, 0.03)
    elif generate_pressure < 2.7:
        generate_difference_pressure = random.uniform(0.01, 0.05)
    else:
        generate_difference_pressure = random.uniform(-0.05, -0.01)
    generate_pressure += generate_difference_pressure

    return (round(generate_temperature, 1), round(generate_pressure, 2))


mode = "heating"
for _ in range(400):
    if generate_temperature >= 85 and generate_pressure < 3:
        mode = "waiting_gas"
    elif generate_temperature >= 85 and generate_pressure >= 3:
        mode = "maintain"

    if mode == "heating":
        generate_temperature, generate_pressure = heat_reactor(generate_temperature, generate_pressure)
    elif mode == "waiting_gas":
        generate_temperature, generate_pressure = waiting_gas(generate_temperature, generate_pressure)
    elif mode == "maintain":
        generate_temperature, generate_pressure = maintain_reactor(generate_temperature, generate_pressure)

    print(generate_temperature, generate_pressure)