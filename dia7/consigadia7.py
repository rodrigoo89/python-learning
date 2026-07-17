class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self,nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance
    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido}\nNúmero de cuenta: {self.numero_cuenta}\nBalance: {self.balance}"



def main():
    cliente1 = input("Ingrese el nombre del cliente: ")
    apellido1 = input("Ingrese el apellido del cliente: ")
    numero_cuenta1 = input("Ingrese el número de cuenta: ")
    balance1 = float(input("Ingrese el balance inicial: "))
    cliente1 = crear_cliente(cliente1, apellido1, numero_cuenta1, balance1)
    while True:
        print(cliente1)  # mostramos el estado actual en cada vuelta
        opcion = input("¿Qué querés hacer? (depositar/retirar/salir): ")
        
        if opcion == "depositar":
            monto = float(input("¿Cuánto querés depositar? "))
            depositar(cliente1, monto)
        elif opcion == "retirar":
            monto = float(input("¿Cuánto querés retirar? "))
            retirar(cliente1, monto)
        elif opcion == "salir":
            break



def crear_cliente(nombre, apellido, numero_cuenta, balance):
    return Cliente(nombre, apellido, numero_cuenta, balance)

def depositar(cliente, cantidad):
    cliente.balance += cantidad
    print(f"Se han depositado {cantidad}. Nuevo balance: {cliente.balance}")
def retirar(cliente, cantidad):
    if cantidad <= cliente.balance:
        cliente.balance -= cantidad
        print(f"Se han retirado {cantidad}. Nuevo balance: {cliente.balance}")
    else:
        print("Fondos insuficientes para retirar.")

        
main()
