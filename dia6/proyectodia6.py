from pathlib import Path
import os

# ---------------------------------------------------------
# CONFIGURACIÓN GENERAL
# ---------------------------------------------------------

# directorio apunta a la carpeta donde vive este script (afuera de Recetas)
directorio = Path(__file__).parent
carpeta_recetas = directorio / "Recetas"


# ---------------------------------------------------------
# FUNCIONES DE UTILIDAD
# ---------------------------------------------------------

def limpiar_pantalla():
    # 'cls' en Windows, 'clear' en Mac/Linux
    os.system("cls" if os.name == "nt" else "clear")


def contar_recetas():
    # Cuenta solo archivos (no carpetas), recorriendo todas las subcarpetas
    return len([
        archivo for archivo in carpeta_recetas.glob("**/*")
        if archivo.is_file()
    ])


def listar_categorias():
    # Devuelve una lista con los nombres de las subcarpetas (categorías)
    return [
        carpeta for carpeta in carpeta_recetas.iterdir()
        if carpeta.is_dir()
    ]


def elegir_categoria():
    # Muestra las categorías disponibles y devuelve la carpeta elegida
    categorias = listar_categorias()

    if not categorias:
        print("No hay categorías creadas todavía.")
        return None

    print("\nCategorías disponibles:")
    for i, categoria in enumerate(categorias, start=1):
        print(f"{i}. {categoria.name}")

    try:
        opcion = int(input("Elegí el número de categoría: "))
        # Restamos 1 porque enumerate empieza en 1 pero la lista en 0
        return categorias[opcion - 1]
    except (ValueError, IndexError):
        print("Opción inválida.")
        return None


def listar_recetas(categoria):
    # Devuelve una lista con los archivos (recetas) dentro de una categoría
    return [archivo for archivo in categoria.iterdir() if archivo.is_file()]


def elegir_receta(categoria):
    # Muestra las recetas de una categoría y devuelve el archivo elegido
    recetas = listar_recetas(categoria)

    if not recetas:
        print("No hay recetas en esta categoría.")
        return None

    print(f"\nRecetas en {categoria.name}:")
    for i, receta in enumerate(recetas, start=1):
        print(f"{i}. {receta.stem}")  # .stem = nombre sin extensión

    try:
        opcion = int(input("Elegí el número de receta: "))
        return recetas[opcion - 1]
    except (ValueError, IndexError):
        print("Opción inválida.")
        return None


# ---------------------------------------------------------
# OPCIONES DEL MENÚ
# ---------------------------------------------------------

def opcion_leer_receta():
    categoria = elegir_categoria()
    if categoria is None:
        return

    receta = elegir_receta(categoria)
    if receta is None:
        return

    print(f"\n--- {receta.stem} ---")
    print(receta.read_text(encoding="utf-8"))


def opcion_crear_receta():
    categoria = elegir_categoria()
    if categoria is None:
        return

    nombre = input("Nombre de la nueva receta: ")
    contenido = input("Escribí el contenido de la receta: ")

    nuevo_archivo = categoria / f"{nombre}.txt"
    nuevo_archivo.write_text(contenido, encoding="utf-8")

    print(f"Receta '{nombre}' creada en {categoria.name}.")


def opcion_crear_categoria():
    nombre = input("Nombre de la nueva categoría: ")
    nueva_carpeta = carpeta_recetas / nombre

    # exist_ok=False haría fallar si ya existe; lo controlamos a mano
    if nueva_carpeta.exists():
        print("Esa categoría ya existe.")
    else:
        nueva_carpeta.mkdir()
        print(f"Categoría '{nombre}' creada.")


def opcion_eliminar_receta():
    categoria = elegir_categoria()
    if categoria is None:
        return

    receta = elegir_receta(categoria)
    if receta is None:
        return

    receta.unlink()  # unlink() borra un archivo
    print(f"Receta '{receta.stem}' eliminada.")


def opcion_eliminar_categoria():
    categoria = elegir_categoria()
    if categoria is None:
        return

    # Antes de borrar la carpeta hay que vaciarla (rmdir falla si no está vacía)
    for archivo in categoria.iterdir():
        archivo.unlink()

    categoria.rmdir()
    print(f"Categoría '{categoria.name}' eliminada.")


# ---------------------------------------------------------
# MENÚ PRINCIPAL
# ---------------------------------------------------------

def mostrar_menu():
    print("""
1. Leer una receta
2. Crear una receta
3. Crear una categoría
4. Eliminar una receta
5. Eliminar una categoría
6. Salir
""")


def main():
    limpiar_pantalla()
    print("Hola, bienvenido al programa de recetas")
    print("Ruta de acceso:", carpeta_recetas)
    print("Número de recetas:", contar_recetas())

    while True:
        mostrar_menu()
        opcion = input("Elegí una opción (1-6): ")

        if opcion == "1":
            opcion_leer_receta()
        elif opcion == "2":
            opcion_crear_receta()
        elif opcion == "3":
            opcion_crear_categoria()
        elif opcion == "4":
            opcion_eliminar_receta()
        elif opcion == "5":
            opcion_eliminar_categoria()
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida, intentá de nuevo.")
            input("Presioná Enter para continuar...")
            limpiar_pantalla()
            continue

        input("\nPresioná Enter para volver al menú...")
        limpiar_pantalla()


if __name__ == "__main__":
    main()