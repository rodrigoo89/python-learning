def al_cuadrado():
    numero = int(input("Ingrese un número: "))
    resultado = numero ** 2
    print(f"El cuadrado de {numero} es {resultado}.")
    print("gracias por usar el programa.")


  
  
try: #El codigo que puede generar un error va dentro del try
    al_cuadrado()

except ValueError: #el codigo que debe ejecutarse si falla 
    print("Error: Debe ingresar un número válido.")
    
else:# el codigo a ejecutar si no falla
    print("El programa se ejecutó correctamente.")

finally:
    print("Esto esto todo.")
    
#EJEMPLO1
def suma(num1, num2):
    try:
       
        resultado = num1 + num2
    except:
        
        print("Error inesperado")
    else:
        
        print(resultado)
        
        
def cociente(num1,num2):
    try:
        resultado = (num1/num2)

    except TypeError:
        print("Los argumentos a ingresar deben ser números")

    except ZeroDivisionError:
        print("El segundo argumento no debe ser cero")

    else:
        print(resultado)


def abrir_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo)
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except Exception:
        print("Error desconocido")
    else:
        print("Abriendo exitosamente")
    finally:
        print("Finalizando ejecución")
        

