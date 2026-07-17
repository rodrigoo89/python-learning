import numeros

turno_perfumeria = numeros.perfumeria()
turno_farmacia = numeros.farmacia()
turno_cosmeticos = numeros.cosmeticos()

def bienvenida():
    while True:
        opcion = input("Ingrese el área que desea atender (perfumeria/farmacia/cosmeticos/salir): ")
        
        if opcion == "farmacia":
            print(next(turno_farmacia))
        elif opcion == "perfumeria":
            print(next(turno_perfumeria))
        elif opcion == "cosmeticos":
            print(next(turno_cosmeticos))
        elif opcion == "salir":
            break

bienvenida()