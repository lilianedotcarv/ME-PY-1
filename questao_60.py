def fahrenheitParaCelsius(f=100.0):
    celsius = (5 / 9) * (f - 32)
    print(f"{f:.1f}°F equivale a {celsius:.2f}°C")
    return celsius
