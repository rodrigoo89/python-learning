from pathlib import Path

# la ruta ahora sí incluye la unidad de disco (C:), tal como aparece en tu terminal
carpeta = Path("C:\\Users\\u607268\\OneDrive - Telecom Argentina SA\\Desktop\\Python\\dia6\\dia6.txt")


#Ejemplo de uso de los métodos y atributos de Path
print(carpeta.suffix)  # .txt
print(carpeta.name)   # dia6.txt
print(carpeta.parent) # C:\Users\u607268\OneDrive - Telecom Argentina SA\Desktop\Python\dia6
print(carpeta.stem)   # dia6
print(carpeta.exists()) # True
print(carpeta.is_file()) # True
print(carpeta.is_dir())  # False