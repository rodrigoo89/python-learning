import re

def verificar_email(email):
  
    patron = r"@.+\.com(\.\w+)?$"


    busqueda = re.search(patron, email)

    
    if busqueda:
        print("Ok")
    else:
        print("La dirección de email es incorrecta")
        
        
def verificar_saludo(frase):
    patron = r"Hola"
    busqueda = re.search(patron, frase)
    if busqueda:
        print("Ok")
    else:
        print("No has saludado")