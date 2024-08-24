import time

def union(set1, set2):
    """
    Realiza la unión de dos conjuntos.
    
    Args:
        set1 (list): Primer conjunto representado como lista.
        set2 (list): Segundo conjunto representado como lista.

    Returns:
        list: Una lista que contiene la unión de los dos conjuntos, sin elementos duplicados.
    """
    result = set1[:]
    for elem in set2:
        if elem not in result:
            result.append(elem)
    return result

def intersection(set1, set2):
    """
    Realiza la intersección de dos conjuntos.
    
    Args:
        set1 (list): Primer conjunto representado como lista.
        set2 (list): Segundo conjunto representado como lista.

    Returns:
        list: Una lista que contiene la intersección de los dos conjuntos.
    """
    result = []
    for elem in set1:
        if elem in set2:
            result.append(elem)
    return result

def difference(set1, set2):
    """
    Realiza la diferencia entre dos conjuntos (set1 - set2).
    
    Args:
        set1 (list): Primer conjunto representado como lista.
        set2 (list): Segundo conjunto representado como lista.

    Returns:
        list: Una lista que contiene la diferencia de los dos conjuntos.
    """
    result = []
    for elem in set1:
        if elem not in set2:
            result.append(elem)
    return result

def symmetric_difference_multiple(conjuntos):
    """
    Realiza la diferencia simétrica entre múltiples conjuntos.
    
    Args:
        conjuntos (list of lists): Lista de listas donde cada lista representa un conjunto.

    Returns:
        list: Una lista que contiene la diferencia simétrica entre todos los conjuntos.
    """
    # Crear un diccionario para contar la cantidad de veces que aparece cada elemento
    element_counts = {}
    for conjunto in conjuntos:
        for elemento in conjunto:
            if elemento in element_counts:
                element_counts[elemento] += 1
            else:
                element_counts[elemento] = 1
    
    # Incluir en el resultado solo los elementos que aparecen un número impar de veces
    result = []
    for elemento, count in element_counts.items():
        if count == 1:
            result.append(elemento)
            
    return result

def complemento(universe, conjunto):
    """
    Calcula el complemento de un conjunto con respecto a un universo.
    
    Args:
        universe (list): El universo de elementos (A-Z, 0-9).
        conjunto (list): Conjunto a complementar.

    Returns:
        list: Una lista que contiene el complemento del conjunto.
    """
    result = []
    for elem in universe:
        if elem not in conjunto:
            result.append(elem)
    return result

def construir_conjuntos(conjuntos, universe):
    """
    Permite al usuario construir un conjunto de elementos.

    Args:
        conjuntos (dict): Diccionario donde se almacenan los conjuntos.
        universe (list): El universo de elementos válidos (A-Z, 0-9).
    """
    nombre = input("Nombre del conjunto: ")
    elementos = input("Ingresa los elementos separados por comas (A-Z, 0-9): ").upper().replace(" ", "")
    validos = list(universe)
    elementos_filtrados = [e for e in elementos.split(',') if e in validos]
    if len(elementos_filtrados) < len(elementos.split(',')):
        print("Algunos elementos ingresados no son válidos y han sido excluidos. Vuelve a crear el conjunto.")
        return
    
    conjunto = sorted(set(elementos_filtrados))
    conjuntos[nombre] = conjunto
    print(f"Conjunto {nombre} creado: {format_as_set_notation(conjunto)}")

def format_as_set_notation(char_set):
    """
    Formatea una lista de caracteres como una notación de conjunto.
    
    Args:
        char_set (list): Lista de caracteres a formatear.

    Returns:
        str: Una cadena que representa la lista en notación de conjunto.
    """
    return "{" + ", ".join(char_set) + "}"

def mostrar_resultado(conjuntos, result, operacion):
    """
    Muestra el resultado de una operación en notación de conjunto.
    
    Args:
        conjuntos (dict): Diccionario de conjuntos existentes.
        result (list): Lista de elementos resultantes de la operación.
        operacion (str): Nombre de la operación realizada.
    """
    formatted_result = format_as_set_notation(sorted(set(result)))
    for set_name, conjunto in conjuntos.items():
        print(f"{set_name}: {format_as_set_notation(sorted(set(conjunto)))}")
    print(f'Resultado de {operacion.lower()}: {formatted_result}')
    time.sleep(2)

def menu():
    """
    Muestra el menú principal del programa y gestiona la interacción con el usuario.
    """
    universe = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    conjuntos = {}
    while True:
        print("\nMenú Principal")
        print("1. Construir conjuntos")
        print("2. Operar conjuntos")
        print("3. Finalizar")
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            construir_conjuntos(conjuntos, universe)
        elif opcion == "2":
            subMenu(conjuntos, universe)
        elif opcion == "3":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

def subMenu(conjuntos, universe):
    """
    Muestra el submenú para realizar operaciones entre los conjuntos y gestiona la interacción con el usuario.
    
    Args:
        conjuntos (dict): Diccionario de conjuntos existentes.
        universe (list): El universo de elementos válidos (A-Z, 0-9).
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
            if len(conjuntos) >= 2:
                conjunto_names = list(conjuntos.keys())
                result = conjuntos[conjunto_names[0]]
                for name in conjunto_names[1:]:
                    result = union(result, conjuntos[name])
                complement_result = complemento(universe, result)
                mostrar_resultado(conjuntos, complement_result, "Complemento")    
            else:
                print("Se necesitan al menos 2 conjuntos para realizar esta operación.")
        elif opcion == "2":
            if len(conjuntos) >= 2:
                conjunto_names = list(conjuntos.keys())
                result = conjuntos[conjunto_names[0]]
                for name in conjunto_names[1:]:
                    result = union(result, conjuntos[name])
                mostrar_resultado(conjuntos, result, "Unión")
            else:
                print("Se necesitan al menos 2 conjuntos para realizar esta operación.")
        elif opcion == "3":
            if len(conjuntos) >= 2:
                conjunto_names = list(conjuntos.keys())
                result = conjuntos[conjunto_names[0]]
                for name in conjunto_names[1:]:
                    result = intersection(result, conjuntos[name])
                mostrar_resultado(conjuntos, result, "Intersección")
            else:
                print("Se necesitan al menos 2 conjuntos para realizar esta operación.")
        elif opcion == "4":
            if len(conjuntos) >= 2:
                conjunto_names = list(conjuntos.keys())
                result = conjuntos[conjunto_names[0]]
                for name in conjunto_names[1:]:
                    result = difference(result, conjuntos[name])
                mostrar_resultado(conjuntos, result, "Diferencia")
            else:
                print("Se necesitan al menos 2 conjuntos para realizar esta operación.")
        elif opcion == "5":
            if len(conjuntos) >= 2:
                result = symmetric_difference_multiple(conjuntos.values())
                mostrar_resultado(conjuntos, result, "Diferencia Simétrica")
            else:
                print("Se necesitan al menos 2 conjuntos para realizar esta operación.")
        elif opcion == "6":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

# Ejecutar el programa
menu()
