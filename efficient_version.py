import time

def char_to_bit(c):
    """
    Convierte un carácter en su correspondiente bit en una máscara de bits.

    Parámetros:
    c (str): Un carácter que puede ser una letra (A-Z) o un dígito numérico (0-9).

    Retorna:
    int: Un entero que representa el bit correspondiente al carácter.
    """
    return 1 << (ord(c) - ord('A') if 'A' <= c <= 'Z' else ord(c) - ord('0') + 26)

def set_to_bitmask(s):
    """
    Convierte un conjunto de caracteres en una máscara de bits.

    Parámetros:
    s (str): Una cadena de caracteres que contiene letras (A-Z) y/o dígitos (0-9).

    Retorna:
    int: Un entero que representa la máscara de bits del conjunto de caracteres.
    """
    return sum(char_to_bit(c) for c in s)

universe = set_to_bitmask("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

def menu():
    """
    Muestra el menú principal para que el usuario construya conjuntos, realice operaciones entre ellos o finalice el programa.
    """
    conjuntos = {}
    while True:
        print("\nMenú Principal")
        print("1. Construir conjuntos")
        print("2. Operar conjuntos")
        print("3. Finalizar")
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            construir_conjuntos(conjuntos)
        elif opcion == "2":
            subMenu(conjuntos)
        elif opcion == "3":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

def mostrar_resultado(conjuntos, bitmask, operacion):
    """
    Muestra el resultado de una operación en notación de conjuntos.

    Parámetros:
    conjuntos (dict): Un diccionario con los nombres de los conjuntos como claves y sus máscaras de bits como valores.
    bitmask (int): La máscara de bits resultante de la operación realizada.
    operacion (str): El nombre de la operación realizada, como "Unión" o "Intersección".
    """
    result_chars = bitmask_to_set(bitmask)
    formatted_result = format_as_set_notation(result_chars)
    for set_name, bitmask in conjuntos.items():
        print(f"{set_name}: {format_as_set_notation(bitmask_to_set(bitmask))}")
    print(f'Resultado de {operacion.lower()}: {formatted_result}')
    time.sleep(2)

def subMenu(conjuntos):
    """
    Muestra un submenú para elegir una operación a realizar entre los conjuntos creados.

    Parámetros:
    conjuntos (dict): Un diccionario con los nombres de los conjuntos como claves y sus máscaras de bits como valores.
    """
    while True:
        print("\nElige qué operación hacer con los conjuntos ingresados:")
        print("1. Complemento")
        print("2. Unión")
        print("3. Intersección")
        print("4. Diferencia")
        print("5. Diferencia Simétrica")
        print("6. Finalizar")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            union_bitmask = 0
            for bitmask in conjuntos.values():
                union_bitmask |= bitmask
            complement_union = universe & ~union_bitmask

            mostrar_resultado(conjuntos=conjuntos, bitmask=complement_union, operacion="Complemento")
        elif opcion == "2":
            union_bitmask = 0
            for bitmask in conjuntos.values():
                union_bitmask |= bitmask

            mostrar_resultado(conjuntos=conjuntos, bitmask=union_bitmask, operacion="Unión")
        elif opcion == "3":
            intersection_bitmask = None
            for bitmask in conjuntos.values():
                if intersection_bitmask is None:
                    intersection_bitmask = bitmask
                else:
                    intersection_bitmask &= bitmask

            mostrar_resultado(conjuntos=conjuntos, bitmask=intersection_bitmask, operacion="Intersección")
        elif opcion == "4":
            difference_bitmask = None
            for bitmask in conjuntos.values():
                if difference_bitmask is None:
                    difference_bitmask = bitmask
                else:
                    difference_bitmask &= ~bitmask

            mostrar_resultado(conjuntos=conjuntos, bitmask=difference_bitmask, operacion="Diferencia")
        elif opcion == "5":
            symmetric_difference_bitmask = 0
            for bitmask in conjuntos.values():
                symmetric_difference_bitmask ^= bitmask

            mostrar_resultado(conjuntos=conjuntos, bitmask=symmetric_difference_bitmask, operacion="Diferencia Simétrica")
        elif opcion == "6":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

def construir_conjuntos(conjuntos):
    """
    Permite al usuario crear un conjunto y almacenarlo en el diccionario de conjuntos.

    Parámetros:
    conjuntos (dict): Un diccionario con los nombres de los conjuntos como claves y sus máscaras de bits como valores.
    """
    nombre = input("Nombre del conjunto: ")
    elementos = input("Ingresa los elementos separados por comas (A-Z, 0-9): ").upper().replace(" ", "")
    validos = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    elementos_filtrados = [e for e in elementos.split(',') if e in validos]
    if len(elementos_filtrados) < len(elementos.split(',')):
        print("Algunos elementos ingresados no son válidos y han sido excluidos. Vuelve a crear el conjunto.")
        return
    
    conjunto = ''.join(sorted(set(elementos_filtrados)))
    conjuntos[nombre] = set_to_bitmask(conjunto)
    print(f"Conjunto {nombre} creado: {format_as_set_notation(conjunto)}")

def format_as_set_notation(char_set):
    """
    Formatea un conjunto de caracteres en notación de conjunto.

    Parámetros:
    char_set (str): Una cadena que representa un conjunto de caracteres.

    Retorna:
    str: La representación del conjunto en notación de conjunto, e.g., "{A, B, C}".
    """
    return "{" + ", ".join(sorted(char_set)) + "}"

def bitmask_to_set(bitmask):
    """
    Convierte una máscara de bits en un conjunto de caracteres.

    Parámetros:
    bitmask (int): Un entero que representa una máscara de bits.

    Retorna:
    str: Una cadena que contiene los caracteres representados en la máscara de bits.
    """
    chars = [chr(i + ord('A')) if i < 26 else chr(i - 26 + ord('0')) for i in range(36) if bitmask & (1 << i)]
    return ''.join(chars)

# Ejecutar el programa
menu()
