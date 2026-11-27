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