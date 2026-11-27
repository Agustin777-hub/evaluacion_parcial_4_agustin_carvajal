def validar_titulo(titulo):
    return titulo.strip() != ""

def validar_copias(copias_texto):
    return copias_texto.isdecimal()

def validar_prestamo(prestamo_texto):
    return prestamo_texto.isdecimal() and int(prestamo_texto) > 0

def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========\n1. Agregar libro\n2. Buscar libro\n3. Eliminar libro\n4. Actualizar disponibilidad\n5. Mostrar libros\n6. Salir\n" + "=" * 36)

def leer_opcion():
    opcion_texto = input("Seleccione una opción: ")
    while not (opcion_texto.isdecimal() and 1 <= int(opcion_texto) <= 6):
        opcion_texto = input("Opción inválida. Ingrese un número entero entre 1 y 6: ")
    return int(opcion_texto)

def agregar_libro(lista_libros):
    titulo = input("Ingrese el título: ")
    copias_texto = input("Ingrese las copias: ")
    prestamo_texto = input("Ingrese el período de préstamo (días): ")
    if validar_titulo(titulo) and validar_copias(copias_texto) and validar_prestamo(prestamo_texto):
        lista_libros.append({"titulo": titulo, "copias": int(copias_texto), "prestamo": int(prestamo_texto), "disponible": False})
        print("Libro agregado correctamente.")
    else:
        print("Datos inválidos: el título no puede estar vacío, las copias deben ser un entero >= 0 y el préstamo un entero > 0. Libro no registrado.")

def buscar_libro(lista_libros, titulo):
    for posicion in range(len(lista_libros)):
        if lista_libros[posicion]["titulo"] == titulo:
            return posicion
    return -1

def eliminar_libro(lista_libros):
    titulo = input("Ingrese el título del libro a eliminar: ")
    posicion = buscar_libro(lista_libros, titulo)
    if posicion != -1:
        lista_libros.pop(posicion)
        print("Libro eliminado correctamente.")
    else:
        print(f"El libro '{titulo}' no se encuentra registrado.")