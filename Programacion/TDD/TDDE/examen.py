def sumar(arg):
    total = 0
    if arg == ([]):
        return "Error: No hay argumentos"

    if type(arg) is str:
        return 0
    
    if type(arg) is tuple:
        return 0

    for val in arg:
        total += val
    return total
