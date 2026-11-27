def validar_titulo(titulo):
    return titulo.strip() != ""

def validar_copias(copias_texto):
    return copias_texto.isdecimal()

def validar_prestamo(prestamo_texto):
    return prestamo_texto.isdecimal() and int(prestamo_texto) > 0