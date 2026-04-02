
nombre = input("¿Cuál es tu nombre?")
ventas = input("¿Cuánto vendiste?")

print(f"Hola {nombre}, cuanto vendiste? {ventas} ")
print(f"Las comision que te corresponde es {float(ventas)*13/100:.2f} pesos")