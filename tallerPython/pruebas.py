import random

tiradas = 0
resultado = 0

while resultado != 6:
    resultado = random.randint(1, 6)
    tiradas += 1
    print(f"Tirada {tiradas}: {resultado}")

print(f"¡Se obtuvo un 6 después de {tiradas} tiradas!")