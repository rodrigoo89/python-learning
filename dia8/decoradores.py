def decorar_saludo(funcion):
    def otra_funcion(palabra):
        print("hola")
        funcion(palabra)
        print("Adios")
        
    return otra_funcion
 
 
  
def mayuscula(texto):
    print(texto.upper())

def minuscula(texto):
    print(texto.lower())


mayuscula_decorada= decorar_saludo(mayuscula)
minuscula_decorada= decorar_saludo(minuscula)

mayuscula_decorada("Python")
minuscula_decorada("HDNASUASD")
    
    
    
    
